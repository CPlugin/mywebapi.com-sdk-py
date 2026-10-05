from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4ServerLog")



@_attrs_define
class MT4ServerLog:
    """ v2 DTO for one MT4 server journal entry. Returned by `JournalRequest`
    when querying server-side logs for a date window. Same field set as the
    the platform's `ServerLog` — the platform struct is already minimal, no
    secrets to drop. `Code` is returned as its name.

        Attributes:
            code (None | str | Unset): Log level / message category (Ok / Trade / Login / Warn / Err / Att).
            time (None | str | Unset): Server-side timestamp as the platform formats it (string, not DateTime — preserved
                verbatim)
            ip (None | str | Unset): Client IP recorded for the event (empty for server-internal events)
            message (None | str | Unset): Free-text log message
     """

    code: None | str | Unset = UNSET
    time: None | str | Unset = UNSET
    ip: None | str | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if time is not UNSET:
            field_dict["time"] = time
        if ip is not UNSET:
            field_dict["ip"] = ip
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        mt4_server_log = cls(
            code=code,
            time=time,
            ip=ip,
            message=message,
        )

        return mt4_server_log

