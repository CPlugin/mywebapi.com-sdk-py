from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5OnlineDisconnectResult")



@_attrs_define
class MT5OnlineDisconnectResult:
    """ Outcome of the forced disconnection of one login, v2 write DTO.

        Attributes:
            login (int | Unset): Login whose connections were dropped.
            ok (bool | Unset): True when every open session of the login was dropped.
            code (int | Unset): Numeric result of the first session that could not be dropped; zero when the login was
                dropped in full.
            status (None | str | Unset): Name of the result code in `Code`.
     """

    login: int | Unset = UNSET
    ok: bool | Unset = UNSET
    code: int | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        ok = self.ok

        code = self.code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if ok is not UNSET:
            field_dict["ok"] = ok
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        ok = d.pop("ok", UNSET)

        code = d.pop("code", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        mt5_online_disconnect_result = cls(
            login=login,
            ok=ok,
            code=code,
            status=status,
        )

        return mt5_online_disconnect_result

