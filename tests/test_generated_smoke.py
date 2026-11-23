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
    get_api_v_2_mt5_trade_platform_time_server as mt5_server_time,
)
from cplugin_webapi_sdk._generated.models import (
    MT5ConSubscription,
    MT5MarketTickStat,
    MT5News,
    MT5SubscriptionAction,
    MT5SubscriptionControlMode,
    MT5SubscriptionFreePeriod,
    MT5SubscriptionPeriod,
    MT5SubscriptionStatus,
    MT5SubscriptionType,
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
        assert "TimeServer" in kwargs["url"]


class TestSubscriptionEnums:
    """Subscription enumerations travel as names; the generated models decode them."""

    def test_enums_carry_the_wire_names(self) -> None:
        assert [e.value for e in MT5SubscriptionType] == ["Folder", "Subscription"]
        assert MT5SubscriptionPeriod.MONTHLY == "Monthly"
        assert MT5SubscriptionStatus.CANCELED == "Canceled"
        assert MT5SubscriptionFreePeriod.NONE == "None"
        assert MT5SubscriptionControlMode.UNSUBSCRIBE == "Unsubscribe"
        assert MT5SubscriptionAction.CANCEL == "Cancel"
        assert str(MT5SubscriptionType.SUBSCRIPTION) == "Subscription"

    def test_configuration_decodes_named_codes_and_round_trips(self) -> None:
        payload = {
            "id": 12,
            "name": "Gold",
            "type": "Folder",
            "controlMode": "Hidden",
            "periodMode": "Monthly",
            "periodFreeMode": "None",
            "flags": "FreePeriod",
        }
        cfg = MT5ConSubscription.from_dict(payload)
        assert cfg.type_ is MT5SubscriptionType.FOLDER
        assert cfg.control_mode is MT5SubscriptionControlMode.HIDDEN
        assert cfg.period_mode is MT5SubscriptionPeriod.MONTHLY
        assert cfg.period_free_mode is MT5SubscriptionFreePeriod.NONE
        wire = cfg.to_dict()
        assert wire["type"] == "Folder"
        assert wire["controlMode"] == "Hidden"
        assert wire["periodMode"] == "Monthly"
        assert wire["periodFreeMode"] == "None"
        assert wire["flags"] == "FreePeriod"

    def test_legacy_numeric_code_passes_through(self) -> None:
        # the server still accepts the numeric code; a response never contains one
        assert MT5ConSubscription.from_dict({"type": 1}).type_ == 1


class TestOptionGreekFields:
    """Tick statistics carry the option pricing fields of the trade server."""

    def test_statistics_expose_greeks_and_sensitivity(self) -> None:
        stat = MT5MarketTickStat.from_dict(
            {
                "symbol": "EURUSD",
                "time": 1795000000,
                "priceType": 2,
                "priceGreeksDelta": 0.51,
                "priceGreeksTheta": -0.02,
                "priceGreeksGamma": 0.003,
                "priceGreeksVega": 0.11,
                "priceGreeksRho": 0.04,
                "priceGreeksOmega": 6.2,
                "priceSensitivity": 1.5,
            }
        )
        assert (stat.price_greeks_delta, stat.price_greeks_theta) == (0.51, -0.02)
        assert (stat.price_greeks_gamma, stat.price_greeks_vega) == (0.003, 0.11)
        assert (stat.price_greeks_rho, stat.price_greeks_omega) == (0.04, 6.2)
        assert stat.price_sensitivity == 1.5
        wire = stat.to_dict()
        assert wire["priceGreeksDelta"] == 0.51
        assert wire["priceSensitivity"] == 1.5

    def test_news_time_is_wall_clock_of_the_trade_server(self) -> None:
        news = MT5News.from_dict({"id": 7, "subject": "Rates", "time": "2026-11-23T10:00:00"})
        assert news.time.tzinfo is None
        assert news.time.hour == 10
