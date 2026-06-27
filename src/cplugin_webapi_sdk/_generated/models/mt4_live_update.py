from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4LiveUpdate")



@_attrs_define
class MT4LiveUpdate:
    """ v2 DTO for a single MT4 LiveUpdate configuration entry. Curated
    subset of the wrapper's ConLiveUpdate — exposes the metadata
    (Company, Path, Version/Build, connection limits and counters,
    Type, Enable, TotalFiles). The wrapper's `Files` array
    (128-element LiveInfoFile descriptor table) is intentionally
    deferred to a future endpoint to keep this payload tractable; v2
    callers needing per-file detail will get a separate
    `CfgRequestLiveUpdateFiles` in a later slice.

        Attributes:
            company (None | str | Unset): Company name advertised by the LiveUpdate service (used as cursor key)
            path (None | str | Unset): Filesystem path to the LiveUpdate files
            version (int | Unset): Service version number
            build (int | Unset): Service build number
            max_connect (int | Unset): Maximum simultaneous client connections allowed
            connections (int | Unset): Currently active client connections (read-only counter)
            type_ (int | Unset): LiveUpdate kind/type (raw wrapper int — LIVE_UPDATE_* constants)
            enable (int | Unset): Enable flag (0 = disabled, 1 = enabled — raw wrapper int)
            total_files (int | Unset): Total files served
     """

    company: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    version: int | Unset = UNSET
    build: int | Unset = UNSET
    max_connect: int | Unset = UNSET
    connections: int | Unset = UNSET
    type_: int | Unset = UNSET
    enable: int | Unset = UNSET
    total_files: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        version = self.version

        build = self.build

        max_connect = self.max_connect

        connections = self.connections

        type_ = self.type_

        enable = self.enable

        total_files = self.total_files


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if company is not UNSET:
            field_dict["company"] = company
        if path is not UNSET:
            field_dict["path"] = path
        if version is not UNSET:
            field_dict["version"] = version
        if build is not UNSET:
            field_dict["build"] = build
        if max_connect is not UNSET:
            field_dict["maxConnect"] = max_connect
        if connections is not UNSET:
            field_dict["connections"] = connections
        if type_ is not UNSET:
            field_dict["type"] = type_
        if enable is not UNSET:
            field_dict["enable"] = enable
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))


        version = d.pop("version", UNSET)

        build = d.pop("build", UNSET)

        max_connect = d.pop("maxConnect", UNSET)

        connections = d.pop("connections", UNSET)

        type_ = d.pop("type", UNSET)

        enable = d.pop("enable", UNSET)

        total_files = d.pop("totalFiles", UNSET)

        mt4_live_update = cls(
            company=company,
            path=path,
            version=version,
            build=build,
            max_connect=max_connect,
            connections=connections,
            type_=type_,
            enable=enable,
            total_files=total_files,
        )

        return mt4_live_update

