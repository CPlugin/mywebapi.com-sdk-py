"""Gated end-to-end test against STAGING.

Skipped unless WEBAPI_E2E=1 and credentials are present. REST checks only;
the optional SignalR smoke (Task 9) is appended below and gated on signalrcore.

Run:
    WEBAPI_E2E=1 WEBAPI_CLIENT_ID=... WEBAPI_CLIENT_SECRET=... \\
        WEBAPI_TRADE_PLATFORM=... python -m pytest e2e -q
"""
from __future__ import annotations

import os

import pytest

from cplugin_webapi_sdk import CPluginWebApiClient, ApiError

# * Skip the entire module when the gating env vars are absent.
# * This keeps the hermetic suite output clean — e2e tests never fail due to
# * missing credentials; they simply do not run.
pytestmark = pytest.mark.skipif(
    os.environ.get("WEBAPI_E2E") != "1"
    or not os.environ.get("WEBAPI_CLIENT_ID")
    or not os.environ.get("WEBAPI_CLIENT_SECRET"),
    reason="set WEBAPI_E2E=1 and WEBAPI_CLIENT_ID/SECRET to run E2E against staging",
)


def _client() -> CPluginWebApiClient:
    # * Always targets staging — no production data is touched in e2e runs.
    return CPluginWebApiClient(
        env="staging",
        client_id=os.environ["WEBAPI_CLIENT_ID"],
        client_secret=os.environ["WEBAPI_CLIENT_SECRET"],
    )


def test_list_trade_platforms_live() -> None:
    """Verify that the OAuth2 handshake succeeds and the platform list returns."""
    with _client() as c:
        platforms = c.list_trade_platforms()
        assert isinstance(platforms, list), "Expected a list of platforms"


def test_mt4_server_time_live() -> None:
    """Verify a round-trip v2 MT4 REST call against the staging server."""
    tp = os.environ.get("WEBAPI_TRADE_PLATFORM", "")
    if not tp:
        pytest.skip("set WEBAPI_TRADE_PLATFORM to a valid staging platform ID")

    with _client() as c:
        try:
            t = c.mt4.get_server_time(tp)
        except ApiError as e:
            pytest.fail(
                f"API error [{e.code}]: {e.description} (activity {e.activity_id})"
            )
        assert isinstance(t, str) and t, "Expected a non-empty ISO timestamp string"


# ---------------------------------------------------------------------------
# SignalR smoke — double-gated: WEBAPI_E2E=1 (module gate above) + signalrcore
# ---------------------------------------------------------------------------


def _has_signalr() -> bool:
    """Return True if signalrcore is importable (the [signalr] extra is installed)."""
    try:
        import signalrcore  # noqa: F401
        return True
    except ImportError:
        return False


@pytest.mark.skipif(not _has_signalr(), reason="signalrcore not installed — install with: pip install 'mywebapi-sdk[signalr]'")
def test_mt4_realtime_connect_live() -> None:
    """Open a WebSocket connection to the MT4 v2 hub and verify it stays open.

    ! EXPERIMENTAL — requires signalrcore and a live staging server.

    Only asserts that the connect/disconnect cycle completes without raising an
    exception. Does not assert on received events (hub may or may not broadcast
    within the settle window).
    """
    tp = os.environ.get("WEBAPI_TRADE_PLATFORM", "")
    if not tp:
        pytest.skip("set WEBAPI_TRADE_PLATFORM to a valid staging platform ID")

    with _client() as c:
        rt = c.realtime.mt4(tp)
        statuses: list = []
        rt.on_connection_status(lambda *args: statuses.append(args))

        rt.start()
        try:
            # * A short settle window — we only assert the socket opened without error.
            import time
            time.sleep(2)
        finally:
            rt.stop()
