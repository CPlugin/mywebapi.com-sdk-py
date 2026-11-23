from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SettingFile")



@_attrs_define
class MT5SettingFile:
    """ Settings file stored in the directory of the manager account on the trade server.

        Attributes:
            section (None | str | Unset): Name of the subfolder of the manager directory.
            key (None | str | Unset): Name of the file.
            data (None | str | Unset): Content of the file. Transferred whole, without interpretation.
     """

    section: None | str | Unset = UNSET
    key: None | str | Unset = UNSET
    data: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        section: None | str | Unset
        if isinstance(self.section, Unset):
            section = UNSET
        else:
            section = self.section

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if section is not UNSET:
            field_dict["section"] = section
        if key is not UNSET:
            field_dict["key"] = key
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_section(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section = _parse_section(d.pop("section", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        mt5_setting_file = cls(
            section=section,
            key=key,
            data=data,
        )

        return mt5_setting_file

