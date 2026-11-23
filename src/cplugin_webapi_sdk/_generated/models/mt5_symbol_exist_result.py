from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SymbolExistResult")



@_attrs_define
class MT5SymbolExistResult:
    """ Answer to the availability check of a symbol for a group: the platform result code and
    whether the group settings allow the symbol.

        Attributes:
            symbol (None | str | Unset): Symbol name that was checked.
            group (None | str | Unset): Group name the check was made for.
            available (bool | Unset): True when the group settings allow working with the symbol.
            code (None | str | Unset): Platform result code of the check, as its name.
     """

    symbol: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    available: bool | Unset = UNSET
    code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        available = self.available

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if group is not UNSET:
            field_dict["group"] = group
        if available is not UNSET:
            field_dict["available"] = available
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        available = d.pop("available", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        mt5_symbol_exist_result = cls(
            symbol=symbol,
            group=group,
            available=available,
            code=code,
        )

        return mt5_symbol_exist_result

