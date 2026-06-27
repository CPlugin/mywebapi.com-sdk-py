"""Unit tests for auth / discovery / client integration.

These tests are hermetic — every external HTTP request is mocked via respx.
The OIDC discovery fixture is vendored under ``tests/fixtures/`` so this
package is self-contained; it mirrors the cross-language shared fixture used
by the TS, C#, and PowerShell SDKs so all assert against the same document.
"""
from __future__ import annotations

import asyncio
import concurrent.futures
import json
import os
import threading
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from cplugin_webapi_sdk import (
    BearerAuth,
    ClientCredentialsAuth,
    OAuth2TokenError,
)


# ---------- fixtures ----------

FIXTURE_PATH = (
    Path(__file__).parent / "fixtures/openid-configuration.json"
).resolve()


@pytest.fixture(scope="module")
def oidc_doc() -> dict[str, Any]:
    with FIXTURE_PATH.open() as f:
        return json.load(f)


@pytest.fixture
def discovery_url() -> str:
    return "https://identity.example/.well-known/openid-configuration"


@pytest.fixture
def token_endpoint() -> str:
    return "https://identity.example/connect/token"


@pytest.fixture
def api_base() -> str:
    return "https://api.example"


@pytest.fixture
def envelope_ok() -> dict[str, Any]:
    return {
        "isError": False,
        "errorCode": None,
        "errorDescription": None,
        "managerAPICode": None,
        "activityId": "00000000-0000-0000-0000-000000000000",
        "payload": "2026-05-15T00:00:00Z",
    }


def _token_body(access_token: str = "tok_abc", expires_in: int = 3600) -> dict[str, Any]:
    return {"access_token": access_token, "expires_in": expires_in, "token_type": "Bearer"}


# ---------- BearerAuth ----------

def test_bearer_auth_sync_adds_header():
    with respx.mock(assert_all_called=False) as mock:
        route = mock.get("https://api.example/x").mock(return_value=httpx.Response(200, json={"ok": True}))
        with httpx.Client(auth=BearerAuth("static_jwt")) as c:
            r = c.get("https://api.example/x")
        assert r.status_code == 200
        sent = route.calls.last.request
        assert sent.headers["authorization"] == "Bearer static_jwt"


@pytest.mark.asyncio
async def test_bearer_auth_async_adds_header():
    with respx.mock(assert_all_called=False) as mock:
        route = mock.get("https://api.example/x").mock(return_value=httpx.Response(200, json={"ok": True}))
        async with httpx.AsyncClient(auth=BearerAuth("static_jwt")) as c:
            r = await c.get("https://api.example/x")
        assert r.status_code == 200
        sent = route.calls.last.request
        assert sent.headers["authorization"] == "Bearer static_jwt"


def test_bearer_auth_rejects_empty():
    with pytest.raises(ValueError):
        BearerAuth("")


# ---------- ClientCredentialsAuth cold start ----------

def test_client_credentials_sync_cold_start(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            r = c.get(f"{api_base}/x")

        assert r.status_code == 200
        assert disc.call_count == 1
        assert tok.call_count == 1
        assert api.call_count == 1
        assert api.calls.last.request.headers["authorization"] == "Bearer tok_abc"


@pytest.mark.asyncio
async def test_client_credentials_async_cold_start(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        async with httpx.AsyncClient(auth=auth) as c:
            r = await c.get(f"{api_base}/x")

        assert r.status_code == 200
        assert disc.call_count == 1
        assert tok.call_count == 1
        assert api.call_count == 1
        assert api.calls.last.request.headers["authorization"] == "Bearer tok_abc"


# ---------- caching ----------

def test_client_credentials_caches_token_within_ttl(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            c.get(f"{api_base}/x")
            c.get(f"{api_base}/x")

        assert disc.call_count == 1
        assert tok.call_count == 1
        assert api.call_count == 2


def test_client_credentials_refetches_token_after_expiry(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            c.get(f"{api_base}/x")
            auth._invalidate_cache_for_tests()
            c.get(f"{api_base}/x")

        assert disc.call_count == 1  # discovery stays cached
        assert tok.call_count == 2
        assert api.call_count == 2


# ---------- single-flight ----------

def test_client_credentials_single_flight_sync(oidc_doc, discovery_url, token_endpoint, api_base):
    """50 concurrent threads share exactly one token fetch."""
    barrier = threading.Barrier(50)

    def slow_token(_req: httpx.Request) -> httpx.Response:
        # Hold the lock-holder inside the critical section long enough for
        # all 50 threads to queue up on the lock.
        barrier_wait_safely(barrier)
        return httpx.Response(200, json=_token_body())

    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(side_effect=slow_token)
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        client = httpx.Client(auth=auth)
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
                # Dispatch all 50 first — DO NOT wait between submits.
                futs = [ex.submit(client.get, f"{api_base}/x") for _ in range(50)]
                for f in futs:
                    f.result()
        finally:
            client.close()

        # respx fixture serialises matches but our auth lock should still
        # collapse all 50 concurrent waiters into 1 token call.
        assert tok.call_count == 1
        assert disc.call_count == 1
        assert api.call_count == 50


def barrier_wait_safely(barrier: threading.Barrier) -> None:
    """Wait at the barrier but don't block forever in a single-thread test."""
    try:
        barrier.wait(timeout=0.05)
    except threading.BrokenBarrierError:
        # Single-flight kicks in — only one thread reaches the barrier.
        pass


@pytest.mark.asyncio
async def test_client_credentials_single_flight_async(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        async with httpx.AsyncClient(auth=auth) as c:
            # Dispatch all 50 first — gather awaits in a single point.
            await asyncio.gather(*[c.get(f"{api_base}/x") for _ in range(50)])

        assert tok.call_count == 1
        assert disc.call_count == 1
        assert api.call_count == 50


# ---------- 401 handling ----------

def test_client_credentials_retries_once_on_401(oidc_doc, discovery_url, token_endpoint, api_base):
    responses = iter([
        httpx.Response(401, json={"error": "invalid_token"}),
        httpx.Response(200, json={"ok": True}),
    ])

    with respx.mock() as mock:
        mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(side_effect=lambda _r: next(responses))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            r = c.get(f"{api_base}/x")

        assert r.status_code == 200
        assert tok.call_count == 2  # initial + forced refresh
        assert api.call_count == 2


def test_client_credentials_gives_up_after_second_401(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(401, json={"error": "still_no"}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            r = c.get(f"{api_base}/x")

        assert r.status_code == 401  # surfaced, no infinite loop
        assert tok.call_count == 2
        assert api.call_count == 2


# ---------- error surfaces ----------

def test_oauth2_token_error_on_invalid_client(oidc_doc, discovery_url, token_endpoint, api_base):
    with respx.mock() as mock:
        mock.get(discovery_url).mock(return_value=httpx.Response(200, json=oidc_doc))
        mock.post(token_endpoint).mock(return_value=httpx.Response(
            400, json={"error": "invalid_client", "error_description": "bad creds"},
        ))
        # No API mock — auth should fail before reaching it.

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            with pytest.raises(OAuth2TokenError) as ei:
                c.get(f"{api_base}/x")

        e = ei.value
        assert e.status_code == 400
        assert e.error == "invalid_client"
        assert e.error_description == "bad creds"
        assert "invalid_client" in str(e)
        assert "400" in str(e)


def test_discovery_failure_then_retry_succeeds(oidc_doc, discovery_url, token_endpoint, api_base):
    """If discovery 404s, the failure is surfaced. After the failure the
    cache stays empty so the next attempt re-tries discovery — and succeeds."""
    disc_responses = iter([
        httpx.Response(404, text="not found"),
        httpx.Response(200, json=oidc_doc),
    ])

    with respx.mock() as mock:
        disc = mock.get(discovery_url).mock(side_effect=lambda _r: next(disc_responses))
        tok = mock.post(token_endpoint).mock(return_value=httpx.Response(200, json=_token_body()))
        api = mock.get(f"{api_base}/x").mock(return_value=httpx.Response(200, json={"ok": True}))

        auth = ClientCredentialsAuth(
            client_id="cid", client_secret="csec",
            identity_url="https://identity.example",
        )
        with httpx.Client(auth=auth) as c:
            with pytest.raises(OAuth2TokenError):
                c.get(f"{api_base}/x")
            # Second attempt should retry discovery and succeed.
            r = c.get(f"{api_base}/x")

        assert r.status_code == 200
        assert disc.call_count == 2
        assert tok.call_count == 1
        assert api.call_count == 1

        assert api.call_count == 1
