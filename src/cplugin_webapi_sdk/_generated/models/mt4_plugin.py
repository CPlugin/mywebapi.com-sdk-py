from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Plugin")



@_attrs_define
class MT4Plugin:
    """ v2 DTO for MT4 plugin metadata (sidecar-only). Mirrors wrapper's
    `ConPlugin` with its embedded `PluginInfo` flattened.

        Attributes:
            file (None | str | Unset): Plugin DLL filename (max 256 chars on the wrapper side)
            name (None | str | Unset): Plugin display name (from `PluginInfo.Name`)
            version (int | Unset): Plugin version (from `PluginInfo.Version`)
            copyright_ (None | str | Unset): Plugin copyright string
            enabled (int | Unset): Enabled flag (raw int — 0 = disabled, non-zero = enabled)
            configurable (int | Unset): Configurable flag (plugin exposes editable parameters)
            manager_access (int | Unset): Manager-terminal-accessible flag
     """

    file: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    version: int | Unset = UNSET
    copyright_: None | str | Unset = UNSET
    enabled: int | Unset = UNSET
    configurable: int | Unset = UNSET
    manager_access: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version = self.version

        copyright_: None | str | Unset
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        enabled = self.enabled

        configurable = self.configurable

        manager_access = self.manager_access


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if configurable is not UNSET:
            field_dict["configurable"] = configurable
        if manager_access is not UNSET:
            field_dict["managerAccess"] = manager_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        version = d.pop("version", UNSET)

        def _parse_copyright_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))


        enabled = d.pop("enabled", UNSET)

        configurable = d.pop("configurable", UNSET)

        manager_access = d.pop("managerAccess", UNSET)

        mt4_plugin = cls(
            file=file,
            name=name,
            version=version,
            copyright_=copyright_,
            enabled=enabled,
            configurable=configurable,
            manager_access=manager_access,
        )

        return mt4_plugin

