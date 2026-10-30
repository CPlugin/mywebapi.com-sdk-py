from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5TickV2")



@_attrs_define
class MT5TickV2:
    """ One historical tick of a symbol, v2 read DTO.

        Attributes:
            time_msc (int | Unset): Tick time — milliseconds since 01.01.1970, in the trade server's trading time.
            time (int | Unset): The same tick time in seconds since 01.01.1970.
            date_time (datetime.datetime | Unset): The same tick time as a date-time without offset, for direct display.
            bid (float | Unset): Bid price at the tick.
            ask (float | Unset): Ask price at the tick.
            last (float | Unset): The price of the last committed transaction.
            volume (int | Unset): Volume as the data provider passed it. The platform fills both this and
                `VolumeExt`; the extended value has the higher accuracy.
            volume_ext (int | Unset): Volume with extended accuracy, as the data provider passed it.
            flags (None | str | Unset): Tick kind flags as a string: the names of the set bits, lowest bit first,
                joined by a comma and a space — for example `"Bid, Volume"`. `None`
                when no bit is set.
     """

    time_msc: int | Unset = UNSET
    time: int | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    bid: float | Unset = UNSET
    ask: float | Unset = UNSET
    last: float | Unset = UNSET
    volume: int | Unset = UNSET
    volume_ext: int | Unset = UNSET
    flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time_msc = self.time_msc

        time = self.time

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
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if time is not UNSET:
            field_dict["time"] = time
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
        time_msc = d.pop("timeMsc", UNSET)

        time = d.pop("time", UNSET)

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


        mt5_tick_v2 = cls(
            time_msc=time_msc,
            time=time,
            date_time=date_time,
            bid=bid,
            ask=ask,
            last=last,
            volume=volume,
            volume_ext=volume_ext,
            flags=flags,
        )

        return mt5_tick_v2

