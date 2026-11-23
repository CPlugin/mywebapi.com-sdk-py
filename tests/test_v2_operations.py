"""Extended v2 Manager API surface — the operation groups added to the manual layer.

Covers the dealer/reports summaries, subscriptions, user certificates, trade
requests, market data and insight, configuration, communications and clients
groups that reached the v2 contract with the Manager API parity work.

Tests are respx-mocked — no live server required. They verify the route and verb
each facade method builds, that optional filters are omitted when unset, that
mapping bodies become the generated request models, and that envelopes unwrap.
"""
from __future__ import annotations

import json

import httpx
import pytest
import respx

from cplugin_webapi_sdk import (
    CPluginWebApiAsyncClient,
    CPluginWebApiClient,
)
from tests.conftest import API, AUTH, envelope_ok

TP = "57e1d286-0000-0000-0000-000000000001"


def _client() -> CPluginWebApiClient:
    return CPluginWebApiClient(env="custom", api_base_url=API, authority=AUTH, token="t")


def _async_client() -> CPluginWebApiAsyncClient:
    return CPluginWebApiAsyncClient(env="custom", api_base_url=API, authority=AUTH, token="t")


MT4_SUMMARY_ALL = f"{API}/api/v2/MT4/{TP}/SummaryGetAll"
MT5_SUMMARY_ALL = f"{API}/api/v2/MT5/{TP}/SummaryGetAll"
MT5_CFG_REQUEST = f"{API}/api/v2/MT5/{TP}/SubscriptionCfgRequest/Gold"
MT5_CERT = f"{API}/api/v2/MT5/{TP}/UserCertGet/1001"
MT5_REQUEST_ALL = f"{API}/api/v2/MT5/{TP}/RequestGetAll"
MT5_ORDER_ADD = f"{API}/api/v2/MT5/{TP}/OrderAdd"
MT5_MAIL_SEND = f"{API}/api/v2/MT5/{TP}/MailSend"
MT5_TICK_LAST = f"{API}/api/v2/MT5/{TP}/TickLast/EURUSD"


# ---------------------------------------------------------------------------
# Surface
# ---------------------------------------------------------------------------

NEW_MT4_METHODS = [
    "summary_get_all",
    "summary_get",
    "summary_currency",
    "exposure_get",
    "exposure_value",
    "trade_calc_profit",
]

NEW_MT5_METHODS = [
    "time_get",
    "summary_get_all",
    "summary_get",
    "summary_currency",
    "exposure_get_all",
    "exposure_get",
    "daily_request",
    "daily_request_light",
    "subscription_cfg_request",
    "subscription_cfg_get",
    "subscription_request",
    "subscription_history_request",
    "user_cert_get",
    "user_account_get",
    "user_get_by_logins",
    "user_group",
    "user_logins",
    "user_cert_confirm",
    "request_get_all",
    "request_get",
    "trade_profit",
    "order_get",
    "order_add",
    "order_cancel",
    "deal_request",
    "history_request",
    "tick_last",
    "tick_stat",
    "book_get",
    "online_request",
    "symbol_request",
    "symbol_exist",
    "leverage_get",
    "mail_request",
    "news_request",
    "setting_get",
    "mail_send",
    "client_user_request",
    "document_request",
    "client_update",
]


def test_mt4_namespace_has_new_group_methods():
    with _client() as c:
        missing = [n for n in NEW_MT4_METHODS if not callable(getattr(c.mt4, n, None))]
    assert not missing, f"MT4 facade misses {missing}"


def test_mt5_namespace_has_new_group_methods():
    with _client() as c:
        missing = [n for n in NEW_MT5_METHODS if not callable(getattr(c.mt5, n, None))]
    assert not missing, f"MT5 facade misses {missing}"


def test_async_namespaces_have_new_group_methods():
    c = _async_client()
    missing = [n for n in NEW_MT5_METHODS if not callable(getattr(c.mt5, n, None))]
    missing += [n for n in NEW_MT4_METHODS if not callable(getattr(c.mt4, n, None))]
    assert not missing, f"async facade misses {missing}"


# ---------------------------------------------------------------------------
# Routes and verbs
# ---------------------------------------------------------------------------

@respx.mock
def test_mt4_summary_get_all_route():
    route = respx.get(MT4_SUMMARY_ALL).mock(return_value=httpx.Response(200, json=envelope_ok([])))
    with _client() as c:
        assert c.mt4.summary_get_all(TP) == []
    assert route.calls.last.request.method == "GET"


@respx.mock
def test_mt5_summary_get_all_route():
    route = respx.get(MT5_SUMMARY_ALL).mock(return_value=httpx.Response(200, json=envelope_ok([])))
    with _client() as c:
        assert c.mt5.summary_get_all(TP) == []
    assert route.calls.last.request.method == "GET"


@respx.mock
def test_mt5_subscription_cfg_request_route():
    payload = {"name": "Gold"}
    route = respx.get(MT5_CFG_REQUEST).mock(
        return_value=httpx.Response(200, json=envelope_ok(payload))
    )
    with _client() as c:
        assert c.mt5.subscription_cfg_request(TP, "Gold") == payload
    assert route.called


@respx.mock
def test_mt5_user_cert_get_route():
    route = respx.get(MT5_CERT).mock(return_value=httpx.Response(200, json=envelope_ok({"login": 1001})))
    with _client() as c:
        assert c.mt5.user_cert_get(TP, 1001) == {"login": 1001}
    assert route.called


@respx.mock
def test_mt5_tick_last_route():
    route = respx.get(MT5_TICK_LAST).mock(return_value=httpx.Response(200, json=envelope_ok(None)))
    with _client() as c:
        c.mt5.tick_last(TP, "EURUSD")
    assert route.called


@respx.mock
def test_mt5_request_get_all_omits_unset_filters():
    """Unset ``from``/``count`` are not sent at all."""
    route = respx.get(MT5_REQUEST_ALL).mock(return_value=httpx.Response(200, json=envelope_ok([])))
    with _client() as c:
        c.mt5.request_get_all(TP)
    url = route.calls.last.request.url
    assert "from=" not in str(url)
    assert "count=" not in str(url)


@respx.mock
def test_mt5_request_get_all_sends_filters_when_given():
    route = respx.get(MT5_REQUEST_ALL).mock(return_value=httpx.Response(200, json=envelope_ok([])))
    with _client() as c:
        c.mt5.request_get_all(TP, from_=10, count=5)
    url = route.calls.last.request.url
    assert url.params["from"] == "10"
    assert url.params["count"] == "5"


# ---------------------------------------------------------------------------
# Mapping bodies become generated request models
# ---------------------------------------------------------------------------

@respx.mock
def test_mt5_order_add_sends_wire_names():
    route = respx.post(MT5_ORDER_ADD).mock(return_value=httpx.Response(200, json=envelope_ok(True)))
    with _client() as c:
        assert c.mt5.order_add(TP, {"login": 1001, "symbol": "EURUSD"}) is True
    body = json.loads(route.calls.last.request.content)
    assert body["login"] == 1001
    assert body["symbol"] == "EURUSD"


@respx.mock
def test_mt5_mail_send_sends_camel_case():
    route = respx.post(MT5_MAIL_SEND).mock(return_value=httpx.Response(200, json=envelope_ok(None)))
    with _client() as c:
        c.mt5.mail_send(TP, {"to": 1001, "toName": "Alice", "subject": "Hi"})
    body = json.loads(route.calls.last.request.content)
    assert body["to"] == 1001
    assert body["toName"] == "Alice"


# ---------------------------------------------------------------------------
# Async mirror
# ---------------------------------------------------------------------------

@respx.mock
@pytest.mark.asyncio
async def test_async_mt5_user_cert_get_route():
    route = respx.get(MT5_CERT).mock(return_value=httpx.Response(200, json=envelope_ok({"login": 1001})))
    c = _async_client()
    try:
        assert await c.mt5.user_cert_get(TP, 1001) == {"login": 1001}
    finally:
        await c.aclose()
    assert route.called


@respx.mock
@pytest.mark.asyncio
async def test_async_mt4_summary_get_all_route():
    route = respx.get(MT4_SUMMARY_ALL).mock(return_value=httpx.Response(200, json=envelope_ok([])))
    c = _async_client()
    try:
        assert await c.mt4.summary_get_all(TP) == []
    finally:
        await c.aclose()
    assert route.called
