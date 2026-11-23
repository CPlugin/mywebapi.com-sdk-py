from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TradeProfitResult")



@_attrs_define
class TradeProfitResult:
    """ Result of a profit calculation, v2 response DTO.

        Attributes:
            profit (float | Unset): Profit of the hypothetical position in the deposit currency of the group.
            profit_rate (float | Unset): Rate that converts the profit of the symbol into the deposit currency of the group.
     """

    profit: float | Unset = UNSET
    profit_rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        profit = self.profit

        profit_rate = self.profit_rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if profit is not UNSET:
            field_dict["profit"] = profit
        if profit_rate is not UNSET:
            field_dict["profitRate"] = profit_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profit = d.pop("profit", UNSET)

        profit_rate = d.pop("profitRate", UNSET)

        trade_profit_result = cls(
            profit=profit,
            profit_rate=profit_rate,
        )

        return trade_profit_result

