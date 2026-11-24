from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SelectedShiftRequest")



@_attrs_define
class MT5SelectedShiftRequest:
    """ Request body moving one symbol inside the selected list, v2 write DTO.

        Attributes:
            pos (int | None | Unset): Position of the symbol in the list, starting from zero.
            shift (int | None | Unset): Offset from the current position: a negative value moves the symbol towards the top
                of
                the list, a positive one towards its end.
     """

    pos: int | None | Unset = UNSET
    shift: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        pos: int | None | Unset
        if isinstance(self.pos, Unset):
            pos = UNSET
        else:
            pos = self.pos

        shift: int | None | Unset
        if isinstance(self.shift, Unset):
            shift = UNSET
        else:
            shift = self.shift


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if pos is not UNSET:
            field_dict["pos"] = pos
        if shift is not UNSET:
            field_dict["shift"] = shift

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_pos(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pos = _parse_pos(d.pop("pos", UNSET))


        def _parse_shift(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shift = _parse_shift(d.pop("shift", UNSET))


        mt5_selected_shift_request = cls(
            pos=pos,
            shift=shift,
        )

        return mt5_selected_shift_request

