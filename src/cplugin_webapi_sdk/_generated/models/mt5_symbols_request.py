from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SymbolsRequest")



@_attrs_define
class MT5SymbolsRequest:
    """ Request body naming several symbols, v2 write DTO.

        Attributes:
            symbols (list[str] | None | Unset): Symbol names exactly as the trade server holds them.
     """

    symbols: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbols: list[str] | None | Unset
        if isinstance(self.symbols, Unset):
            symbols = UNSET
        elif isinstance(self.symbols, list):
            symbols = self.symbols


        else:
            symbols = self.symbols


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbols is not UNSET:
            field_dict["symbols"] = symbols

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_symbols(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                symbols_type_0 = cast(list[str], data)

                return symbols_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        symbols = _parse_symbols(d.pop("symbols", UNSET))


        mt5_symbols_request = cls(
            symbols=symbols,
        )

        return mt5_symbols_request

