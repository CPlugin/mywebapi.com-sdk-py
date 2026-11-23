from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.so_activation import SoActivation
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Account")



@_attrs_define
class MT5Account:
    """ 
        Attributes:
            login (int): Get and set the login of the client, to whom the trading account belongs.
            currency_digits (int | None | Unset): Get and set the number of decimal places in the account deposit currency.
            balance (float | None | Unset): Get and set the balance of a trading account.
            credit (float | None | Unset): Get and set the current amount of credit given to an account.
            margin (float | None | Unset): Get and set the current value of the account margin.
            margin_free (float | None | Unset): Get and set the free margin of an account.
            margin_level (float | None | Unset): Get and set the margin level as a percentage.
            margin_leverage (int | None | Unset): Get and set the margin leverage.
            profit (float | None | Unset): Get and set the size of the current profit for all open positions.
            storage (float | None | Unset): Get and set the current size of swaps charged for open positions on the account.
            floating (float | None | Unset): Get and set the size of floating profit/loss of open positions on the account.
            equity (float | None | Unset): Get and set account equity.
            so_activation (None | SoActivation | Unset): Get and set the account status as per the minimum amount of funds
                on the account required to maintain trading positions.
            so_time (datetime.datetime | None | Unset): Get and set the time when the Margin Call or Stop Out level was
                reached.
            so_level (float | None | Unset): Get and set the margin level of an account at the time of reaching the Stop Out
                level.
            so_equity (float | None | Unset): Get and set the account equity at the time of reaching the Stop Out level.
            so_margin (float | None | Unset): Get and set the margin amount on an account at the time of reaching the Stop
                Out level.
            blocked_commission (float | None | Unset): Get and set the amount of the standard commission locked on the
                account, which has been accumulated during the day/month.
            blocked_profit (float | None | Unset): Get and set the amount of intraday profit locked on the account.
            margin_initial (float | None | Unset): Get and set the current size of the initial margin of positions on a
                trading account.
            margin_maintenance (float | None | Unset): Get and set the current size of the maintenance margin of positions
                on a trading account.
            assets (float | None | Unset): Get and set the current total amount of assets on a trading account.
            liabilities (float | None | Unset): Get and set the current total amount of liabilities on a trading account.
     """

    login: int
    currency_digits: int | None | Unset = UNSET
    balance: float | None | Unset = UNSET
    credit: float | None | Unset = UNSET
    margin: float | None | Unset = UNSET
    margin_free: float | None | Unset = UNSET
    margin_level: float | None | Unset = UNSET
    margin_leverage: int | None | Unset = UNSET
    profit: float | None | Unset = UNSET
    storage: float | None | Unset = UNSET
    floating: float | None | Unset = UNSET
    equity: float | None | Unset = UNSET
    so_activation: None | SoActivation | Unset = UNSET
    so_time: datetime.datetime | None | Unset = UNSET
    so_level: float | None | Unset = UNSET
    so_equity: float | None | Unset = UNSET
    so_margin: float | None | Unset = UNSET
    blocked_commission: float | None | Unset = UNSET
    blocked_profit: float | None | Unset = UNSET
    margin_initial: float | None | Unset = UNSET
    margin_maintenance: float | None | Unset = UNSET
    assets: float | None | Unset = UNSET
    liabilities: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        currency_digits: int | None | Unset
        if isinstance(self.currency_digits, Unset):
            currency_digits = UNSET
        else:
            currency_digits = self.currency_digits

        balance: float | None | Unset
        if isinstance(self.balance, Unset):
            balance = UNSET
        else:
            balance = self.balance

        credit: float | None | Unset
        if isinstance(self.credit, Unset):
            credit = UNSET
        else:
            credit = self.credit

        margin: float | None | Unset
        if isinstance(self.margin, Unset):
            margin = UNSET
        else:
            margin = self.margin

        margin_free: float | None | Unset
        if isinstance(self.margin_free, Unset):
            margin_free = UNSET
        else:
            margin_free = self.margin_free

        margin_level: float | None | Unset
        if isinstance(self.margin_level, Unset):
            margin_level = UNSET
        else:
            margin_level = self.margin_level

        margin_leverage: int | None | Unset
        if isinstance(self.margin_leverage, Unset):
            margin_leverage = UNSET
        else:
            margin_leverage = self.margin_leverage

        profit: float | None | Unset
        if isinstance(self.profit, Unset):
            profit = UNSET
        else:
            profit = self.profit

        storage: float | None | Unset
        if isinstance(self.storage, Unset):
            storage = UNSET
        else:
            storage = self.storage

        floating: float | None | Unset
        if isinstance(self.floating, Unset):
            floating = UNSET
        else:
            floating = self.floating

        equity: float | None | Unset
        if isinstance(self.equity, Unset):
            equity = UNSET
        else:
            equity = self.equity

        so_activation: None | str | Unset
        if isinstance(self.so_activation, Unset):
            so_activation = UNSET
        elif isinstance(self.so_activation, SoActivation):
            so_activation = self.so_activation.value
        else:
            so_activation = self.so_activation

        so_time: None | str | Unset
        if isinstance(self.so_time, Unset):
            so_time = UNSET
        elif isinstance(self.so_time, datetime.datetime):
            so_time = self.so_time.isoformat()
        else:
            so_time = self.so_time

        so_level: float | None | Unset
        if isinstance(self.so_level, Unset):
            so_level = UNSET
        else:
            so_level = self.so_level

        so_equity: float | None | Unset
        if isinstance(self.so_equity, Unset):
            so_equity = UNSET
        else:
            so_equity = self.so_equity

        so_margin: float | None | Unset
        if isinstance(self.so_margin, Unset):
            so_margin = UNSET
        else:
            so_margin = self.so_margin

        blocked_commission: float | None | Unset
        if isinstance(self.blocked_commission, Unset):
            blocked_commission = UNSET
        else:
            blocked_commission = self.blocked_commission

        blocked_profit: float | None | Unset
        if isinstance(self.blocked_profit, Unset):
            blocked_profit = UNSET
        else:
            blocked_profit = self.blocked_profit

        margin_initial: float | None | Unset
        if isinstance(self.margin_initial, Unset):
            margin_initial = UNSET
        else:
            margin_initial = self.margin_initial

        margin_maintenance: float | None | Unset
        if isinstance(self.margin_maintenance, Unset):
            margin_maintenance = UNSET
        else:
            margin_maintenance = self.margin_maintenance

        assets: float | None | Unset
        if isinstance(self.assets, Unset):
            assets = UNSET
        else:
            assets = self.assets

        liabilities: float | None | Unset
        if isinstance(self.liabilities, Unset):
            liabilities = UNSET
        else:
            liabilities = self.liabilities


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "login": login,
        })
        if currency_digits is not UNSET:
            field_dict["currencyDigits"] = currency_digits
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if margin is not UNSET:
            field_dict["margin"] = margin
        if margin_free is not UNSET:
            field_dict["marginFree"] = margin_free
        if margin_level is not UNSET:
            field_dict["marginLevel"] = margin_level
        if margin_leverage is not UNSET:
            field_dict["marginLeverage"] = margin_leverage
        if profit is not UNSET:
            field_dict["profit"] = profit
        if storage is not UNSET:
            field_dict["storage"] = storage
        if floating is not UNSET:
            field_dict["floating"] = floating
        if equity is not UNSET:
            field_dict["equity"] = equity
        if so_activation is not UNSET:
            field_dict["soActivation"] = so_activation
        if so_time is not UNSET:
            field_dict["soTime"] = so_time
        if so_level is not UNSET:
            field_dict["soLevel"] = so_level
        if so_equity is not UNSET:
            field_dict["soEquity"] = so_equity
        if so_margin is not UNSET:
            field_dict["soMargin"] = so_margin
        if blocked_commission is not UNSET:
            field_dict["blockedCommission"] = blocked_commission
        if blocked_profit is not UNSET:
            field_dict["blockedProfit"] = blocked_profit
        if margin_initial is not UNSET:
            field_dict["marginInitial"] = margin_initial
        if margin_maintenance is not UNSET:
            field_dict["marginMaintenance"] = margin_maintenance
        if assets is not UNSET:
            field_dict["assets"] = assets
        if liabilities is not UNSET:
            field_dict["liabilities"] = liabilities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login")

        def _parse_currency_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_digits = _parse_currency_digits(d.pop("currencyDigits", UNSET))


        def _parse_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        balance = _parse_balance(d.pop("balance", UNSET))


        def _parse_credit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credit = _parse_credit(d.pop("credit", UNSET))


        def _parse_margin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin = _parse_margin(d.pop("margin", UNSET))


        def _parse_margin_free(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_free = _parse_margin_free(d.pop("marginFree", UNSET))


        def _parse_margin_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_level = _parse_margin_level(d.pop("marginLevel", UNSET))


        def _parse_margin_leverage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        margin_leverage = _parse_margin_leverage(d.pop("marginLeverage", UNSET))


        def _parse_profit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profit = _parse_profit(d.pop("profit", UNSET))


        def _parse_storage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage = _parse_storage(d.pop("storage", UNSET))


        def _parse_floating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        floating = _parse_floating(d.pop("floating", UNSET))


        def _parse_equity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        equity = _parse_equity(d.pop("equity", UNSET))


        def _parse_so_activation(data: object) -> None | SoActivation | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                so_activation_type_1 = SoActivation(data)



                return so_activation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SoActivation | Unset, data)

        so_activation = _parse_so_activation(d.pop("soActivation", UNSET))


        def _parse_so_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                so_time_type_0 = datetime.datetime.fromisoformat(data)



                return so_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        so_time = _parse_so_time(d.pop("soTime", UNSET))


        def _parse_so_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        so_level = _parse_so_level(d.pop("soLevel", UNSET))


        def _parse_so_equity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        so_equity = _parse_so_equity(d.pop("soEquity", UNSET))


        def _parse_so_margin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        so_margin = _parse_so_margin(d.pop("soMargin", UNSET))


        def _parse_blocked_commission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        blocked_commission = _parse_blocked_commission(d.pop("blockedCommission", UNSET))


        def _parse_blocked_profit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        blocked_profit = _parse_blocked_profit(d.pop("blockedProfit", UNSET))


        def _parse_margin_initial(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_initial = _parse_margin_initial(d.pop("marginInitial", UNSET))


        def _parse_margin_maintenance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_maintenance = _parse_margin_maintenance(d.pop("marginMaintenance", UNSET))


        def _parse_assets(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        assets = _parse_assets(d.pop("assets", UNSET))


        def _parse_liabilities(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        liabilities = _parse_liabilities(d.pop("liabilities", UNSET))


        mt5_account = cls(
            login=login,
            currency_digits=currency_digits,
            balance=balance,
            credit=credit,
            margin=margin,
            margin_free=margin_free,
            margin_level=margin_level,
            margin_leverage=margin_leverage,
            profit=profit,
            storage=storage,
            floating=floating,
            equity=equity,
            so_activation=so_activation,
            so_time=so_time,
            so_level=so_level,
            so_equity=so_equity,
            so_margin=so_margin,
            blocked_commission=blocked_commission,
            blocked_profit=blocked_profit,
            margin_initial=margin_initial,
            margin_maintenance=margin_maintenance,
            assets=assets,
            liabilities=liabilities,
        )

        return mt5_account

