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
    """ v2 Type 1 mutator DTO for MT4 server-wide common settings. Curated
    subset of the wrapper's `ConCommon` struct — exposes the fields
    most likely to need adjustment from a SaaS surface while leaving
    runtime counters, derived state, and the wrapper's internal arrays
    to the secret-preservation overlay on the controller side.

        Attributes:
            name (None | str | Unset): Trade server display name.
            owner (None | str | Unset): Broker / company display name.
            time_zone (int | Unset): Server time zone offset from UTC, in hours.
            daylight_correction (int | Unset): DST correction setting (server-specific integer).
            time_zone_real (int | Unset): Real time-zone (no DST) offset from UTC, in hours.
            time_sync (None | str | Unset): NTP server hostname for clock sync.
            min_client (int | Unset): Minimum acceptable client build number.
            min_api (int | Unset): Minimum acceptable Manager API build number.
            keep_emails (int | Unset): How long (days) to keep mailbox messages.
            keep_ticks (int | Unset): How long (days) to keep tick history.
            anti_flood (int | Unset): Anti-flood threshold (requests per second).
            flood_control (int | Unset): Flood-control behaviour mode.
     """

    name: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    time_zone: int | Unset = UNSET
    daylight_correction: int | Unset = UNSET
    time_zone_real: int | Unset = UNSET
    time_sync: None | str | Unset = UNSET
    min_client: int | Unset = UNSET
    min_api: int | Unset = UNSET
    keep_emails: int | Unset = UNSET
    keep_ticks: int | Unset = UNSET
    anti_flood: int | Unset = UNSET
    flood_control: int | Unset = UNSET





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

        time_zone = self.time_zone

        daylight_correction = self.daylight_correction

        time_zone_real = self.time_zone_real

        time_sync: None | str | Unset
        if isinstance(self.time_sync, Unset):
            time_sync = UNSET
        else:
            time_sync = self.time_sync

        min_client = self.min_client

        min_api = self.min_api

        keep_emails = self.keep_emails

        keep_ticks = self.keep_ticks

        anti_flood = self.anti_flood

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


        time_zone = d.pop("timeZone", UNSET)

        daylight_correction = d.pop("daylightCorrection", UNSET)

        time_zone_real = d.pop("timeZoneReal", UNSET)

        def _parse_time_sync(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_sync = _parse_time_sync(d.pop("timeSync", UNSET))


        min_client = d.pop("minClient", UNSET)

        min_api = d.pop("minApi", UNSET)

        keep_emails = d.pop("keepEmails", UNSET)

        keep_ticks = d.pop("keepTicks", UNSET)

        anti_flood = d.pop("antiFlood", UNSET)

        flood_control = d.pop("floodControl", UNSET)

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

