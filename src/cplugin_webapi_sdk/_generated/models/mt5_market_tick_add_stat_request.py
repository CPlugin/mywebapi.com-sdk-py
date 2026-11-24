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
  from ..models.mt5_market_tick_stat import MT5MarketTickStat





T = TypeVar("T", bound="MT5MarketTickAddStatRequest")



@_attrs_define
class MT5MarketTickAddStatRequest:
    """ A quote together with the statistical information to publish with it.

        Attributes:
            tick (MT5MarketTick | None | Unset): The quote the statistics belong to. Mandatory.
            stat (MT5MarketTickStat | None | Unset): The statistical information to publish. Mandatory.
     """

    tick: MT5MarketTick | None | Unset = UNSET
    stat: MT5MarketTickStat | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_market_tick import MT5MarketTick
        from ..models.mt5_market_tick_stat import MT5MarketTickStat
        tick: dict[str, Any] | None | Unset
        if isinstance(self.tick, Unset):
            tick = UNSET
        elif isinstance(self.tick, MT5MarketTick):
            tick = self.tick.to_dict()
        else:
            tick = self.tick

        stat: dict[str, Any] | None | Unset
        if isinstance(self.stat, Unset):
            stat = UNSET
        elif isinstance(self.stat, MT5MarketTickStat):
            stat = self.stat.to_dict()
        else:
            stat = self.stat


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if tick is not UNSET:
            field_dict["tick"] = tick
        if stat is not UNSET:
            field_dict["stat"] = stat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_market_tick import MT5MarketTick
        from ..models.mt5_market_tick_stat import MT5MarketTickStat
        d = dict(src_dict)
        def _parse_tick(data: object) -> MT5MarketTick | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tick_type_1 = MT5MarketTick.from_dict(data)



                return tick_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5MarketTick | None | Unset, data)

        tick = _parse_tick(d.pop("tick", UNSET))


        def _parse_stat(data: object) -> MT5MarketTickStat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stat_type_1 = MT5MarketTickStat.from_dict(data)



                return stat_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5MarketTickStat | None | Unset, data)

        stat = _parse_stat(d.pop("stat", UNSET))


        mt5_market_tick_add_stat_request = cls(
            tick=tick,
            stat=stat,
        )

        return mt5_market_tick_add_stat_request

