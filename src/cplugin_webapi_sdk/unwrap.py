"""Bridge generated endpoint ``Response`` objects to unwrapped ``data``.

Generated ``*_detailed`` / ``asyncio_detailed`` functions return a
``cplugin_webapi_sdk._generated.types.Response`` whose ``.content`` attribute
holds the raw v2 envelope JSON bytes. We re-parse those bytes with our pydantic
``ApiEnvelope`` to get a uniform ``{data, error, meta}`` seam:

- If ``envelope.error`` is non-null → raise ``ApiError``.
- Otherwise → return ``envelope.data`` (and ``envelope.meta`` for paged callers).

We deliberately re-parse the raw JSON instead of reading ``Response.parsed``
because the generated ``*ApiResponse`` model already strips the envelope one
level, making ``meta`` (and therefore ``paging``) inaccessible. Re-parsing is
cheap (single JSON round-trip) and gives the ergonomic client a reliable, typed
``(data, meta)`` pair for every response.

Public surface
--------------
``unwrap(response)``
    Sync — returns ``data`` or raises ``ApiError``.
``unwrap_with_meta(response)``
    Sync — returns ``(data, meta | None)``.
``unwrap_async(awaitable)``
    Async — awaits then delegates to ``unwrap``.
``unwrap_with_meta_async(awaitable)``
    Async — awaits then delegates to ``unwrap_with_meta``.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Awaitable

from pydantic import ValidationError

from .envelope import ApiEnvelope, ApiErrorBody, ApiMeta
from .errors import ApiError


# ---------------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------------

@dataclass
class Unwrapped:
    """Internal seam for the paged accessor (Task 6).

    Holds the two values we surface: the typed payload and the optional meta
    block that carries the pagination cursor.
    """

    data: Any
    meta: ApiMeta | None


def _parse(response: Any) -> tuple[Any, ApiMeta | None]:
    """Parse ``response.content`` into ``(data, meta)`` or raise ``ApiError``.

    ``response`` is duck-typed: any object with ``.status_code`` (int or
    ``http.HTTPStatus``) and ``.content`` (bytes) attributes is accepted.
    This matches the generated ``cplugin_webapi_sdk._generated.types.Response``
    without importing it here and creating a coupling to the generated layer.
    An optional ``.headers`` mapping is handed to ``ApiError`` so it can report
    ``X-Request-Outcome`` / ``X-Request-Timeout-Applied``.
    """
    raw: bytes = response.content
    headers = getattr(response, "headers", None)
    # * Decode bytes → str so json.loads always receives a str/bytes it can handle.
    text = raw.decode("utf-8") if isinstance(raw, (bytes, bytearray)) else raw

    try:
        # * model_validate parses camelCase JSON via field aliases defined in ApiEnvelope.
        env: ApiEnvelope[Any] = ApiEnvelope[Any].model_validate(json.loads(text))
    except (json.JSONDecodeError, ValidationError) as exc:
        # ! A TLS-terminating proxy (nginx, Caddy) can return an HTML 502/503/504
        # ! or an empty body before the server even sees the request.  Re-raise as
        # ! the SDK's own error type so callers need only catch ApiError.
        preview = text[:200].replace("\n", " ")
        status = int(response.status_code)
        body = ApiErrorBody(
            code="InvalidResponse",
            message=f"HTTP {status}: unparseable response body — {preview!r}",
            manager_code=None,
        )
        raise ApiError(body, None, status, headers) from exc

    if env.error is not None:
        # ! Raise before touching env.data — error payload may carry a non-null
        # ! data field on some future server versions; ignore it on error.
        raise ApiError(env.error, env.meta, int(response.status_code), headers)

    return env.data, env.meta


# ---------------------------------------------------------------------------
# Public sync API
# ---------------------------------------------------------------------------

def unwrap(response: Any) -> Any:
    """Return the ``data`` field of the v2 envelope, or raise ``ApiError``.

    Typical usage::

        response = get_api_v2_mt4_server_time.sync_detailed(tp, client=client)
        server_time: datetime = unwrap(response)
    """
    data, _ = _parse(response)
    return data


def unwrap_with_meta(response: Any) -> tuple[Any, ApiMeta | None]:
    """Return ``(data, meta)`` from the v2 envelope, or raise ``ApiError``.

    The ``meta`` value carries ``paging`` (cursor + ``has_more`` flag) for list
    endpoints. Non-list endpoints return ``meta.paging = None``.

    Typical usage::

        response = list_trades.sync_detailed(tp, client=client)
        trades, meta = unwrap_with_meta(response)
        cursor = meta.paging.next_cursor if meta and meta.paging else None
    """
    return _parse(response)


# ---------------------------------------------------------------------------
# Public async API
# ---------------------------------------------------------------------------

async def unwrap_async(awaitable_response: Awaitable[Any]) -> Any:
    """Await the async endpoint call, then return ``data`` or raise ``ApiError``.

    Typical usage::

        server_time = await unwrap_async(
            get_api_v2_mt4_server_time.asyncio_detailed(tp, client=client)
        )
    """
    response = await awaitable_response
    return unwrap(response)


async def unwrap_with_meta_async(awaitable_response: Awaitable[Any]) -> tuple[Any, ApiMeta | None]:
    """Await the async endpoint call, then return ``(data, meta)`` or raise ``ApiError``.

    Typical usage::

        trades, meta = await unwrap_with_meta_async(
            list_trades.asyncio_detailed(tp, client=client)
        )
    """
    response = await awaitable_response
    return unwrap_with_meta(response)
