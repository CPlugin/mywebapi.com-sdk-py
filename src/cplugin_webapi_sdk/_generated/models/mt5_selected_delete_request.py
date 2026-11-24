from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SelectedDeleteRequest")



@_attrs_define
class MT5SelectedDeleteRequest:
    """ Request body removing one symbol from the selected list, v2 write DTO.

        Attributes:
            symbol (None | str | Unset): Symbol name to remove.
            pos (int | None | Unset): Position of the symbol in the list, starting from zero.
     """

    symbol: None | str | Unset = UNSET
    pos: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        pos: int | None | Unset
        if isinstance(self.pos, Unset):
            pos = UNSET
        else:
            pos = self.pos


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if pos is not UNSET:
            field_dict["pos"] = pos

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


        def _parse_pos(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pos = _parse_pos(d.pop("pos", UNSET))


        mt5_selected_delete_request = cls(
            symbol=symbol,
            pos=pos,
        )

        return mt5_selected_delete_request

