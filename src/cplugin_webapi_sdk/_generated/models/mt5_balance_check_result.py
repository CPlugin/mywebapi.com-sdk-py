from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT5BalanceCheckResult")



@_attrs_define
class MT5BalanceCheckResult:
    """ Result of comparing the stored balance and credit of one account with its deals history.

        Attributes:
            login (int | Unset): Account login the result belongs to.
            balance_user (float | Unset): Balance stored in the account record at the time of the check.
            balance_history (float | Unset): Balance the deals history adds up to.
            credit_user (float | Unset): Credit stored in the account record at the time of the check.
            credit_history (float | Unset): Credit the deals history adds up to.
            mismatch (bool | Unset): Whether the stored balance or credit differs from the history.
     """

    login: int | Unset = UNSET
    balance_user: float | Unset = UNSET
    balance_history: float | Unset = UNSET
    credit_user: float | Unset = UNSET
    credit_history: float | Unset = UNSET
    mismatch: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        balance_user = self.balance_user

        balance_history = self.balance_history

        credit_user = self.credit_user

        credit_history = self.credit_history

        mismatch = self.mismatch


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if balance_user is not UNSET:
            field_dict["balanceUser"] = balance_user
        if balance_history is not UNSET:
            field_dict["balanceHistory"] = balance_history
        if credit_user is not UNSET:
            field_dict["creditUser"] = credit_user
        if credit_history is not UNSET:
            field_dict["creditHistory"] = credit_history
        if mismatch is not UNSET:
            field_dict["mismatch"] = mismatch

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        balance_user = d.pop("balanceUser", UNSET)

        balance_history = d.pop("balanceHistory", UNSET)

        credit_user = d.pop("creditUser", UNSET)

        credit_history = d.pop("creditHistory", UNSET)

        mismatch = d.pop("mismatch", UNSET)

        mt5_balance_check_result = cls(
            login=login,
            balance_user=balance_user,
            balance_history=balance_history,
            credit_user=credit_user,
            credit_history=credit_history,
            mismatch=mismatch,
        )

        return mt5_balance_check_result

