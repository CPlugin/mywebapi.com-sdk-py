from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT4TradeRestoreResult")



@_attrs_define
class MT4TradeRestoreResult:
    """ v2 DTO for a single per-order result of a backup-restore operation.
    Mirrors the platform's `TradeRestoreResult` — order ticket plus
    a 1-byte status flag.

        Attributes:
            order (int | Unset): Order ticket from the input array (matches by position)
            res (int | Unset): Per-order restore status: `0` = error, `1` = restored
     """

    order: int | Unset = UNSET
    res: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        order = self.order

        res = self.res


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order is not UNSET:
            field_dict["order"] = order
        if res is not UNSET:
            field_dict["res"] = res

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order = d.pop("order", UNSET)

        res = d.pop("res", UNSET)

        mt4_trade_restore_result = cls(
            order=order,
            res=res,
        )

        return mt4_trade_restore_result

