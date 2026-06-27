"""Unit tests for the optional realtime SignalR client (realtime.py).

All tests here are hermetic — they do NOT require ``signalrcore`` installed.
The ``signalrcore`` absence path is exercised via monkeypatching ``_import_signalr``.
URL-building logic is tested directly on the pure-Python ``_build_hub_url`` helper.

Live smoke tests against staging are in ``e2e/test_e2e.py`` and are double-gated
on ``WEBAPI_E2E=1`` + ``signalrcore`` importable.
"""
from __future__ import annotations

import pytest

from cplugin_webapi_sdk import realtime
from cplugin_webapi_sdk.realtime import (
    MT4RealtimeClient,
    MT5RealtimeClient,
    RealtimeNamespace,
    SignalRNotInstalledError,
    _build_hub_url,  # * internal helper, tested directly
)


# ---------------------------------------------------------------------------
# _build_hub_url — pure-Python, no dependencies
# ---------------------------------------------------------------------------


def test_build_hub_url_appends_trade_platform():
    """tradePlatform query value is URL-encoded and appended to the hub path."""
    url = _build_hub_url("https://pre.mywebapi.com", "mt4", "real real/123 abc")
    # * tradePlatform must be URL-encoded (spaces → %20, slash → %2F)
    assert url.startswith("https://pre.mywebapi.com/hubs/mt4/v2?tradePlatform=")
    assert "real%20real%2F123%20abc" in url


def test_build_hub_url_strips_trailing_slash():
    """Trailing slash on base_url is stripped before appending the hub path."""
    url = _build_hub_url("https://pre.mywebapi.com/", "mt5", "tp1")
    assert url == "https://pre.mywebapi.com/hubs/mt5/v2?tradePlatform=tp1"


def test_build_hub_url_mt4_platform_segment():
    """The platform segment is exactly 'mt4' for the MT4 hub."""
    url = _build_hub_url("https://api.example.com", "mt4", "tp-abc")
    assert "/hubs/mt4/v2" in url


def test_build_hub_url_mt5_platform_segment():
    """The platform segment is exactly 'mt5' for the MT5 hub."""
    url = _build_hub_url("https://api.example.com", "mt5", "tp-xyz")
    assert "/hubs/mt5/v2" in url


def test_build_hub_url_empty_trade_platform():
    """Empty trade_platform produces an empty query value (not a ValueError here)."""
    url = _build_hub_url("https://api.example.com", "mt4", "")
    assert url.endswith("?tradePlatform=")


# ---------------------------------------------------------------------------
# SignalRNotInstalledError — absence of signalrcore
# ---------------------------------------------------------------------------


def test_construct_without_signalrcore_raises_clear_hint(monkeypatch):
    """When signalrcore is absent, construction raises SignalRNotInstalledError
    with a message that mentions both 'signalrcore' and 'pip install'.
    """
    # * Force the lazy import to fail, simulating the extra not being installed.
    def _fake_import():
        raise ImportError("signalrcore not installed")

    monkeypatch.setattr(realtime, "_import_signalr", _fake_import)

    with pytest.raises(SignalRNotInstalledError) as ei:
        MT4RealtimeClient(
            base_url="https://pre.mywebapi.com",
            token_factory=lambda: "t",
            trade_platform="tp1",
        )

    assert "signalrcore" in str(ei.value)
    assert "pip install" in str(ei.value)


def test_mt5_construct_without_signalrcore_raises(monkeypatch):
    """MT5RealtimeClient also raises SignalRNotInstalledError when signalrcore absent."""
    monkeypatch.setattr(realtime, "_import_signalr", lambda: (_ for _ in ()).throw(ImportError()))

    with pytest.raises(SignalRNotInstalledError):
        MT5RealtimeClient(
            base_url="https://pre.mywebapi.com",
            token_factory=lambda: "tok",
            trade_platform="tp2",
        )


def test_error_message_includes_install_hint():
    """SignalRNotInstalledError message references the [signalr] extra."""
    err = SignalRNotInstalledError()
    assert "[signalr]" in str(err) or "signalr" in str(err)
    assert "pip install" in str(err)


# ---------------------------------------------------------------------------
# RealtimeNamespace — accessed as client.realtime
# ---------------------------------------------------------------------------


def test_realtime_namespace_mt4_constructs_correct_client(monkeypatch):
    """RealtimeNamespace.mt4(tp) delegates to MT4RealtimeClient with correct args."""
    created: list = []

    # * Stub out _import_signalr so no real connection is attempted.
    class _FakeBuilder:
        def with_url(self, url, options=None):
            self._url = url
            return self

        def build(self):
            class _FakeConn:
                def on(self, *a): pass
                def send(self, *a): pass
                def stream(self, *a): pass
                def start(self): pass
                def stop(self): pass
            return _FakeConn()

    monkeypatch.setattr(realtime, "_import_signalr", lambda: _FakeBuilder)

    ns = RealtimeNamespace(
        base_url="https://pre.mywebapi.com",
        token_factory=lambda: "bearer-token",
    )
    rt = ns.mt4("my-tp")

    assert isinstance(rt, MT4RealtimeClient)
    # * Hub URL must reference mt4 and the trade platform.
    assert "/hubs/mt4/v2" in rt.hub_url
    assert "my-tp" in rt.hub_url


def test_realtime_namespace_mt5_constructs_correct_client(monkeypatch):
    """RealtimeNamespace.mt5(tp) delegates to MT5RealtimeClient with correct args."""
    class _FakeBuilder:
        def with_url(self, url, options=None):
            return self
        def build(self):
            class _Conn:
                def on(self, *a): pass
                def stream(self, *a): pass
                def start(self): pass
                def stop(self): pass
            return _Conn()

    monkeypatch.setattr(realtime, "_import_signalr", lambda: _FakeBuilder)

    ns = RealtimeNamespace(
        base_url="https://cloud.mywebapi.com",
        token_factory=lambda: "tok",
    )
    rt = ns.mt5("tp-mt5")

    assert isinstance(rt, MT5RealtimeClient)
    assert "/hubs/mt5/v2" in rt.hub_url
    assert "tp-mt5" in rt.hub_url


def test_realtime_namespace_binds_token_factory(monkeypatch):
    """Token factory passed to RealtimeNamespace is forwarded to the hub client."""
    calls: list = []

    def _token():
        calls.append(1)
        return "the-token"

    class _FakeBuilder:
        _captured_opts: dict = {}

        def with_url(self, url, options=None):
            _FakeBuilder._captured_opts = options or {}
            return self

        def build(self):
            class _Conn:
                def on(self, *a): pass
                def stream(self, *a): pass
                def start(self): pass
                def stop(self): pass
            return _Conn()

    monkeypatch.setattr(realtime, "_import_signalr", lambda: _FakeBuilder)

    ns = RealtimeNamespace(base_url="https://pre.mywebapi.com", token_factory=_token)
    ns.mt4("tp1")

    # * access_token_factory must be the token callable we passed in.
    factory = _FakeBuilder._captured_opts.get("access_token_factory")
    assert callable(factory)
    result = factory()
    assert result == "the-token"


def test_empty_trade_platform_raises_value_error(monkeypatch):
    """Constructing a realtime client with an empty trade_platform raises ValueError."""
    monkeypatch.setattr(realtime, "_import_signalr", lambda: object)  # won't be called

    with pytest.raises(ValueError, match="trade_platform"):
        MT4RealtimeClient(
            base_url="https://pre.mywebapi.com",
            token_factory=lambda: "t",
            trade_platform="",
        )


# ---------------------------------------------------------------------------
# Package-level import — realtime module must be importable without signalrcore
# ---------------------------------------------------------------------------


def test_realtime_module_importable_without_signalrcore():
    """realtime.py imports cleanly even when signalrcore is not installed.

    The lazy import is deferred to construction time, so top-level import
    must not trigger ModuleNotFoundError.
    """
    # * If we reach this line the import at the top of this file succeeded.
    assert MT4RealtimeClient is not None
    assert MT5RealtimeClient is not None
    assert RealtimeNamespace is not None
    assert SignalRNotInstalledError is not None
