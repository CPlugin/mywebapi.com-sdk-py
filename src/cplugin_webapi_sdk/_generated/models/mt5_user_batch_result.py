from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset






T = TypeVar("T", bound="MT5UserBatchResult")



@_attrs_define
class MT5UserBatchResult:
    """ Outcome of a batch operation for one account.

        Attributes:
            login (int | Unset): Login of the account the result belongs to.
            code (MT5Result | Unset):
     """

    login: int | Unset = UNSET
    code: MT5Result | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        _code = d.pop("code", UNSET)
        code: MT5Result | Unset
        if isinstance(_code,  Unset):
            code = UNSET
        else:
            code = MT5Result(_code)




        mt5_user_batch_result = cls(
            login=login,
            code=code,
        )

        return mt5_user_batch_result

