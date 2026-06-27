"""Smoke tests for the generated client tree.

Verifies that the generated package imports cleanly and that the server_time
endpoint builds a well-formed request kwargs dict — no network required.
"""
from __future__ import annotations

import uuid
import pytest

# * These imports will fail fast if codegen produced broken output or the
#   package tree is missing — that's the intended signal.
from cplugin_webapi_sdk._generated import AuthenticatedClient, Client
from cplugin_webapi_sdk._generated.api.mt4_v_2_common import (
    get_api_v_2_mt4_trade_platform_server_time as mt4_server_time,
)
from cplugin_webapi_sdk._generated.api.mt5_v_2_common import (
    get_api_v_2_mt5_trade_platform_server_time as mt5_server_time,
)


class TestGeneratedImports:
    """Package-level smoke: all key symbols importable."""

    def test_client_class_importable(self) -> None:
        assert Client is not None

    def test_authenticated_client_class_importable(self) -> None:
        assert AuthenticatedClient is not None

    def test_mt4_server_time_module_importable(self) -> None:
        assert mt4_server_time is not None

    def test_mt5_server_time_module_importable(self) -> None:
        assert mt5_server_time is not None


class TestMt4ServerTimeKwargs:
    """Verifies MT4 server_time endpoint builds correct request kwargs."""

    def test_method_is_get(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt4_server_time._get_kwargs(trade_platform=platform_id)
        assert kwargs["method"] == "get"

    def test_url_contains_trade_platform(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt4_server_time._get_kwargs(trade_platform=platform_id)
        assert str(platform_id) in kwargs["url"]

    def test_url_contains_server_time_segment(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt4_server_time._get_kwargs(trade_platform=platform_id)
        assert "ServerTime" in kwargs["url"]

    def test_url_contains_v2_path(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt4_server_time._get_kwargs(trade_platform=platform_id)
        assert "/api/v2/" in kwargs["url"]


class TestMt5ServerTimeKwargs:
    """Verifies MT5 server_time endpoint builds correct request kwargs."""

    def test_method_is_get(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt5_server_time._get_kwargs(trade_platform=platform_id)
        assert kwargs["method"] == "get"

    def test_url_contains_trade_platform(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt5_server_time._get_kwargs(trade_platform=platform_id)
        assert str(platform_id) in kwargs["url"]

    def test_url_contains_server_time_segment(self) -> None:
        platform_id = uuid.uuid4()
        kwargs = mt5_server_time._get_kwargs(trade_platform=platform_id)
        assert "ServerTime" in kwargs["url"]
