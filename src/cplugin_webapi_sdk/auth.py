"""httpx auth classes for the WebAPI v2 client.

* ``BearerAuth`` — wraps a static JWT. No refresh, no 401 retry.
* ``ClientCredentialsAuth`` — OAuth2 client_credentials with discovery,
  single-flight token fetching, expiry-driven refresh, and a one-shot 401
  retry that forces a refresh before yielding the request again.

Both implement httpx's sync + async ``Auth`` generator protocol so a single
auth instance can be shared between ``httpx.Client`` and ``httpx.AsyncClient``.

``time.monotonic()`` is used everywhere for expiry math — wall-clock jumps
(NTP, container clock skew) must not invalidate or extend tokens. The
server's ``expires_in`` is already a relative duration, so monotonic is the
correct reference.
"""
from __future__ import annotations

import asyncio
import threading
import time
from typing import Any, Generator, AsyncGenerator

import httpx

from .discovery import OidcDiscovery


class OAuth2TokenError(Exception):
    """Raised when token acquisition fails (network, 4xx, malformed body)."""

    def __init__(
        self,
        status_code: int,
        error: str | None = None,
        error_description: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.error = error
        self.error_description = error_description
        super().__init__(str(self))

    def __str__(self) -> str:
        err = self.error or "oauth2_error"
        desc = self.error_description or "token request failed"
        return f"OAuth2 token error ({err} / {self.status_code}): {desc}"


class BearerAuth(httpx.Auth):
    """Attach a static bearer token. No refresh, no 401 handling."""

    requires_response_body = False

    def __init__(self, token: str) -> None:
        if not token:
            raise ValueError("BearerAuth requires a non-empty token")
        self._token = token

    def current_token(self) -> str:
        """Return the static bearer token (public accessor for Task 9 realtime wiring)."""
        return self._token

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"Bearer {self._token}"
        yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        request.headers["Authorization"] = f"Bearer {self._token}"
        yield request


class ClientCredentialsAuth(httpx.Auth):
    """OAuth2 client_credentials with single-flight caching + 401 retry.

    Behaviour:

    * On every request, attach the cached token (fetch it if missing/expired).
    * If the response is 401, force-refresh once and yield the request again.
    * Token fetch is single-flight per process — concurrent callers wait on
      the lock and reuse whatever the first caller acquired.
    * Expiry uses ``time.monotonic()`` minus a ``skew_seconds`` safety margin.
    """

    # We need the body to surface ``error_description`` from the IdP on 401.
    requires_response_body = True

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        identity_url: str,
        scopes: list[str] | None = None,
        skew_seconds: int = 60,
        http_sync: httpx.Client | None = None,
        http_async: httpx.AsyncClient | None = None,
    ) -> None:
        if not client_id:
            raise ValueError("client_id is required")
        if not client_secret:
            raise ValueError("client_secret is required")
        if not identity_url:
            raise ValueError("identity_url is required")
        self._client_id = client_id
        self._client_secret = client_secret
        self._scopes = list(scopes) if scopes else None
        self._skew = skew_seconds
        self._http_sync = http_sync
        self._http_async = http_async
        self._discovery = OidcDiscovery(identity_url, http_sync, http_async)
        self._cached_token: str | None = None
        self._expires_at: float = 0.0
        self._lock_sync = threading.Lock()
        self._lock_async = asyncio.Lock()

    # ---------- httpx hook points ----------

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"Bearer {self._get_token_sync(force=False)}"
        response = yield request
        if response.status_code == 401:
            request.headers["Authorization"] = f"Bearer {self._get_token_sync(force=True)}"
            yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        request.headers["Authorization"] = f"Bearer {await self._get_token_async(force=False)}"
        response = yield request
        if response.status_code == 401:
            request.headers["Authorization"] = f"Bearer {await self._get_token_async(force=True)}"
            yield request

    # ---------- token acquisition ----------

    def _is_token_fresh(self) -> bool:
        return (
            self._cached_token is not None
            and (self._expires_at - time.monotonic()) > self._skew
        )

    def _form_body(self) -> dict[str, str]:
        body = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        if self._scopes:
            body["scope"] = " ".join(self._scopes)
        return body

    def _apply_token_response(self, r: httpx.Response) -> str:
        if r.status_code < 200 or r.status_code >= 300:
            err: str | None = None
            desc: str | None = None
            try:
                body = r.json()
                if isinstance(body, dict):
                    err = body.get("error")
                    desc = body.get("error_description")
            except Exception:  # noqa: BLE001
                pass
            raise OAuth2TokenError(
                status_code=r.status_code,
                error=err,
                error_description=desc or f"token endpoint returned HTTP {r.status_code}",
            )
        try:
            body = r.json()
        except Exception as e:  # noqa: BLE001
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="invalid_response",
                error_description=f"token endpoint response was not JSON: {e}",
            ) from e
        if not isinstance(body, dict):
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="invalid_response",
                error_description="token endpoint response was not a JSON object",
            )
        access_token = body.get("access_token")
        expires_in = body.get("expires_in")
        if not isinstance(access_token, str) or not access_token:
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="invalid_response",
                error_description="token endpoint response missing access_token",
            )
        if not isinstance(expires_in, (int, float)) or expires_in <= 0:
            # Sensible default if IdP omits or returns a bad value.
            expires_in = 3600
        self._cached_token = access_token
        self._expires_at = time.monotonic() + float(expires_in)
        return access_token

    def current_token(self) -> str:
        """Return the current cached/refreshed bearer token (public accessor).

        Performs a lazy fetch or returns the cached token without forcing a
        refresh. Used by Task 9 realtime wiring via ``_token_getter``.
        """
        return self._get_token_sync(force=False)

    def _get_token_sync(self, force: bool) -> str:
        if not force and self._is_token_fresh():
            return self._cached_token  # type: ignore[return-value]
        with self._lock_sync:
            if not force and self._is_token_fresh():
                return self._cached_token  # type: ignore[return-value]
            doc = self._discovery.get_sync()
            endpoint = doc["token_endpoint"]
            client = self._http_sync or httpx.Client()
            owns_client = self._http_sync is None
            try:
                r = client.post(
                    endpoint,
                    data=self._form_body(),
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json",
                    },
                )
            finally:
                if owns_client:
                    client.close()
            return self._apply_token_response(r)

    async def _get_token_async(self, force: bool) -> str:
        if not force and self._is_token_fresh():
            return self._cached_token  # type: ignore[return-value]
        async with self._lock_async:
            if not force and self._is_token_fresh():
                return self._cached_token  # type: ignore[return-value]
            doc = await self._discovery.get_async()
            endpoint = doc["token_endpoint"]
            client = self._http_async or httpx.AsyncClient()
            owns_client = self._http_async is None
            try:
                r = await client.post(
                    endpoint,
                    data=self._form_body(),
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json",
                    },
                )
            finally:
                if owns_client:
                    await client.aclose()
            return self._apply_token_response(r)

    # ---------- test/debug hooks ----------

    def _invalidate_cache_for_tests(self) -> None:
        """Force the next request to fetch a fresh token. Test-only."""
        self._expires_at = 0.0

    def _cached_token_for_tests(self) -> str | None:
        return self._cached_token

    # ---------- introspection ----------

    @property
    def expires_in(self) -> float:
        """Seconds remaining until the cached token expires (monotonic-based)."""
        if self._cached_token is None:
            return 0.0
        return max(0.0, self._expires_at - time.monotonic())

    @property
    def has_token(self) -> bool:
        return self._cached_token is not None
