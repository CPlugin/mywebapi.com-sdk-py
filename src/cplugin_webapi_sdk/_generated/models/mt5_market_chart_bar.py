from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5MarketChartBar")



@_attrs_define
class MT5MarketChartBar:
    """ One minute bar of a symbol, as sent for a history change.

        Attributes:
            time (datetime.datetime | None | Unset): Bar opening time as a trading time of the trade server. Mandatory.
            open_ (float | Unset): Open price. A value of zero deletes the stored bar with the same time.
            high (float | Unset): Highest price of the minute.
            low (float | Unset): Lowest price of the minute.
            close (float | Unset): Close price of the minute.
            tick_volume (int | Unset): Tick volume — the number of incoming ticks that moved the quote during the minute.
            spread (int | Unset): Lowest spread, in points, recorded while the minute was forming.
            volume (int | Unset): Real traded volume executed during the minute.
     """

    time: datetime.datetime | None | Unset = UNSET
    open_: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    close: float | Unset = UNSET
    tick_volume: int | Unset = UNSET
    spread: int | Unset = UNSET
    volume: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        tick_volume = self.tick_volume

        spread = self.spread

        volume = self.volume


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if open_ is not UNSET:
            field_dict["open"] = open_
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if close is not UNSET:
            field_dict["close"] = close
        if tick_volume is not UNSET:
            field_dict["tickVolume"] = tick_volume
        if spread is not UNSET:
            field_dict["spread"] = spread
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)



                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        open_ = d.pop("open", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        close = d.pop("close", UNSET)

        tick_volume = d.pop("tickVolume", UNSET)

        spread = d.pop("spread", UNSET)

        volume = d.pop("volume", UNSET)

        mt5_market_chart_bar = cls(
            time=time,
            open_=open_,
            high=high,
            low=low,
            close=close,
            tick_volume=tick_volume,
            spread=spread,
            volume=volume,
        )

        return mt5_market_chart_bar

