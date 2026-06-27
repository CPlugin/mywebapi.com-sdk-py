"""Cursor pagination over the v2 envelope's ``meta.paging``.

Mirrors the TS SDK's ``paginate()`` / ``collectAll()`` helpers with sync AND
async symmetry.

The ``fetch_page(cursor)`` callback contract
-------------------------------------------
- Accepts a cursor token (``str | None``; ``None`` means "first page").
- Returns ``(items, meta)`` — the same tuple that namespace ``*_request``
  methods produce via ``unwrap_with_meta``.  ``meta`` may be ``None`` on
  non-paged endpoints; the helpers stop gracefully in that case.

Continuation rule
-----------------
- Continue while ``meta.paging.has_more is True`` AND
  ``meta.paging.next_cursor`` is non-empty.
- Either sentinel alone stops iteration:
  - ``has_more=False`` → stop (even if ``next_cursor`` happens to be set).
  - ``next_cursor=None/""`` → stop (defensive guard against server omission).
  - ``meta=None`` or ``meta.paging=None`` → treat as last page and stop.
"""
from __future__ import annotations

from typing import Any, AsyncGenerator, Awaitable, Callable, Iterator

from .envelope import ApiMeta

# * Type aliases describing the callback contract.
_PageResult = tuple[list[Any], ApiMeta | None]
PageFetcherSync = Callable[[str | None], _PageResult]
PageFetcherAsync = Callable[[str | None], Awaitable[_PageResult]]


# ---------------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------------

def _next_cursor(meta: ApiMeta | None) -> str | None:
    """Extract the next cursor from a page's metadata, or ``None`` to stop.

    Returns ``None`` when:
    - ``meta`` is ``None`` (non-paged endpoint or server omission).
    - ``meta.paging`` is ``None``.
    - ``meta.paging.has_more`` is ``False``.
    - ``meta.paging.next_cursor`` is ``None`` or empty string.
    """
    if meta is None or meta.paging is None:
        return None
    if not meta.paging.has_more:
        return None
    # * Treat empty string the same as None — defensive against server quirks.
    return meta.paging.next_cursor or None


# ---------------------------------------------------------------------------
# Public sync API
# ---------------------------------------------------------------------------

def paginate_sync(fetch_page: PageFetcherSync) -> Iterator[list[Any]]:
    """Yield successive pages from a cursor-paginated endpoint (sync).

    ``fetch_page`` is called with the current cursor (``None`` for the first
    page) and must return ``(items, meta)``.  Iteration stops when
    ``meta.paging.has_more`` is ``False`` or ``next_cursor`` is absent.

    Example::

        for page in paginate_sync(lambda cur: client.mt4.users_request(tp, cursor=cur)):
            for user in page:
                process(user)
    """
    cursor: str | None = None
    while True:
        items, meta = fetch_page(cursor)
        yield items
        cursor = _next_cursor(meta)
        if cursor is None:
            return


def collect_all_sync(fetch_page: PageFetcherSync) -> list[Any]:
    """Drain all pages into a single flat list (sync).

    Convenience wrapper around :func:`paginate_sync`.  For large collections
    prefer :func:`paginate_sync` to avoid materialising all records in memory.

    Example::

        all_users = collect_all_sync(
            lambda cur: client.mt4.users_request(tp, cursor=cur)
        )
    """
    out: list[Any] = []
    for page in paginate_sync(fetch_page):
        out.extend(page)
    return out


# ---------------------------------------------------------------------------
# Public async API
# ---------------------------------------------------------------------------

async def paginate_async(fetch_page: PageFetcherAsync) -> AsyncGenerator[list[Any], None]:
    """Async generator yielding successive pages from a cursor-paginated endpoint.

    ``fetch_page`` must be an async callable accepting a cursor and returning
    ``(items, meta)``.  Mirrors :func:`paginate_sync` exactly.

    Example::

        async for page in paginate_async(
            lambda cur: client.mt4.users_request(tp, cursor=cur)
        ):
            for user in page:
                await process(user)
    """
    cursor: str | None = None
    while True:
        items, meta = await fetch_page(cursor)
        yield items
        cursor = _next_cursor(meta)
        if cursor is None:
            return


async def collect_all_async(fetch_page: PageFetcherAsync) -> list[Any]:
    """Drain all pages into a single flat list (async).

    Convenience wrapper around :func:`paginate_async`.  For large collections
    prefer :func:`paginate_async` to avoid materialising all records in memory.

    Example::

        all_users = await collect_all_async(
            lambda cur: client.mt4.users_request(tp, cursor=cur)
        )
    """
    out: list[Any] = []
    async for page in paginate_async(fetch_page):
        out.extend(page)
    return out
