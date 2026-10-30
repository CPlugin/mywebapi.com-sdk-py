from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Common")



@_attrs_define
class MT4Common:
    """ v2 DTO for MT4 server-wide common settings. Curated subset of the
    the platform's ConCommon struct — exposes fields useful to clients while
    shielding the v2 contract from MetaQuotes schema drift.

        Attributes:
            name (None | str | Unset): Trade server name
            owner (None | str | Unset): Broker / company display name
            build (int | Unset): Trade server build number
            version (int | Unset): Trade server version
            time_zone (int | Unset): Server time zone offset from UTC, in hours (DST-adjusted)
     """

    name: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    build: int | Unset = UNSET
    version: int | Unset = UNSET
    time_zone: int | Unset = UNSET





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

        build = self.build

        version = self.version

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if build is not UNSET:
            field_dict["build"] = build
        if version is not UNSET:
            field_dict["version"] = version
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

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


        build = d.pop("build", UNSET)

        version = d.pop("version", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        mt4_common = cls(
            name=name,
            owner=owner,
            build=build,
            version=version,
            time_zone=time_zone,
        )

        return mt4_common

