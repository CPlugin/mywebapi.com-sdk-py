"""Contract tests for CPluginWebApiClient / CPluginWebApiAsyncClient.

Tests use respx to mock the HTTP layer — no live server required. They verify:
- Namespace existence (.mt4, .mt5) and expected method surface.
- Happy-path: envelope unwrapping returns the ``data`` field.
- Error-path: error envelope raises ``ApiError`` with correct attributes.
- ``list_trade_platforms()`` — raw v1 array, no envelope.
- 401 forces auth refresh + retry (auth.ClientCredentialsAuth behaviour).
- Context-manager protocol (sync ``__enter__`` / ``__exit__``).
- Async client mirrors all sync behaviours.
"""
from __future__ import annotations

from uuid import UUID

import httpx
import pytest
import respx

from cplugin_webapi_sdk import (
    CPluginWebApiClient,
    CPluginWebApiAsyncClient,
    ApiError,
)
from tests.conftest import (
    API,
    AUTH,
    envelope_ok,
    envelope_err,
    token_body,
)

# * Trade platform UUID used across all tests.
TP = "57e1d286-0000-0000-0000-000000000001"
TP_UUID = UUID(TP)

# * Convenience: discovery + token endpoint URLs derived from AUTH constant.
DISCOVERY = f"{AUTH}/.well-known/openid-configuration"
TOKEN_EP = f"{AUTH}/connect/token"


def _oidc_doc() -> dict:
    return {"issuer": AUTH, "token_endpoint": TOKEN_EP}


def _mock_client(transport=None) -> CPluginWebApiClient:
    """Construct a sync client wired against the mock API/AUTH base URLs."""
    return CPluginWebApiClient(
        env="custom",
        api_base_url=API,
        authority=AUTH,
        client_id="cid",
        client_secret="csec",
        transport=transport,
    )


def _mock_async_client(transport=None) -> CPluginWebApiAsyncClient:
    """Construct an async client wired against the mock API/AUTH base URLs."""
    return CPluginWebApiAsyncClient(
        env="custom",
        api_base_url=API,
        authority=AUTH,
        client_id="cid",
        client_secret="csec",
        transport=transport,
    )


# ---------------------------------------------------------------------------
# Namespace surface
# ---------------------------------------------------------------------------

class TestNamespaces:
    """Verify namespace attributes and key method existence (no HTTP required)."""

    def test_mt4_namespace_exists(self):
        # * Instantiation with token= avoids any network call at construction.
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="t"
        )
        assert hasattr(c, "mt4")
        assert hasattr(c, "mt5")
        c.close()

    def test_mt4_methods_present(self):
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="t"
        )
        for method in (
            "get_server_time",
            "get_manager_common",
            "users_request",
            "get_user_record",
            "patch_user_record",
            "group_exists",
            "list_symbol_configs",
            "get_symbol_info",
            "trades_request",
            "raw",
        ):
            assert callable(getattr(c.mt4, method, None)), f"mt4.{method} missing"
        c.close()

    def test_mt5_methods_present(self):
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="t"
        )
        for method in (
            "get_server_time",
            "get_manager_current",
            "get_user",
            "get_group",
            "get_symbol",
            "positions_by_group",
            "raw",
        ):
            assert callable(getattr(c.mt5, method, None)), f"mt5.{method} missing"
        c.close()

    def test_list_trade_platforms_method_exists(self):
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="t"
        )
        assert callable(c.list_trade_platforms)
        c.close()

    def test_paged_method_exists(self):
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="t"
        )
        assert callable(c.paged)
        c.close()

    def test_task9_attributes_present(self):
        """Task 9 will read _api_base and _token_getter — verify they exist."""
        c = CPluginWebApiClient(
            env="custom", api_base_url=API, authority=AUTH, token="static-tok"
        )
        assert c._api_base == API
        assert callable(c._token_getter)
        assert c._token_getter() == "static-tok"
        c.close()

    def test_async_task9_attributes_present(self):
        """Async client exposes same Task 9 hooks."""
        c = CPluginWebApiAsyncClient(
            env="custom", api_base_url=API, authority=AUTH, token="static-tok"
        )
        assert c._api_base == API
        assert callable(c._token_getter)


# ---------------------------------------------------------------------------
# Sync happy-path
# ---------------------------------------------------------------------------

@respx.mock
def test_mt4_get_server_time_unwraps_data():
    """Successful response: unwrap returns the ``data`` field."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T00:00:00Z"))
    )
    c = _mock_client()
    result = c.mt4.get_server_time(TP)
    assert result == "2026-06-26T00:00:00Z"
    c.close()


@respx.mock
def test_mt4_get_server_time_accepts_uuid_object():
    """trade_platform may be passed as a uuid.UUID instance."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T12:00:00Z"))
    )
    c = _mock_client()
    result = c.mt4.get_server_time(TP_UUID)
    assert result == "2026-06-26T12:00:00Z"
    c.close()


@respx.mock
def test_mt5_get_server_time_unwraps_data():
    """MT5 namespace: successful response unwraps correctly."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT5/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T08:00:00Z"))
    )
    c = _mock_client()
    result = c.mt5.get_server_time(TP)
    assert result == "2026-06-26T08:00:00Z"
    c.close()


# ---------------------------------------------------------------------------
# Error envelope → ApiError
# ---------------------------------------------------------------------------

@respx.mock
def test_mt4_error_envelope_raises_apierror():
    """Error envelope: ApiError is raised with correct code and activity_id."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_err("Forbidden", "no access"))
    )
    c = _mock_client()
    with pytest.raises(ApiError) as exc_info:
        c.mt4.get_server_time(TP)
    err = exc_info.value
    assert err.code == "Forbidden"
    assert err.activity_id == "trace-1"
    c.close()


@respx.mock
def test_mt4_error_message_propagated():
    """ApiError.message carries the server-provided human-readable description."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_err("NotFound", "platform gone"))
    )
    c = _mock_client()
    with pytest.raises(ApiError) as exc_info:
        c.mt4.get_server_time(TP)
    # * ApiError exposes the human-readable text as .description (mirrors TS SDK)
    assert exc_info.value.description == "platform gone"
    c.close()


# ---------------------------------------------------------------------------
# list_trade_platforms — v1 raw array
# ---------------------------------------------------------------------------

@respx.mock
def test_list_trade_platforms_returns_list():
    """list_trade_platforms returns a plain Python list (no envelope unwrap)."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/TradePlatforms").mock(
        return_value=httpx.Response(
            200, json=[{"id": TP, "name": "Demo MT4", "type": 0}]
        )
    )
    c = _mock_client()
    platforms = c.list_trade_platforms()
    assert isinstance(platforms, list)
    assert platforms[0]["id"] == TP
    c.close()


@respx.mock
def test_list_trade_platforms_raises_on_http_error():
    """list_trade_platforms propagates HTTP errors via raise_for_status."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/TradePlatforms").mock(
        return_value=httpx.Response(503, text="unavailable")
    )
    c = _mock_client()
    with pytest.raises(httpx.HTTPStatusError):
        c.list_trade_platforms()
    c.close()


# ---------------------------------------------------------------------------
# C-1: get_symbol_info passes symbol query param
# ---------------------------------------------------------------------------

@respx.mock
def test_get_symbol_info_sends_symbol_query_param():
    """C-1: passing symbol= must put it in the request query string."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    # * Use a pattern that captures the query parameter so we can assert on it.
    route = respx.get(f"{API}/api/v2/MT4/{TP}/SymbolInfoGet").mock(
        return_value=httpx.Response(200, json=envelope_ok({"symbol": "EURUSD", "bid": 1.1}))
    )
    c = _mock_client()
    result = c.mt4.get_symbol_info(TP, symbol="EURUSD")
    assert result["symbol"] == "EURUSD"
    # * Verify the outbound request actually carried the symbol query param.
    sent_url = str(route.calls.last.request.url)
    assert "symbol=EURUSD" in sent_url, f"Expected symbol=EURUSD in URL, got: {sent_url}"
    c.close()


@respx.mock
def test_get_symbol_info_omits_symbol_when_not_given():
    """Without symbol=, the query param must be absent (returns the whole list)."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    route = respx.get(f"{API}/api/v2/MT4/{TP}/SymbolInfoGet").mock(
        return_value=httpx.Response(200, json=envelope_ok([{"symbol": "EURUSD"}, {"symbol": "GBPUSD"}]))
    )
    c = _mock_client()
    result = c.mt4.get_symbol_info(TP)
    assert isinstance(result, list)
    sent_url = str(route.calls.last.request.url)
    assert "symbol" not in sent_url, f"symbol param must not be present when omitted, got: {sent_url}"
    c.close()


# ---------------------------------------------------------------------------
# paged() seam
# ---------------------------------------------------------------------------

@respx.mock
def test_paged_iterates_until_has_more_false():
    """paged() yields data from each page and stops when has_more is False."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))

    page1 = {
        "data": [{"login": 1}],
        "error": None,
        "meta": {
            "activityId": "a1",
            "paging": {"nextCursor": "cur-2", "hasMore": True},
        },
    }
    page2 = {
        "data": [{"login": 2}],
        "error": None,
        "meta": {
            "activityId": "a2",
            "paging": {"nextCursor": None, "hasMore": False},
        },
    }

    _pages = iter([page1, page2])
    respx.get(f"{API}/api/v2/MT4/{TP}/UsersRequest").mock(
        side_effect=lambda _r: httpx.Response(200, json=next(_pages))
    )

    c = _mock_client()
    collected = []
    for page in c.paged(lambda cur: c.mt4.users_request(TP, cursor=cur)):
        collected.extend(page)
    assert collected == [{"login": 1}, {"login": 2}]
    c.close()


# ---------------------------------------------------------------------------
# Context manager
# ---------------------------------------------------------------------------

@respx.mock
def test_sync_context_manager():
    """with CPluginWebApiClient(...) as c: syntax works."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T00:00:00Z"))
    )
    with _mock_client() as c:
        result = c.mt4.get_server_time(TP)
    assert result == "2026-06-26T00:00:00Z"


# ---------------------------------------------------------------------------
# 401 → forced refresh + retry (ClientCredentialsAuth behaviour)
# ---------------------------------------------------------------------------

@respx.mock
def test_401_forces_refresh_and_retries():
    """A 401 response causes one forced token refresh; the retried request succeeds."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    # * Two token calls expected: initial fetch + forced refresh on 401.
    tok_route = respx.post(TOKEN_EP).mock(
        return_value=httpx.Response(200, json=token_body())
    )
    _responses = iter([
        httpx.Response(401, json={"error": "invalid_token"}),
        httpx.Response(200, json=envelope_ok("refreshed")),
    ])
    api_route = respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        side_effect=lambda _r: next(_responses)
    )
    c = _mock_client()
    result = c.mt4.get_server_time(TP)
    assert result == "refreshed"
    # * Two token fetches (initial + forced refresh on 401).
    assert tok_route.call_count == 2
    # * Two API calls (failed 401 + successful retry).
    assert api_route.call_count == 2
    c.close()


# ---------------------------------------------------------------------------
# Async client mirrors
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
@respx.mock
async def test_async_mt4_get_server_time():
    """Async client: successful response unwraps the data field."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T00:00:00Z"))
    )
    async with _mock_async_client() as c:
        result = await c.mt4.get_server_time(TP)
    assert result == "2026-06-26T00:00:00Z"


@pytest.mark.asyncio
@respx.mock
async def test_async_mt5_get_server_time():
    """Async MT5 namespace: successful response unwraps correctly."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT5/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("2026-06-26T09:00:00Z"))
    )
    async with _mock_async_client() as c:
        result = await c.mt5.get_server_time(TP)
    assert result == "2026-06-26T09:00:00Z"


@pytest.mark.asyncio
@respx.mock
async def test_async_error_envelope_raises_apierror():
    """Async client: error envelope raises ApiError."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_err("Unauthorized", "token expired"))
    )
    async with _mock_async_client() as c:
        with pytest.raises(ApiError) as exc_info:
            await c.mt4.get_server_time(TP)
    assert exc_info.value.code == "Unauthorized"
    assert exc_info.value.description == "token expired"


@pytest.mark.asyncio
@respx.mock
async def test_async_list_trade_platforms():
    """Async list_trade_platforms returns plain list."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/TradePlatforms").mock(
        return_value=httpx.Response(200, json=[{"id": TP, "name": "MT5-demo"}])
    )
    async with _mock_async_client() as c:
        platforms = await c.list_trade_platforms()
    assert platforms[0]["id"] == TP


@pytest.mark.asyncio
@respx.mock
async def test_async_paged_iterates():
    """Async paged() iterator yields all pages."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))

    page1 = {
        "data": [{"login": 10}],
        "error": None,
        "meta": {"activityId": "a1", "paging": {"nextCursor": "c2", "hasMore": True}},
    }
    page2 = {
        "data": [{"login": 20}],
        "error": None,
        "meta": {"activityId": "a2", "paging": {"nextCursor": None, "hasMore": False}},
    }
    _pages = iter([page1, page2])
    respx.get(f"{API}/api/v2/MT4/{TP}/UsersRequest").mock(
        side_effect=lambda _r: httpx.Response(200, json=next(_pages))
    )

    async with _mock_async_client() as c:
        collected = []
        async for page_data in c.paged(
            lambda cur: c.mt4.users_request(TP, cursor=cur)
        ):
            collected.extend(page_data)

    assert collected == [{"login": 10}, {"login": 20}]


# ---------------------------------------------------------------------------
# Brief-specified variants: explicit aclose() + flattened paged() items
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
@respx.mock
async def test_async_get_server_time_with_explicit_aclose():
    """Async client: explicit aclose() (not async-with) properly cleans up."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    respx.get(f"{API}/api/v2/MT4/{TP}/ServerTime").mock(
        return_value=httpx.Response(200, json=envelope_ok("T"))
    )
    c = _mock_async_client()
    result = await c.mt4.get_server_time(TP)
    assert result == "T"
    await c.aclose()


@respx.mock
def test_paged_walks_users_request_flattened():
    """paged() yields the data list per page; extend() produces the full item sequence."""
    respx.get(DISCOVERY).mock(return_value=httpx.Response(200, json=_oidc_doc()))
    respx.post(TOKEN_EP).mock(return_value=httpx.Response(200, json=token_body()))
    _pages = iter([
        httpx.Response(200, json={
            "data": [1, 2], "error": None,
            "meta": {"activityId": None, "paging": {"nextCursor": "c2", "hasMore": True}},
        }),
        httpx.Response(200, json={
            "data": [3], "error": None,
            "meta": {"activityId": None, "paging": {"nextCursor": None, "hasMore": False}},
        }),
    ])
    respx.get(f"{API}/api/v2/MT4/{TP}/UsersRequest").mock(
        side_effect=lambda _r: next(_pages)
    )
    c = _mock_client()
    collected: list = []
    for page in c.paged(lambda cur: c.mt4.users_request(TP, cursor=cur)):
        collected.extend(page)
    assert collected == [1, 2, 3]
    c.close()
