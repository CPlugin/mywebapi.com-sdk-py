from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SelectedPage")



@_attrs_define
class MT5SelectedPage:
    """ One positional window of the selected-symbol list, v2 read DTO.

        Attributes:
            symbols (list[str] | None | Unset): Symbol names of this window, in list order.
            total (int | Unset): Total number of symbols in the list at the moment of the request.
            from_ (int | Unset): Position the window starts at, echoed from the request.
     """

    symbols: list[str] | None | Unset = UNSET
    total: int | Unset = UNSET
    from_: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbols: list[str] | None | Unset
        if isinstance(self.symbols, Unset):
            symbols = UNSET
        elif isinstance(self.symbols, list):
            symbols = self.symbols


        else:
            symbols = self.symbols

        total = self.total

        from_ = self.from_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if total is not UNSET:
            field_dict["total"] = total
        if from_ is not UNSET:
            field_dict["from"] = from_

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


        total = d.pop("total", UNSET)

        from_ = d.pop("from", UNSET)

        mt5_selected_page = cls(
            symbols=symbols,
            total=total,
            from_=from_,
        )

        return mt5_selected_page

