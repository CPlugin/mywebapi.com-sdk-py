from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_market_tick import MT5MarketTick





T = TypeVar("T", bound="MT5MarketTickAddBatchRequest")



@_attrs_define
class MT5MarketTickAddBatchRequest:
    """ Quotes to add into the price stream in one call.

        Attributes:
            ticks (list[MT5MarketTick] | None | Unset): Quotes to add. Must be non-empty.
     """

    ticks: list[MT5MarketTick] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_market_tick import MT5MarketTick
        ticks: list[dict[str, Any]] | None | Unset
        if isinstance(self.ticks, Unset):
            ticks = UNSET
        elif isinstance(self.ticks, list):
            ticks = []
            for ticks_type_0_item_data in self.ticks:
                ticks_type_0_item = ticks_type_0_item_data.to_dict()
                ticks.append(ticks_type_0_item)


        else:
            ticks = self.ticks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ticks is not UNSET:
            field_dict["ticks"] = ticks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_market_tick import MT5MarketTick
        d = dict(src_dict)
        def _parse_ticks(data: object) -> list[MT5MarketTick] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ticks_type_0 = []
                _ticks_type_0 = data
                for ticks_type_0_item_data in (_ticks_type_0):
                    ticks_type_0_item = MT5MarketTick.from_dict(ticks_type_0_item_data)



                    ticks_type_0.append(ticks_type_0_item)

                return ticks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5MarketTick] | None | Unset, data)

        ticks = _parse_ticks(d.pop("ticks", UNSET))


        mt5_market_tick_add_batch_request = cls(
            ticks=ticks,
        )

        return mt5_market_tick_add_batch_request

