from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT5SymbolMarginRateMaintenanceType0")



@_attrs_define
class MT5SymbolMarginRateMaintenanceType0:
    """ orders and positions margin rates

        Attributes:
            buy (float | Unset):
            sell (float | Unset):
            buy_limit (float | Unset):
            sell_limit (float | Unset):
            buy_stop (float | Unset):
            sell_stop (float | Unset):
            buy_stop_limit (float | Unset):
            sell_stop_limit (float | Unset):
     """

    buy: float | Unset = UNSET
    sell: float | Unset = UNSET
    buy_limit: float | Unset = UNSET
    sell_limit: float | Unset = UNSET
    buy_stop: float | Unset = UNSET
    sell_stop: float | Unset = UNSET
    buy_stop_limit: float | Unset = UNSET
    sell_stop_limit: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        buy = self.buy

        sell = self.sell

        buy_limit = self.buy_limit

        sell_limit = self.sell_limit

        buy_stop = self.buy_stop

        sell_stop = self.sell_stop

        buy_stop_limit = self.buy_stop_limit

        sell_stop_limit = self.sell_stop_limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if buy is not UNSET:
            field_dict["Buy"] = buy
        if sell is not UNSET:
            field_dict["Sell"] = sell
        if buy_limit is not UNSET:
            field_dict["BuyLimit"] = buy_limit
        if sell_limit is not UNSET:
            field_dict["SellLimit"] = sell_limit
        if buy_stop is not UNSET:
            field_dict["BuyStop"] = buy_stop
        if sell_stop is not UNSET:
            field_dict["SellStop"] = sell_stop
        if buy_stop_limit is not UNSET:
            field_dict["BuyStopLimit"] = buy_stop_limit
        if sell_stop_limit is not UNSET:
            field_dict["SellStopLimit"] = sell_stop_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buy = d.pop("Buy", UNSET)

        sell = d.pop("Sell", UNSET)

        buy_limit = d.pop("BuyLimit", UNSET)

        sell_limit = d.pop("SellLimit", UNSET)

        buy_stop = d.pop("BuyStop", UNSET)

        sell_stop = d.pop("SellStop", UNSET)

        buy_stop_limit = d.pop("BuyStopLimit", UNSET)

        sell_stop_limit = d.pop("SellStopLimit", UNSET)

        mt5_symbol_margin_rate_maintenance_type_0 = cls(
            buy=buy,
            sell=sell,
            buy_limit=buy_limit,
            sell_limit=sell_limit,
            buy_stop=buy_stop,
            sell_stop=sell_stop,
            buy_stop_limit=buy_stop_limit,
            sell_stop_limit=sell_stop_limit,
        )

        return mt5_symbol_margin_rate_maintenance_type_0

