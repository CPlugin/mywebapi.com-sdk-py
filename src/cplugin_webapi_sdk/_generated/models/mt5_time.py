from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Time")



@_attrs_define
class MT5Time:
    """ Server time configuration (MT5 CIMTConTime), v2 read DTO.

        Attributes:
            time_zone (int | Unset): Server time zone, minutes from GMT (0 = GMT, 60 = GMT+1).
            time_server (None | str | Unset): Time synchronization server address (TIME/NTP).
            daylight (bool | Unset): Daylight saving time mode enabled.
            daylight_state (int | Unset): Daylight saving state (0 = no DST in zone, non-zero otherwise).
     """

    time_zone: int | Unset = UNSET
    time_server: None | str | Unset = UNSET
    daylight: bool | Unset = UNSET
    daylight_state: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time_zone = self.time_zone

        time_server: None | str | Unset
        if isinstance(self.time_server, Unset):
            time_server = UNSET
        else:
            time_server = self.time_server

        daylight = self.daylight

        daylight_state = self.daylight_state


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if time_server is not UNSET:
            field_dict["timeServer"] = time_server
        if daylight is not UNSET:
            field_dict["daylight"] = daylight
        if daylight_state is not UNSET:
            field_dict["daylightState"] = daylight_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_zone = d.pop("timeZone", UNSET)

        def _parse_time_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_server = _parse_time_server(d.pop("timeServer", UNSET))


        daylight = d.pop("daylight", UNSET)

        daylight_state = d.pop("daylightState", UNSET)

        mt5_time = cls(
            time_zone=time_zone,
            time_server=time_server,
            daylight=daylight,
            daylight_state=daylight_state,
        )

        return mt5_time

