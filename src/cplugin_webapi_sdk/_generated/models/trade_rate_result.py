from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TradeRateResult")



@_attrs_define
class TradeRateResult:
    """ Result of a conversion rate calculation, v2 response DTO.

        Attributes:
            rate (float | Unset): Rate of buying or selling the base currency for the calculation currency.
     """

    rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        rate = self.rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        trade_rate_result = cls(
            rate=rate,
        )

        return trade_rate_result

