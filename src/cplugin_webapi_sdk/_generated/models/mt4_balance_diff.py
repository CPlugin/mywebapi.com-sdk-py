from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT4BalanceDiff")



@_attrs_define
class MT4BalanceDiff:
    """ v2 DTO returned by `AdmBalanceCheck`. Reports the difference between
    the account's recorded balance and what the MT4 server recomputes from
    closed orders + balance operations. `Diff = 0` means the integrity
    check passed; non-zero means the recorded balance has drifted and would
    be set to `recorded + Diff` if `AdmBalanceFix` ran.

        Attributes:
            login (int | Unset): Account login
            diff (float | Unset): Difference (signed). Zero means balance integrity check passed.
     """

    login: int | Unset = UNSET
    diff: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        diff = self.diff


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if diff is not UNSET:
            field_dict["diff"] = diff

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        diff = d.pop("diff", UNSET)

        mt4_balance_diff = cls(
            login=login,
            diff=diff,
        )

        return mt4_balance_diff

