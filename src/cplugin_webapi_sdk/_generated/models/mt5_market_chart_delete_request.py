from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5MarketChartDeleteRequest")



@_attrs_define
class MT5MarketChartDeleteRequest:
    """ Bars to delete from the chart history of a symbol.

        Attributes:
            times (list[int] | None | Unset): Opening times of the bars to delete, in seconds since 01.01.1970. Must be non-
                empty.
     """

    times: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        times: list[int] | None | Unset
        if isinstance(self.times, Unset):
            times = UNSET
        elif isinstance(self.times, list):
            times = self.times


        else:
            times = self.times


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if times is not UNSET:
            field_dict["times"] = times

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_times(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                times_type_0 = cast(list[int], data)

                return times_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        times = _parse_times(d.pop("times", UNSET))


        mt5_market_chart_delete_request = cls(
            times=times,
        )

        return mt5_market_chart_delete_request

