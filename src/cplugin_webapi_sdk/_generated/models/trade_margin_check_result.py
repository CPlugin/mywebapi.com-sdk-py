from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_account import MT5Account





T = TypeVar("T", bound="TradeMarginCheckResult")



@_attrs_define
class TradeMarginCheckResult:
    """ Answer of a margin check, v2 response DTO.

        Attributes:
            allowed (bool | Unset): Whether the account has enough free margin for the order. `false` is a normal
                answer, not an error: the order would be rejected by the trade server.
            account_new (MT5Account | None | Unset): Estimated state of the account after the order; empty when the server
                did not fill it.
            account_current (MT5Account | None | Unset): State of the account at the moment of the check.
     """

    allowed: bool | Unset = UNSET
    account_new: MT5Account | None | Unset = UNSET
    account_current: MT5Account | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_account import MT5Account
        allowed = self.allowed

        account_new: dict[str, Any] | None | Unset
        if isinstance(self.account_new, Unset):
            account_new = UNSET
        elif isinstance(self.account_new, MT5Account):
            account_new = self.account_new.to_dict()
        else:
            account_new = self.account_new

        account_current: dict[str, Any] | None | Unset
        if isinstance(self.account_current, Unset):
            account_current = UNSET
        elif isinstance(self.account_current, MT5Account):
            account_current = self.account_current.to_dict()
        else:
            account_current = self.account_current


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if account_new is not UNSET:
            field_dict["accountNew"] = account_new
        if account_current is not UNSET:
            field_dict["accountCurrent"] = account_current

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_account import MT5Account
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        def _parse_account_new(data: object) -> MT5Account | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_new_type_1 = MT5Account.from_dict(data)



                return account_new_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5Account | None | Unset, data)

        account_new = _parse_account_new(d.pop("accountNew", UNSET))


        def _parse_account_current(data: object) -> MT5Account | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_current_type_1 = MT5Account.from_dict(data)



                return account_current_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5Account | None | Unset, data)

        account_current = _parse_account_current(d.pop("accountCurrent", UNSET))


        trade_margin_check_result = cls(
            allowed=allowed,
            account_new=account_new,
            account_current=account_current,
        )

        return trade_margin_check_result

