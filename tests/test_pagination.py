"""Tests for pagination.py — cursor-based page iteration over meta.paging.

The ``fetch_page`` callback returns ``(items, meta)`` — the same shape that
namespace ``*_request`` methods return via ``unwrap_with_meta``.  We simulate
three pages of data and verify both the page-by-page and flat-collect helpers.
"""
from __future__ import annotations

import pytest
from cplugin_webapi_sdk.envelope import ApiMeta
from cplugin_webapi_sdk.pagination import (
    collect_all_async,
    collect_all_sync,
    paginate_async,
    paginate_sync,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _meta(next_cursor: str | None, has_more: bool) -> ApiMeta:
    """Build an ApiMeta with paging populated."""
    return ApiMeta.model_validate(
        {"activityId": None, "paging": {"nextCursor": next_cursor, "hasMore": has_more}}
    )


def _make_sync_pager():
    """Return a sync fetch_page callable that walks three pages."""
    pages: dict = {
        None:  ([1, 2], _meta("c2", True)),
        "c2":  ([3, 4], _meta("c3", True)),
        "c3":  ([5],    _meta(None, False)),
    }

    def fetch(cursor: str | None):
        return pages[cursor]

    return fetch


def _make_async_pager():
    """Return an async fetch_page callable wrapping the same three pages."""
    sync_fetch = _make_sync_pager()

    async def afetch(cursor: str | None):
        return sync_fetch(cursor)

    return afetch


# ---------------------------------------------------------------------------
# paginate_sync — yields pages one by one
# ---------------------------------------------------------------------------

def test_paginate_sync_yields_three_pages():
    out = list(paginate_sync(_make_sync_pager()))
    assert out == [[1, 2], [3, 4], [5]]


def test_paginate_sync_single_page_no_more():
    """A single page with has_more=False should yield exactly once."""
    def fetch(cursor):
        return (["only"], _meta(None, False))

    assert list(paginate_sync(fetch)) == [["only"]]


def test_paginate_sync_stops_when_next_cursor_is_none_but_has_more_false():
    """Stopping condition: has_more=False wins even if next_cursor is non-null."""
    calls = []

    def fetch(cursor):
        calls.append(cursor)
        return (["x"], _meta("ghost", False))

    result = list(paginate_sync(fetch))
    assert result == [["x"]]
    assert len(calls) == 1  # * only one call made


def test_paginate_sync_with_null_meta():
    """If meta is None (non-paged endpoint), yield once and stop gracefully."""
    def fetch(cursor):
        return (["a", "b"], None)

    assert list(paginate_sync(fetch)) == [["a", "b"]]


def test_paginate_sync_stops_when_has_more_true_but_no_cursor():
    """has_more=True without a cursor must not loop — guards against a server bug."""
    calls = []

    def fetch(cursor):
        calls.append(cursor)
        return (["x"], _meta(None, True))  # has_more=True, but next_cursor=None

    result = list(paginate_sync(fetch))
    assert result == [["x"]]
    assert len(calls) == 1


# ---------------------------------------------------------------------------
# collect_all_sync — flattens all pages into one list
# ---------------------------------------------------------------------------

def test_collect_all_sync_flattens():
    assert collect_all_sync(_make_sync_pager()) == [1, 2, 3, 4, 5]


def test_collect_all_sync_empty_page_included():
    """Empty pages do not break collection; the full sequence is returned."""
    pages = {
        None:  ([], _meta("c2", True)),
        "c2":  ([7], _meta(None, False)),
    }

    def fetch(cursor):
        return pages[cursor]

    assert collect_all_sync(fetch) == [7]


# ---------------------------------------------------------------------------
# paginate_async — async generator yielding pages
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_paginate_async_yields_three_pages():
    out = [page async for page in paginate_async(_make_async_pager())]
    assert out == [[1, 2], [3, 4], [5]]


@pytest.mark.asyncio
async def test_paginate_async_single_page():
    async def afetch(cursor):
        return (["only"], _meta(None, False))

    out = [page async for page in paginate_async(afetch)]
    assert out == [["only"]]


@pytest.mark.asyncio
async def test_paginate_async_null_meta():
    """Null meta from non-paged endpoint: yield once, stop."""
    async def afetch(cursor):
        return (["z"], None)

    out = [page async for page in paginate_async(afetch)]
    assert out == [["z"]]


@pytest.mark.asyncio
async def test_paginate_async_stops_when_has_more_true_but_no_cursor():
    """has_more=True without a cursor must not loop — guards against a server bug."""
    calls = []

    async def afetch(cursor):
        calls.append(cursor)
        return (["x"], _meta(None, True))  # has_more=True, but next_cursor=None

    out = [page async for page in paginate_async(afetch)]
    assert out == [["x"]]
    assert len(calls) == 1


# ---------------------------------------------------------------------------
# collect_all_async — async flatten
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_collect_all_async_flattens():
    assert await collect_all_async(_make_async_pager()) == [1, 2, 3, 4, 5]


@pytest.mark.asyncio
async def test_collect_all_async_empty_pages():
    pages = {
        None:  ([], _meta("tok", True)),
        "tok": ([99], _meta(None, False)),
    }

    async def afetch(cursor):
        return pages[cursor]

    assert await collect_all_async(afetch) == [99]
