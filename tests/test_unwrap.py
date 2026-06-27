"""Tests for unwrap.py — generated Response → data / ApiError + meta bridge.

FakeResp stands in for the generated `_generated.types.Response` dataclass.
Only `.status_code` and `.content` are exercised here (the two attributes that
`unwrap` actually reads).
"""
from __future__ import annotations

import json

import pytest

from cplugin_webapi_sdk.errors import ApiError
from cplugin_webapi_sdk.unwrap import unwrap, unwrap_async, unwrap_with_meta, unwrap_with_meta_async


# ---------------------------------------------------------------------------
# Minimal stand-in for cplugin_webapi_sdk._generated.types.Response
# ---------------------------------------------------------------------------

class FakeResp:
    """Minimal stand-in that mirrors the two attributes unwrap() reads."""

    def __init__(self, payload: dict, status: int = 200) -> None:
        self.status_code = status
        self.content = json.dumps(payload).encode()


# ---------------------------------------------------------------------------
# unwrap — sync, success path
# ---------------------------------------------------------------------------

def test_unwrap_returns_data_string():
    r = FakeResp({"data": "ok", "error": None, "meta": {"activityId": "a"}})
    assert unwrap(r) == "ok"


def test_unwrap_returns_data_list():
    r = FakeResp({"data": [1, 2, 3], "error": None, "meta": None})
    assert unwrap(r) == [1, 2, 3]


def test_unwrap_returns_data_dict():
    r = FakeResp({"data": {"key": "val"}, "error": None, "meta": None})
    assert unwrap(r) == {"key": "val"}


def test_unwrap_returns_data_numeric():
    r = FakeResp({"data": 42, "error": None, "meta": None})
    assert unwrap(r) == 42


def test_unwrap_null_data_no_error_returns_none():
    # * Success envelope with null data is valid (e.g. 204-style v2 responses).
    r = FakeResp({"data": None, "error": None, "meta": None})
    assert unwrap(r) is None


# ---------------------------------------------------------------------------
# unwrap — sync, error path
# ---------------------------------------------------------------------------

def test_unwrap_raises_apierror_on_error():
    r = FakeResp(
        {
            "data": None,
            "error": {"code": "NotFound", "managerCode": None, "message": "resource not found"},
            "meta": {"activityId": "trace-xyz"},
        }
    )
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    err = exc_info.value
    assert err.code == "NotFound"
    assert err.description == "resource not found"
    assert err.activity_id == "trace-xyz"
    assert err.status == 200


def test_unwrap_raises_apierror_with_manager_code():
    r = FakeResp(
        {
            "data": None,
            "error": {"code": "Internal", "managerCode": "3", "message": "mt4 error"},
            "meta": None,
        },
        status=200,
    )
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    err = exc_info.value
    assert err.manager_code == "3"
    assert err.activity_id is None  # meta was None


def test_unwrap_raises_apierror_carries_status_code():
    r = FakeResp(
        {"data": None, "error": {"code": "Unauthorized", "managerCode": None, "message": "jwt expired"}, "meta": None},
        status=401,
    )
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    assert exc_info.value.status == 401


# ---------------------------------------------------------------------------
# unwrap_with_meta — success path
# ---------------------------------------------------------------------------

def test_unwrap_with_meta_returns_data_and_meta():
    r = FakeResp(
        {
            "data": [1, 2],
            "error": None,
            "meta": {
                "activityId": "act-1",
                "paging": {"nextCursor": "cursor-abc", "hasMore": True},
            },
        }
    )
    data, meta = unwrap_with_meta(r)
    assert data == [1, 2]
    assert meta is not None
    assert meta.activity_id == "act-1"
    assert meta.paging is not None
    assert meta.paging.next_cursor == "cursor-abc"
    assert meta.paging.has_more is True


def test_unwrap_with_meta_returns_none_meta_when_absent():
    r = FakeResp({"data": "x", "error": None, "meta": None})
    data, meta = unwrap_with_meta(r)
    assert data == "x"
    assert meta is None


def test_unwrap_with_meta_raises_apierror_on_error():
    r = FakeResp(
        {
            "data": None,
            "error": {"code": "Forbidden", "managerCode": None, "message": "access denied"},
            "meta": {"activityId": "t-9"},
        }
    )
    with pytest.raises(ApiError) as exc_info:
        unwrap_with_meta(r)
    assert exc_info.value.code == "Forbidden"


# ---------------------------------------------------------------------------
# unwrap_async — async success + error paths
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_unwrap_async_awaits_and_returns_data():
    async def coro():
        return FakeResp({"data": 99, "error": None, "meta": None})

    assert await unwrap_async(coro()) == 99


@pytest.mark.asyncio
async def test_unwrap_async_raises_apierror():
    async def coro():
        return FakeResp(
            {"data": None, "error": {"code": "NotFound", "managerCode": None, "message": "nope"}, "meta": None}
        )

    with pytest.raises(ApiError) as exc_info:
        await unwrap_async(coro())
    assert exc_info.value.code == "NotFound"


# ---------------------------------------------------------------------------
# unwrap_with_meta_async
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_unwrap_with_meta_async_returns_data_and_meta():
    async def coro():
        return FakeResp(
            {
                "data": "page-result",
                "error": None,
                "meta": {"activityId": "async-trace", "paging": {"nextCursor": "tok", "hasMore": False}},
            }
        )

    data, meta = await unwrap_with_meta_async(coro())
    assert data == "page-result"
    assert meta.paging.next_cursor == "tok"
    assert meta.paging.has_more is False


@pytest.mark.asyncio
async def test_unwrap_with_meta_async_raises_apierror():
    async def coro():
        return FakeResp(
            {"data": None, "error": {"code": "Internal", "managerCode": "7", "message": "crash"}, "meta": None}
        )

    with pytest.raises(ApiError):
        await unwrap_with_meta_async(coro())


# ---------------------------------------------------------------------------
# Malformed / non-JSON / empty response body → ApiError(code="InvalidResponse")
# ---------------------------------------------------------------------------

class RawResp:
    """Stand-in that accepts arbitrary raw bytes (not a JSON-serialisable dict)."""

    def __init__(self, content: bytes, status: int = 200) -> None:
        self.status_code = status
        self.content = content


def test_empty_body_raises_invalid_response():
    # (a) Empty body — json.JSONDecodeError → ApiError with code "InvalidResponse".
    r = RawResp(b"", status=502)
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    err = exc_info.value
    assert err.code == "InvalidResponse"
    assert err.status == 502


def test_html_body_raises_invalid_response():
    # (b) Proxy HTML error page — json.JSONDecodeError → ApiError with code "InvalidResponse".
    r = RawResp(b"<html><body>503 Service Unavailable</body></html>", status=503)
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    err = exc_info.value
    assert err.code == "InvalidResponse"
    assert err.status == 503


def test_structurally_wrong_json_raises_invalid_response():
    # Valid JSON but not an ApiEnvelope — pydantic ValidationError → ApiError.
    r = RawResp(b'["not", "an", "envelope"]', status=200)
    with pytest.raises(ApiError) as exc_info:
        unwrap(r)
    assert exc_info.value.code == "InvalidResponse"


@pytest.mark.asyncio
async def test_empty_body_async_raises_invalid_response():
    # Async path delegates to sync _parse — one async case confirms the bridge works.
    async def coro():
        return RawResp(b"", status=503)

    with pytest.raises(ApiError) as exc_info:
        await unwrap_async(coro())
    err = exc_info.value
    assert err.code == "InvalidResponse"
    assert err.status == 503
