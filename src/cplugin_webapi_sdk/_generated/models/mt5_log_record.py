from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5LogRecord")



@_attrs_define
class MT5LogRecord:
    """ Entry of the journal of a trade server.

        Attributes:
            flags (int | Unset): Entry flags as a bit mask.
            code (int | Unset): Platform code of the event.
            type_ (int | Unset): Platform type of the event.
            time (datetime.datetime | None | Unset): Time of the entry, in UTC.
            time_msc (datetime.datetime | None | Unset): Time of the entry with millisecond precision, in UTC.
            source (None | str | Unset): Source of the entry: the component of the trade server that recorded it.
            message (None | str | Unset): Text of the entry.
     """

    flags: int | Unset = UNSET
    code: int | Unset = UNSET
    type_: int | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    time_msc: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        flags = self.flags

        code = self.code

        type_ = self.type_

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        time_msc: None | str | Unset
        if isinstance(self.time_msc, Unset):
            time_msc = UNSET
        elif isinstance(self.time_msc, datetime.datetime):
            time_msc = self.time_msc.isoformat()
        else:
            time_msc = self.time_msc

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if flags is not UNSET:
            field_dict["flags"] = flags
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time is not UNSET:
            field_dict["time"] = time
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if source is not UNSET:
            field_dict["source"] = source
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flags = d.pop("flags", UNSET)

        code = d.pop("code", UNSET)

        type_ = d.pop("type", UNSET)

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


        def _parse_time_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_msc = _parse_time_msc(d.pop("timeMsc", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        mt5_log_record = cls(
            flags=flags,
            code=code,
            type_=type_,
            time=time,
            time_msc=time_msc,
            source=source,
            message=message,
        )

        return mt5_log_record

