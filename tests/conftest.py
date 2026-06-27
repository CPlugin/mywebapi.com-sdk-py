"""Test fixtures for the WebAPI v2 Python SDK.

Two fixture families live here:

1. **Mock fixtures** — ``API``, ``AUTH``, ``oidc_doc``, ``discovery_url``,
   ``token_endpoint``, ``token_body``, ``envelope_ok``, ``envelope_err`` —
   used by respx-based contract tests (no live server required).

2. **Live fixtures** — ``jwt_token``, ``trade_platform``, ``known_login`` —
   skipped automatically when the required env vars are not set.

Live env vars (or ``.env`` in ``clients/python/``):

* ``WEBAPI_BASE_URL``
* ``WEBAPI_AUTH_SERVER``
* ``WEBAPI_CLIENT_ID``
* ``WEBAPI_CLIENT_SECRET``
* ``WEBAPI_TRADE_PLATFORM``
* ``WEBAPI_KNOWN_LOGIN``
"""
import os
import pytest
import httpx


# ---------------------------------------------------------------------------
# Mock environment constants (used by respx-based tests)
# ---------------------------------------------------------------------------

# * Base URL for the mock API server used in contract tests.
API = "https://api.test"
# * OIDC authority for the mock identity server used in contract tests.
AUTH = "https://auth.test"


# ---------------------------------------------------------------------------
# Mock fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def oidc_doc():
    """Minimal OIDC discovery document for the mock authority."""
    return {
        "issuer": AUTH,
        "token_endpoint": f"{AUTH}/connect/token",
    }


@pytest.fixture
def discovery_url():
    """URL of the mock OIDC discovery endpoint."""
    return f"{AUTH}/.well-known/openid-configuration"


@pytest.fixture
def token_endpoint():
    """URL of the mock OAuth2 token endpoint."""
    return f"{AUTH}/connect/token"


def token_body(access_token: str = "tok-1") -> dict:
    """Return a minimal successful token response body."""
    return {"access_token": access_token, "token_type": "Bearer", "expires_in": 3600}


def envelope_ok(data) -> dict:
    """Return a v2 envelope with the given data payload and no error."""
    return {
        "data": data,
        "error": None,
        "meta": {"activityId": "a1", "paging": None},
    }


def envelope_err(code: str = "Forbidden", message: str = "nope") -> dict:
    """Return a v2 envelope carrying an error payload."""
    return {
        "data": None,
        "error": {"code": code, "managerCode": None, "message": message},
        "meta": {"activityId": "trace-1", "paging": None},
    }


# ---------------------------------------------------------------------------
# Live test fixtures (skipped when env vars are absent)
# ---------------------------------------------------------------------------

def _env(name: str) -> str:
    v = os.environ.get(name)
    if not v:
        pytest.skip(f"{name} not set — live-WebAPI test")
    return v


@pytest.fixture(scope="session")
def jwt_token() -> str:
    auth = _env("WEBAPI_AUTH_SERVER").rstrip("/")
    cid = _env("WEBAPI_CLIENT_ID")
    sec = _env("WEBAPI_CLIENT_SECRET")
    r = httpx.post(
        f"{auth}/connect/token",
        data={
            "grant_type": "client_credentials",
            "client_id": cid,
            "client_secret": sec,
            "scope": "openid profile WebAPI",
        },
        timeout=15.0,
    )
    r.raise_for_status()
    return r.json()["access_token"]


@pytest.fixture
def trade_platform() -> str:
    return _env("WEBAPI_TRADE_PLATFORM")


@pytest.fixture
def known_login() -> int:
    return int(_env("WEBAPI_KNOWN_LOGIN"))
