from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5BatchUpdateResult")



@_attrs_define
class MT5BatchUpdateResult:
    """ Outcome of one entry of a batch update, in the order the entries were sent.

        Attributes:
            name (None | str | Unset): Group name or symbol name the entry refers to.
            ok (bool | Unset): True when the trade server applied the entry.
            code (None | str | Unset): Platform result code of the entry, as its name.
     """

    name: None | str | Unset = UNSET
    ok: bool | Unset = UNSET
    code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ok = self.ok

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if ok is not UNSET:
            field_dict["ok"] = ok
        if code is not UNSET:
            field_dict["code"] = code

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


        ok = d.pop("ok", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        mt5_batch_update_result = cls(
            name=name,
            ok=ok,
            code=code,
        )

        return mt5_batch_update_result

