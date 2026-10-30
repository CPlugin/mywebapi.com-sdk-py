from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5ChartBarV2")



@_attrs_define
class MT5ChartBarV2:
    """ One OHLC bar of a symbol's chart history, v2 read DTO. The trade server keeps
    history as minutes; bars of a coarser period are aggregated from those minutes
    on the boundaries of the server's trading time.

        Attributes:
            time (int | Unset): Bar opening time — seconds since 01.01.1970, in the trade server's trading time.
            date_time (datetime.datetime | Unset): The same bar opening time as a date-time without offset, for direct
                display.
            open_ (float | Unset): Open price — the price at the beginning of the bar's minute.
            high (float | Unset): Highest price reached inside the bar.
            low (float | Unset): Lowest price reached inside the bar.
            close (float | Unset): Close price — the price at the end of the bar's minute.
            tick_volume (int | Unset): Tick volume: the number of incoming ticks that moved the quote during the bar.
                Consecutive ticks with the same price count once.
            spread (int | Unset): Lowest spread, in points, recorded while the bar was forming.
            volume (int | Unset): Real traded volume executed during the bar.
     """

    time: int | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    open_: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    close: float | Unset = UNSET
    tick_volume: int | Unset = UNSET
    spread: int | Unset = UNSET
    volume: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time = self.time

        date_time: str | Unset = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

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
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
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
        time = d.pop("time", UNSET)

        _date_time = d.pop("dateTime", UNSET)
        date_time: datetime.datetime | Unset
        if isinstance(_date_time,  Unset):
            date_time = UNSET
        else:
            date_time = datetime.datetime.fromisoformat(_date_time)




        open_ = d.pop("open", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        close = d.pop("close", UNSET)

        tick_volume = d.pop("tickVolume", UNSET)

        spread = d.pop("spread", UNSET)

        volume = d.pop("volume", UNSET)

        mt5_chart_bar_v2 = cls(
            time=time,
            date_time=date_time,
            open_=open_,
            high=high,
            low=low,
            close=close,
            tick_volume=tick_volume,
            spread=spread,
            volume=volume,
        )

        return mt5_chart_bar_v2

