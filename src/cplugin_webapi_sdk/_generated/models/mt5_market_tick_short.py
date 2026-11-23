from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5MarketTickShort")



@_attrs_define
class MT5MarketTickShort:
    """ A summary quote record of a symbol.

        Attributes:
            time (int | Unset): Quote time — seconds since 01.01.1970 in the trading time of the trade server.
            time_msc (int | Unset): Quote time — milliseconds since 01.01.1970 in the trading time of the trade server.
            date_time (datetime.datetime | Unset): The same quote time as a date-time without offset, for direct reading.
            bid (float | Unset): Bid price.
            ask (float | Unset): Ask price.
            last (float | Unset): Price of the last committed deal.
            volume (int | Unset): Volume of the last deal, as the data provider passed it.
            volume_ext (int | Unset): Volume of the last deal with extended accuracy.
            flags (None | str | Unset): Kind of the tick as the names of the set flags, for example `"Bid, Volume"`.
     """

    time: int | Unset = UNSET
    time_msc: int | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    bid: float | Unset = UNSET
    ask: float | Unset = UNSET
    last: float | Unset = UNSET
    volume: int | Unset = UNSET
    volume_ext: int | Unset = UNSET
    flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time = self.time

        time_msc = self.time_msc

        date_time: str | Unset = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        bid = self.bid

        ask = self.ask

        last = self.last

        volume = self.volume

        volume_ext = self.volume_ext

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask
        if last is not UNSET:
            field_dict["last"] = last
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        time_msc = d.pop("timeMsc", UNSET)

        _date_time = d.pop("dateTime", UNSET)
        date_time: datetime.datetime | Unset
        if isinstance(_date_time,  Unset):
            date_time = UNSET
        else:
            date_time = datetime.datetime.fromisoformat(_date_time)




        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        last = d.pop("last", UNSET)

        volume = d.pop("volume", UNSET)

        volume_ext = d.pop("volumeExt", UNSET)

        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        mt5_market_tick_short = cls(
            time=time,
            time_msc=time_msc,
            date_time=date_time,
            bid=bid,
            ask=ask,
            last=last,
            volume=volume,
            volume_ext=volume_ext,
            flags=flags,
        )

        return mt5_market_tick_short

