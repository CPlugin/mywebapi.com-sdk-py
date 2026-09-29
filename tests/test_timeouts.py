"""Request timeouts: X-Request-Timeout, validation, HTTP timeout stretching, outcome parsing.

Server contract: a trade-platform call answers within its deadline (trade 5 s, read
10 s, change 15 s, history 30 s, maintenance 60 s, or the caller's X-Request-Timeout of
1–300 s). A miss is a v2 error — Timeout (read, safe), OutcomeUnknown (write, may still
be applied) or Busy (not sent, safe) — with an X-Request-Outcome header.
"""
from __future__ import annotations

import math

import httpx
import pytest
import respx

from cplugin_webapi_sdk import (
    ApiError,
    CPluginWebApiAsyncClient,
    CPluginWebApiClient,
    ErrorCode,
    RequestOutcome,
    is_outcome_unknown,
    is_safe_to_retry,
    unwrap,
)
from cplugin_webapi_sdk._generated.api.mt4_v_2_common import (
    get_api_v_2_mt4_trade_platform_server_time as server_time_op,
)
from cplugin_webapi_sdk.timeouts import (
    DEFAULT_TRANSPORT_TIMEOUT,
    TRANSPORT_TIMEOUT_MARGIN,
    UNDOCUMENTED_OPERATION_TIMEOUT,
    format_seconds,
    operation_default_timeout,
    validate_idempotency_key,
    validate_request_timeout,
)
from tests.conftest import API, AUTH, envelope_err, envelope_ok

TP = "57e1d286-0000-0000-0000-000000000001"
MT4_TIME = f"{API}/api/v2/MT4/{TP}/ServerTime"
MT5_TIME = f"{API}/api/v2/MT5/{TP}/ServerTime"
MT4_PATCH = f"{API}/api/v2/MT4/{TP}/UserRecord/1001"


def _client(**kw) -> CPluginWebApiClient:
    return CPluginWebApiClient(env="custom", api_base_url=API, authority=AUTH, token="t", **kw)


def _async_client(**kw) -> CPluginWebApiAsyncClient:
    return CPluginWebApiAsyncClient(env="custom", api_base_url=API, authority=AUTH, token="t", **kw)


def _read_timeout(request: httpx.Request) -> float | None:
    # * httpx records the effective per-request timeout in the request extensions.
    return request.extensions["timeout"]["read"]


# ---------------------------------------------------------------------------
# X-Request-Timeout header
# ---------------------------------------------------------------------------

@respx.mock
def test_no_request_timeout_sends_no_header():
    """Without a timeout the server applies its own per-operation default."""
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client() as c:
        c.mt4.get_server_time(TP)
    request = route.calls.last.request
    assert "x-request-timeout" not in request.headers
    # * ServerTime is a read: 10 s server default + margin, above the 30 s floor.
    assert _read_timeout(request) == 10 + TRANSPORT_TIMEOUT_MARGIN


@respx.mock
def test_per_call_request_timeout_sends_header():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client() as c:
        c.mt4.get_server_time(TP, request_timeout=2.5)
    assert route.calls.last.request.headers["X-Request-Timeout"] == "2.5"


@respx.mock
def test_client_default_request_timeout_applies_to_every_call():
    route = respx.get(MT5_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(request_timeout=20) as c:
        c.mt5.get_server_time(TP)
    assert route.calls.last.request.headers["X-Request-Timeout"] == "20"


@respx.mock
def test_per_call_request_timeout_overrides_client_default():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(request_timeout=20) as c:
        c.mt4.get_server_time(TP, request_timeout=3)
    assert route.calls.last.request.headers["X-Request-Timeout"] == "3"


@respx.mock
def test_raw_accepts_request_timeout():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client() as c:
        resp = c.mt4.raw(server_time_op, trade_platform=TP, request_timeout=7)
    assert route.calls.last.request.headers["X-Request-Timeout"] == "7"
    assert unwrap(resp) == "t"


@respx.mock
def test_raw_accepts_generated_parameter_name():
    """x_request_timeout (the generated name) works like request_timeout."""
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client() as c:
        c.mt4.raw(server_time_op, trade_platform=TP, x_request_timeout=12)
    request = route.calls.last.request
    assert request.headers["X-Request-Timeout"] == "12"
    assert _read_timeout(request) == 12 + TRANSPORT_TIMEOUT_MARGIN


def test_raw_rejects_disagreeing_timeouts():
    with _client() as c, pytest.raises(ValueError, match="disagree"):
        c.mt4.raw(server_time_op, trade_platform=TP, request_timeout=5, x_request_timeout=6)


def test_generated_layer_does_not_pin_a_default():
    """The generator must not bake the documented default into the call (it would always be sent)."""
    kwargs = server_time_op._get_kwargs(trade_platform=TP)
    assert "X-Request-Timeout" not in kwargs.get("headers", {})


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("value", [0, 0.5, 300.01, 301, -1, math.nan, math.inf])
def test_out_of_range_request_timeout_rejected_before_sending(value):
    with respx.mock(assert_all_called=False) as mock:
        route = mock.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
        with _client() as c, pytest.raises(ValueError, match="from 1 to 300"):
            c.mt4.get_server_time(TP, request_timeout=value)
        assert not route.called


@pytest.mark.parametrize("value", [True, "10", b"10"])
def test_non_numeric_request_timeout_rejected(value):
    with pytest.raises(TypeError):
        validate_request_timeout(value)


@pytest.mark.parametrize("value", [1, 1.0, 150, 300])
def test_bounds_are_inclusive(value):
    assert validate_request_timeout(value) == float(value)


def test_invalid_client_default_fails_at_construction():
    with pytest.raises(ValueError):
        _client(request_timeout=0)


@pytest.mark.parametrize("seconds, text", [(10.0, "10"), (2.5, "2.5"), (1.2345, "1.234"), (300, "300")])
def test_seconds_formatted_like_the_server(seconds, text):
    assert format_seconds(seconds) == text


@pytest.mark.parametrize("key", ["", "   ", "x" * 256, "ключ", "a\nb"])
def test_bad_idempotency_key_rejected(key):
    with pytest.raises(ValueError):
        validate_idempotency_key(key)


# ---------------------------------------------------------------------------
# HTTP timeout stretching
# ---------------------------------------------------------------------------

@respx.mock
def test_http_timeout_outlasts_the_server_deadline():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(timeout=10) as c:
        c.mt4.get_server_time(TP, request_timeout=120)
    assert _read_timeout(route.calls.last.request) == 120 + TRANSPORT_TIMEOUT_MARGIN


@respx.mock
def test_http_timeout_never_shortened():
    """A longer client timeout than request_timeout + margin is kept."""
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(timeout=200) as c:
        c.mt4.get_server_time(TP, request_timeout=5)
    assert _read_timeout(route.calls.last.request) == 200


@respx.mock
def test_no_http_timeout_stays_unlimited():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(timeout=None) as c:
        c.mt4.get_server_time(TP, request_timeout=5)
    assert _read_timeout(route.calls.last.request) is None


def test_margin_covers_the_server_connect_allowance():
    """The server may add up to 20 s for opening the platform connection; the client must wait longer."""
    assert TRANSPORT_TIMEOUT_MARGIN > 20
    assert DEFAULT_TRANSPORT_TIMEOUT == 30


def test_operation_defaults_come_from_the_spec():
    from cplugin_webapi_sdk._generated.api.mt4_v_2_users import (
        patch_api_v_2_mt4_trade_platform_user_record_login as patch_op,
    )
    from cplugin_webapi_sdk._generated.api.mt4_v_2_sidecar_batch_reads import (
        get_api_v_2_mt4_trade_platform_users_snapshot as snapshot_op,
    )
    assert operation_default_timeout(server_time_op) == 10
    assert operation_default_timeout(patch_op) == 15
    # * Sidecar operations document no default: assume the longest server default.
    assert operation_default_timeout(snapshot_op) == UNDOCUMENTED_OPERATION_TIMEOUT == 60
    assert operation_default_timeout(object()) == UNDOCUMENTED_OPERATION_TIMEOUT


def test_every_documented_default_is_mapped():
    """The generated table covers every operation whose spec documents a timeout."""
    import json
    from pathlib import Path

    from cplugin_webapi_sdk._generated.operation_timeouts import DEFAULTS

    spec = json.loads((Path(__file__).parents[1] / "src/cplugin_webapi_sdk/spec/v2.json").read_text("utf-8"))
    documented = sorted(
        p["schema"]["default"]
        for item in spec["paths"].values()
        for op in item.values()
        for p in op.get("parameters", [])
        if p.get("name") == "X-Request-Timeout" and "default" in p.get("schema", {})
    )
    assert sorted(DEFAULTS.values()) == documented


@respx.mock
def test_default_deadline_of_a_write_sets_the_http_timeout():
    route = respx.patch(MT4_PATCH).mock(return_value=httpx.Response(200, json=envelope_ok({})))
    with _client() as c:
        c.mt4.patch_user_record(TP, 1001, {"leverage": 200})
    assert _read_timeout(route.calls.last.request) == 15 + TRANSPORT_TIMEOUT_MARGIN


@respx.mock
def test_patch_user_record_sends_only_the_changed_fields():
    import json

    route = respx.patch(MT4_PATCH).mock(return_value=httpx.Response(200, json=envelope_ok({"login": 1001})))
    with _client() as c:
        assert c.mt4.patch_user_record(TP, 1001, {"leverage": 200, "comment": "vip"}) == {"login": 1001}
    request = route.calls.last.request
    assert json.loads(request.content) == {"leverage": 200, "comment": "vip"}
    assert request.headers["Content-Type"] == "application/json"


@pytest.mark.parametrize("changes, exc", [({}, ValueError), ([("leverage", 1)], TypeError)])
def test_patch_user_record_rejects_empty_or_non_mapping(changes, exc):
    with _client() as c, pytest.raises(exc):
        c.mt4.patch_user_record(TP, 1001, changes)


@respx.mock
def test_undocumented_operation_waits_for_the_longest_default():
    from cplugin_webapi_sdk._generated.api.mt4_v_2_sidecar_batch_reads import (
        get_api_v_2_mt4_trade_platform_users_snapshot as snapshot_op,
    )
    route = respx.get(f"{API}/api/v2/MT4/{TP}/UsersSnapshot").mock(
        return_value=httpx.Response(200, json=envelope_ok([]))
    )
    with _client() as c:
        c.mt4.raw(snapshot_op, trade_platform=TP)
    assert _read_timeout(route.calls.last.request) == 60 + TRANSPORT_TIMEOUT_MARGIN


@respx.mock
def test_configured_timeout_is_the_floor_for_default_deadlines():
    route = respx.get(MT4_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    with _client(timeout=100) as c:
        c.mt4.get_server_time(TP)
    assert _read_timeout(route.calls.last.request) == 100


# ---------------------------------------------------------------------------
# Outcome parsing
# ---------------------------------------------------------------------------

def _timed_out(code: str, outcome: str | None, applied: str | None = "5") -> httpx.Response:
    headers = {}
    if outcome is not None:
        headers["X-Request-Outcome"] = outcome
    if applied is not None:
        headers["X-Request-Timeout-Applied"] = applied
    return httpx.Response(200, json=envelope_err(code, "did not finish"), headers=headers)


@respx.mock
def test_read_timeout_is_safe_to_retry():
    respx.get(MT4_TIME).mock(return_value=_timed_out("Timeout", "timeout", "10"))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.get_server_time(TP)
    err = ei.value
    assert err.code == ErrorCode.TIMEOUT
    assert err.outcome == RequestOutcome.TIMEOUT
    assert err.applied_timeout == 10.0
    assert err.safe_to_retry and is_safe_to_retry(err)
    assert not err.outcome_unknown and not is_outcome_unknown(err)


@respx.mock
def test_write_outcome_unknown_is_not_safe_to_retry():
    respx.patch(MT4_PATCH).mock(return_value=_timed_out("OutcomeUnknown", "unknown", "15"))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.patch_user_record(TP, 1001, {"leverage": 200})
    err = ei.value
    assert err.code == ErrorCode.OUTCOME_UNKNOWN
    assert err.outcome == RequestOutcome.UNKNOWN
    assert is_outcome_unknown(err)
    assert not is_safe_to_retry(err)


@respx.mock
def test_in_progress_idempotent_repeat_is_outcome_unknown():
    route = respx.patch(MT4_PATCH).mock(return_value=_timed_out("OutcomeUnknown", "in-progress", None))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.patch_user_record(TP, 1001, {"leverage": 200}, idempotency_key="order-42")
    assert route.calls.last.request.headers["Idempotency-Key"] == "order-42"
    assert ei.value.outcome == RequestOutcome.IN_PROGRESS
    assert ei.value.applied_timeout is None
    assert is_outcome_unknown(ei.value) and not is_safe_to_retry(ei.value)


@respx.mock
def test_busy_is_safe_to_retry():
    respx.get(MT4_TIME).mock(return_value=_timed_out("Busy", "not-started"))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.get_server_time(TP)
    assert ei.value.outcome == RequestOutcome.NOT_STARTED
    assert is_safe_to_retry(ei.value)


@respx.mock
def test_outcome_header_alone_classifies():
    """A proxy or a future server may omit one signal; either one is enough."""
    respx.get(MT4_TIME).mock(return_value=_timed_out("Internal", "Unknown"))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.get_server_time(TP)
    assert ei.value.outcome == "unknown"
    assert is_outcome_unknown(ei.value)


@respx.mock
def test_other_errors_are_neither():
    respx.get(MT4_TIME).mock(return_value=_timed_out("Validation", None, None))
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.get_server_time(TP, request_timeout=5)
    assert ei.value.outcome is None
    assert not is_safe_to_retry(ei.value) and not is_outcome_unknown(ei.value)


def test_non_api_errors_are_neither():
    exc = httpx.ReadTimeout("slow")
    assert not is_safe_to_retry(exc) and not is_outcome_unknown(exc)


@respx.mock
def test_unparseable_gateway_page_keeps_headers():
    respx.get(MT4_TIME).mock(
        return_value=httpx.Response(504, text="<html>gateway</html>", headers={"X-Request-Outcome": "unknown"})
    )
    with _client() as c, pytest.raises(ApiError) as ei:
        c.mt4.get_server_time(TP)
    assert ei.value.code == ErrorCode.INVALID_RESPONSE
    assert is_outcome_unknown(ei.value)


# ---------------------------------------------------------------------------
# No automatic retry of a sent request
# ---------------------------------------------------------------------------

@respx.mock
def test_outcome_unknown_write_is_sent_once():
    route = respx.patch(MT4_PATCH).mock(return_value=_timed_out("OutcomeUnknown", "unknown"))
    with _client() as c, pytest.raises(ApiError):
        c.mt4.patch_user_record(TP, 1001, {"leverage": 200})
    assert route.call_count == 1


@respx.mock
def test_read_timeout_is_not_retried_by_the_sdk():
    route = respx.get(MT4_TIME).mock(side_effect=httpx.ReadTimeout("slow"))
    with _client() as c, pytest.raises(httpx.ReadTimeout):
        c.mt4.get_server_time(TP)
    assert route.call_count == 1


# ---------------------------------------------------------------------------
# Async mirror
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
@respx.mock
async def test_async_request_timeout_and_outcome():
    route = respx.get(MT4_TIME).mock(return_value=_timed_out("Timeout", "timeout", "4"))
    async with _async_client(request_timeout=8) as c:
        with pytest.raises(ApiError) as ei:
            await c.mt4.get_server_time(TP, request_timeout=4)
    request = route.calls.last.request
    assert request.headers["X-Request-Timeout"] == "4"
    assert _read_timeout(request) == 4 + TRANSPORT_TIMEOUT_MARGIN
    assert ei.value.applied_timeout == 4.0 and is_safe_to_retry(ei.value)


@pytest.mark.asyncio
@respx.mock
async def test_async_raw_with_idempotency_key():
    route = respx.get(MT5_TIME).mock(return_value=httpx.Response(200, json=envelope_ok("t")))
    from cplugin_webapi_sdk._generated.api.mt5_v_2_common import (
        get_api_v_2_mt5_trade_platform_server_time as mt5_time_op,
    )
    async with _async_client() as c:
        resp = await c.mt5.raw(mt5_time_op, trade_platform=TP, request_timeout=9, idempotency_key="k-1")
    request = route.calls.last.request
    assert request.headers["X-Request-Timeout"] == "9"
    assert request.headers["Idempotency-Key"] == "k-1"
    assert unwrap(resp) == "t"
