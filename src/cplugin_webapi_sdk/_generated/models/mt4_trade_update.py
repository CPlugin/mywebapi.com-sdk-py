from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4TradeUpdate")



@_attrs_define
class MT4TradeUpdate:
    """ Type 1 mutator input for the admin direct-edit endpoint
    `AdmTradeRecordModify`. Only the fields a back-office tool would
    legitimately need to adjust are exposed; everything else (order id,
    login, symbol, volume, open/close times, gateway internals, conversion
    rates, API data blobs) is preserved from the server-side read.

    <br>
    For typical stop-loss / take-profit edits prefer
    `POST TradeTransaction` with `tradeTransactionType=BrModify`
    — that goes through the platform's audited path. This endpoint is the
    low-level admin override for back-office corrections.

        Attributes:
            order (int | Unset): Order ticket to edit (path parameter is the source of truth)
            sl (float | Unset): New stop-loss price (0 = remove SL)
            tp (float | Unset): New take-profit price (0 = remove TP)
            magic (int | Unset): Magic number / EA tag
            comment (None | str | Unset): Comment (broker-visible)
            commission (float | Unset): Manual commission override
            commission_agent (float | Unset): Manual agent-commission override
            storage (float | Unset): Swap / storage override
            profit (float | Unset): Profit override (back-office correction only)
            taxes (float | Unset): Taxes override
     """

    order: int | Unset = UNSET
    sl: float | Unset = UNSET
    tp: float | Unset = UNSET
    magic: int | Unset = UNSET
    comment: None | str | Unset = UNSET
    commission: float | Unset = UNSET
    commission_agent: float | Unset = UNSET
    storage: float | Unset = UNSET
    profit: float | Unset = UNSET
    taxes: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        order = self.order

        sl = self.sl

        tp = self.tp

        magic = self.magic

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        commission = self.commission

        commission_agent = self.commission_agent

        storage = self.storage

        profit = self.profit

        taxes = self.taxes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order is not UNSET:
            field_dict["order"] = order
        if sl is not UNSET:
            field_dict["sl"] = sl
        if tp is not UNSET:
            field_dict["tp"] = tp
        if magic is not UNSET:
            field_dict["magic"] = magic
        if comment is not UNSET:
            field_dict["comment"] = comment
        if commission is not UNSET:
            field_dict["commission"] = commission
        if commission_agent is not UNSET:
            field_dict["commissionAgent"] = commission_agent
        if storage is not UNSET:
            field_dict["storage"] = storage
        if profit is not UNSET:
            field_dict["profit"] = profit
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order = d.pop("order", UNSET)

        sl = d.pop("sl", UNSET)

        tp = d.pop("tp", UNSET)

        magic = d.pop("magic", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        commission = d.pop("commission", UNSET)

        commission_agent = d.pop("commissionAgent", UNSET)

        storage = d.pop("storage", UNSET)

        profit = d.pop("profit", UNSET)

        taxes = d.pop("taxes", UNSET)

        mt4_trade_update = cls(
            order=order,
            sl=sl,
            tp=tp,
            magic=magic,
            comment=comment,
            commission=commission,
            commission_agent=commission_agent,
            storage=storage,
            profit=profit,
            taxes=taxes,
        )

        return mt4_trade_update

