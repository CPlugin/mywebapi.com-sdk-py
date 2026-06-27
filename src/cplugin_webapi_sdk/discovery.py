"""OIDC discovery — fetches ``.well-known/openid-configuration`` once and
caches the parsed document for the lifetime of the process.

Sync and async paths share the same cache: the first caller to populate it
wins, all subsequent callers (sync or async) get the cached document with no
further network IO. Locks guard only the *first* fetch — once cached, reads
are lock-free.
"""
from __future__ import annotations

import asyncio
import threading
from typing import Any

import httpx


class OidcDiscovery:
    """Single-flight OIDC discovery document fetcher."""

    def __init__(
        self,
        identity_url: str,
        http_sync: httpx.Client | None = None,
        http_async: httpx.AsyncClient | None = None,
    ) -> None:
        self._identity_url = identity_url.rstrip("/")
        self._http_sync = http_sync
        self._http_async = http_async
        self._cached: dict[str, Any] | None = None
        self._lock_sync = threading.Lock()
        self._lock_async = asyncio.Lock()

    @property
    def discovery_url(self) -> str:
        return f"{self._identity_url}/.well-known/openid-configuration"

    def get_sync(self) -> dict[str, Any]:
        # Fast path — lock-free read once populated.
        if self._cached is not None:
            return self._cached
        with self._lock_sync:
            if self._cached is not None:
                return self._cached
            client = self._http_sync or httpx.Client()
            owns_client = self._http_sync is None
            try:
                r = client.get(self.discovery_url)
            finally:
                if owns_client:
                    client.close()
            self._cached = self._validate_doc(self._parse_response(r))
            return self._cached

    async def get_async(self) -> dict[str, Any]:
        if self._cached is not None:
            return self._cached
        async with self._lock_async:
            if self._cached is not None:
                return self._cached
            client = self._http_async or httpx.AsyncClient()
            owns_client = self._http_async is None
            try:
                r = await client.get(self.discovery_url)
            finally:
                if owns_client:
                    await client.aclose()
            self._cached = self._validate_doc(self._parse_response(r))
            return self._cached

    @staticmethod
    def _parse_response(r: httpx.Response) -> dict[str, Any]:
        # Defer import to avoid circular dependency at module import time.
        from .auth import OAuth2TokenError

        if r.status_code < 200 or r.status_code >= 300:
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="discovery_failed",
                error_description=f"OIDC discovery returned HTTP {r.status_code}",
            )
        try:
            doc = r.json()
        except Exception as e:  # noqa: BLE001
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="discovery_failed",
                error_description=f"OIDC discovery response was not JSON: {e}",
            ) from e
        if not isinstance(doc, dict):
            raise OAuth2TokenError(
                status_code=r.status_code,
                error="discovery_failed",
                error_description="OIDC discovery document was not a JSON object",
            )
        return doc

    @staticmethod
    def _validate_doc(doc: dict[str, Any]) -> dict[str, Any]:
        from .auth import OAuth2TokenError

        endpoint = doc.get("token_endpoint")
        if not isinstance(endpoint, str) or not endpoint:
            raise OAuth2TokenError(
                status_code=0,
                error="discovery_invalid",
                error_description="OIDC discovery document missing token_endpoint",
            )
        return doc
