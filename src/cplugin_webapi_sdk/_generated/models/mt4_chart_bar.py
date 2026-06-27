from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4ChartBar")



@_attrs_define
class MT4ChartBar:
    """ v2 DTO for one OHLC chart bar. Curated from the wrapper's `RateInfoEx`;
    drops the internal `SymbolMultiply`/`Digits` scaling helpers
    (callers don't need them — the wrapper's `buildRI` already
    normalised Open/High/Low/Close from raw int prices into floating point).

        Attributes:
            time (datetime.datetime | Unset): Bar timestamp (UTC, start of the bar's period)
            open_ (float | Unset): Open price
            high (float | Unset): High price during the bar
            low (float | Unset): Low price during the bar
            close (float | Unset): Close price
            volume (float | Unset): Trading volume during the bar (lots × 100 in MT4 convention)
     """

    time: datetime.datetime | Unset = UNSET
    open_: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    close: float | Unset = UNSET
    volume: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

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
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




        open_ = d.pop("open", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        close = d.pop("close", UNSET)

        volume = d.pop("volume", UNSET)

        mt4_chart_bar = cls(
            time=time,
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
        )

        return mt4_chart_bar

