from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4CommonUpdate")



@_attrs_define
class MT4CommonUpdate:
    """ v2 mutator DTO for MT4 server-wide common settings: a partial record over the platform's
    `ConCommon` struct.

        Attributes:
            name (None | str | Unset): Trade server display name.
            owner (None | str | Unset): Broker / company display name.
            time_zone (int | None | Unset): Server time zone offset from UTC, in hours.
            daylight_correction (int | None | Unset): DST correction setting (server-specific integer).
            time_zone_real (int | None | Unset): Real time-zone (no DST) offset from UTC, in hours.
            time_sync (None | str | Unset): NTP server hostname for clock sync.
            min_client (int | None | Unset): Minimum acceptable client build number.
            min_api (int | None | Unset): Minimum client API build the trade server accepts.
            keep_emails (int | None | Unset): How long (days) to keep mailbox messages.
            keep_ticks (int | None | Unset): How long (days) to keep tick history.
            anti_flood (int | None | Unset): Anti-flood threshold (requests per second).
            flood_control (int | None | Unset): Flood-control behaviour mode.
     """

    name: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    time_zone: int | None | Unset = UNSET
    daylight_correction: int | None | Unset = UNSET
    time_zone_real: int | None | Unset = UNSET
    time_sync: None | str | Unset = UNSET
    min_client: int | None | Unset = UNSET
    min_api: int | None | Unset = UNSET
    keep_emails: int | None | Unset = UNSET
    keep_ticks: int | None | Unset = UNSET
    anti_flood: int | None | Unset = UNSET
    flood_control: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        time_zone: int | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        daylight_correction: int | None | Unset
        if isinstance(self.daylight_correction, Unset):
            daylight_correction = UNSET
        else:
            daylight_correction = self.daylight_correction

        time_zone_real: int | None | Unset
        if isinstance(self.time_zone_real, Unset):
            time_zone_real = UNSET
        else:
            time_zone_real = self.time_zone_real

        time_sync: None | str | Unset
        if isinstance(self.time_sync, Unset):
            time_sync = UNSET
        else:
            time_sync = self.time_sync

        min_client: int | None | Unset
        if isinstance(self.min_client, Unset):
            min_client = UNSET
        else:
            min_client = self.min_client

        min_api: int | None | Unset
        if isinstance(self.min_api, Unset):
            min_api = UNSET
        else:
            min_api = self.min_api

        keep_emails: int | None | Unset
        if isinstance(self.keep_emails, Unset):
            keep_emails = UNSET
        else:
            keep_emails = self.keep_emails

        keep_ticks: int | None | Unset
        if isinstance(self.keep_ticks, Unset):
            keep_ticks = UNSET
        else:
            keep_ticks = self.keep_ticks

        anti_flood: int | None | Unset
        if isinstance(self.anti_flood, Unset):
            anti_flood = UNSET
        else:
            anti_flood = self.anti_flood

        flood_control: int | None | Unset
        if isinstance(self.flood_control, Unset):
            flood_control = UNSET
        else:
            flood_control = self.flood_control


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if daylight_correction is not UNSET:
            field_dict["daylightCorrection"] = daylight_correction
        if time_zone_real is not UNSET:
            field_dict["timeZoneReal"] = time_zone_real
        if time_sync is not UNSET:
            field_dict["timeSync"] = time_sync
        if min_client is not UNSET:
            field_dict["minClient"] = min_client
        if min_api is not UNSET:
            field_dict["minApi"] = min_api
        if keep_emails is not UNSET:
            field_dict["keepEmails"] = keep_emails
        if keep_ticks is not UNSET:
            field_dict["keepTicks"] = keep_ticks
        if anti_flood is not UNSET:
            field_dict["antiFlood"] = anti_flood
        if flood_control is not UNSET:
            field_dict["floodControl"] = flood_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))


        def _parse_time_zone(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_daylight_correction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        daylight_correction = _parse_daylight_correction(d.pop("daylightCorrection", UNSET))


        def _parse_time_zone_real(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone_real = _parse_time_zone_real(d.pop("timeZoneReal", UNSET))


        def _parse_time_sync(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_sync = _parse_time_sync(d.pop("timeSync", UNSET))


        def _parse_min_client(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_client = _parse_min_client(d.pop("minClient", UNSET))


        def _parse_min_api(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_api = _parse_min_api(d.pop("minApi", UNSET))


        def _parse_keep_emails(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        keep_emails = _parse_keep_emails(d.pop("keepEmails", UNSET))


        def _parse_keep_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        keep_ticks = _parse_keep_ticks(d.pop("keepTicks", UNSET))


        def _parse_anti_flood(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        anti_flood = _parse_anti_flood(d.pop("antiFlood", UNSET))


        def _parse_flood_control(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flood_control = _parse_flood_control(d.pop("floodControl", UNSET))


        mt4_common_update = cls(
            name=name,
            owner=owner,
            time_zone=time_zone,
            daylight_correction=daylight_correction,
            time_zone_real=time_zone_real,
            time_sync=time_sync,
            min_client=min_client,
            min_api=min_api,
            keep_emails=keep_emails,
            keep_ticks=keep_ticks,
            anti_flood=anti_flood,
            flood_control=flood_control,
        )

        return mt4_common_update

