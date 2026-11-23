from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5LicenseCheckRequest")



@_attrs_define
class MT5LicenseCheckRequest:
    """ Application license to verify against the license of the trade server.

        Attributes:
            name (None | str | Unset): Name of the application as it appears in the platform license, up to 128 characters.
            random (None | str | Unset): Random sequence, up to 256 bytes. Transferred whole, without interpretation.
     """

    name: None | str | Unset = UNSET
    random: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        random: None | str | Unset
        if isinstance(self.random, Unset):
            random = UNSET
        else:
            random = self.random


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if random is not UNSET:
            field_dict["random"] = random

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


        def _parse_random(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        random = _parse_random(d.pop("random", UNSET))


        mt5_license_check_request = cls(
            name=name,
            random=random,
        )

        return mt5_license_check_request

