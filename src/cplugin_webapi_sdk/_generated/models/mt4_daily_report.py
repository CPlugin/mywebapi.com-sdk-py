from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4DailyReport")



@_attrs_define
class MT4DailyReport:
    """ v2 DTO mirroring the wrapper's `DailyReport`: one end-of-day
    balance/equity/PnL snapshot for a single account. Used by the broker
    daily-report family (per-login query, bulk pull, incremental sync).
    Internal underscore-prefixed unix-time field, the `Next` pointer
    chain, and the 3-int `Reserved` padding are intentionally excluded.
    Note: `Ctm` is reported by the MT4 server in its local time zone,
    not UTC — clients should treat it as "broker day boundary" and convert
    as appropriate.

        Attributes:
            login (int | Unset): Account login the report belongs to
            ctm (datetime.datetime | Unset): Day boundary timestamp (wrapper internal: __time32_t, server-local time)
            group (None | str | Unset): Trading group the account was in on that day
            bank (None | str | Unset): Free-form bank/payment identifier recorded with the day's deposits
            balance_prev (float | Unset): Balance at the start of the reporting day
            balance (float | Unset): Balance at the end of the reporting day
            deposit (float | Unset): Net deposits credited within the day (positive = inflow)
            credit (float | Unset): Credit balance at end-of-day
            profit_closed (float | Unset): Closed-position profit/loss realised within the day
            profit (float | Unset): Floating (open-position) profit/loss at end-of-day
            equity (float | Unset): Equity at end-of-day (Balance + Credit + Profit)
            margin (float | Unset): Used margin at end-of-day
            margin_free (float | Unset): Free margin at end-of-day (Equity - Margin)
     """

    login: int | Unset = UNSET
    ctm: datetime.datetime | Unset = UNSET
    group: None | str | Unset = UNSET
    bank: None | str | Unset = UNSET
    balance_prev: float | Unset = UNSET
    balance: float | Unset = UNSET
    deposit: float | Unset = UNSET
    credit: float | Unset = UNSET
    profit_closed: float | Unset = UNSET
    profit: float | Unset = UNSET
    equity: float | Unset = UNSET
    margin: float | Unset = UNSET
    margin_free: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        ctm: str | Unset = UNSET
        if not isinstance(self.ctm, Unset):
            ctm = self.ctm.isoformat()

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        bank: None | str | Unset
        if isinstance(self.bank, Unset):
            bank = UNSET
        else:
            bank = self.bank

        balance_prev = self.balance_prev

        balance = self.balance

        deposit = self.deposit

        credit = self.credit

        profit_closed = self.profit_closed

        profit = self.profit

        equity = self.equity

        margin = self.margin

        margin_free = self.margin_free


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if ctm is not UNSET:
            field_dict["ctm"] = ctm
        if group is not UNSET:
            field_dict["group"] = group
        if bank is not UNSET:
            field_dict["bank"] = bank
        if balance_prev is not UNSET:
            field_dict["balancePrev"] = balance_prev
        if balance is not UNSET:
            field_dict["balance"] = balance
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if credit is not UNSET:
            field_dict["credit"] = credit
        if profit_closed is not UNSET:
            field_dict["profitClosed"] = profit_closed
        if profit is not UNSET:
            field_dict["profit"] = profit
        if equity is not UNSET:
            field_dict["equity"] = equity
        if margin is not UNSET:
            field_dict["margin"] = margin
        if margin_free is not UNSET:
            field_dict["marginFree"] = margin_free

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        _ctm = d.pop("ctm", UNSET)
        ctm: datetime.datetime | Unset
        if isinstance(_ctm,  Unset):
            ctm = UNSET
        else:
            ctm = datetime.datetime.fromisoformat(_ctm)




        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_bank(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank = _parse_bank(d.pop("bank", UNSET))


        balance_prev = d.pop("balancePrev", UNSET)

        balance = d.pop("balance", UNSET)

        deposit = d.pop("deposit", UNSET)

        credit = d.pop("credit", UNSET)

        profit_closed = d.pop("profitClosed", UNSET)

        profit = d.pop("profit", UNSET)

        equity = d.pop("equity", UNSET)

        margin = d.pop("margin", UNSET)

        margin_free = d.pop("marginFree", UNSET)

        mt4_daily_report = cls(
            login=login,
            ctm=ctm,
            group=group,
            bank=bank,
            balance_prev=balance_prev,
            balance=balance,
            deposit=deposit,
            credit=credit,
            profit_closed=profit_closed,
            profit=profit,
            equity=equity,
            margin=margin,
            margin_free=margin_free,
        )

        return mt4_daily_report

