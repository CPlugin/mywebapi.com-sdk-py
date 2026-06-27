from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4SymbolGroup")



@_attrs_define
class MT4SymbolGroup:
    """ v2 DTO describing a single MT4 symbol group (security category).
    Mirrors the wrapper's ConSymbolGroup — which only carries Name and
    Description as fixed-size ANSI fields. There is no ProfitCurrency on
    the MT4-side group struct (that lives on per-symbol settings, not on
    the group level), so the DTO faithfully exposes only what exists.

        Attributes:
            name (None | str | Unset): Group name (e.g. "Forex", "CFD", "Metals")
            description (None | str | Unset): Human-readable description of the group
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

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


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        mt4_symbol_group = cls(
            name=name,
            description=description,
        )

        return mt4_symbol_group

