from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_order import MT5Order
  from ..models.mt5_position import MT5Position





T = TypeVar("T", bound="MT5Daily")



@_attrs_define
class MT5Daily:
    """ Daily report of one client account, v2 read DTO.

        Attributes:
            datetime_ (int | Unset): Time the report was generated, in seconds since 01.01.1970 as the trade server counts
                them.
            datetime_prev (int | Unset): Time of the previous report of the same account, in seconds since 01.01.1970.
            login (int | Unset): Login of the account the report belongs to.
            name (None | str | Unset): Name of the account holder as stored in the account.
            group (None | str | Unset): Group of the account.
            currency (None | str | Unset): Deposit currency of the account.
            currency_digits (int | Unset): Number of decimal places of the deposit currency.
            company (None | str | Unset): Company serving the account.
            e_mail (None | str | Unset): Email of the account holder.
            balance (float | Unset): Balance of the account at the report time.
            credit (float | Unset): Amount of credit funds of the account at the report time.
            interest_rate (float | Unset): Annual interest rate of the account, in percent.
            commission_daily (float | Unset): Commissions charged from the account during the reported day.
            commission_monthly (float | Unset): Commissions charged from the account during the current month.
            agent_daily (float | Unset): Agent commission charged for the trade operations of the reported day.
            agent_monthly (float | Unset): Agent commission charged for the trade operations of the current month.
            balance_prev_day (float | Unset): Balance of the account at the end of the previous day.
            balance_prev_month (float | Unset): Balance of the account at the end of the previous month.
            equity_prev_day (float | Unset): Equity of the account at the end of the previous day.
            equity_prev_month (float | Unset): Equity of the account at the end of the previous month.
            margin (float | Unset): Margin reserved for the open positions of the account.
            margin_free (float | Unset): Free margin of the account.
            margin_level (float | Unset): Margin level of the account, in percent.
            margin_leverage (int | Unset): Margin leverage of the account.
            profit (float | Unset): Current profit of all open positions of the account.
            profit_storage (float | Unset): Swaps charged for the open positions of the account but not yet reflected in the
                balance.
            profit_equity (float | Unset): Current floating equity of the account.
            profit_assets (float | Unset): Current assets of the account.
            profit_liabilities (float | Unset): Current liabilities of the account.
            daily_profit (float | Unset): Profit of the account for the reported day.
            daily_balance (float | Unset): Amount accrued to the balance of the account during the reported day.
            daily_credit (float | Unset): Credit given to the account during the reported day.
            daily_charge (float | Unset): Other charges from the balance of the account during the reported day.
            daily_correction (float | Unset): Corrective balance operations of the reported day.
            daily_bonus (float | Unset): Bonuses added to the balance of the account during the reported day.
            daily_storage (float | Unset): Swaps calculated for the account for the reported day.
            daily_comm_instant (float | Unset): Instant commissions charged from the account during the reported day.
            daily_comm_round (float | Unset): Turnover commissions charged from the account during the reported day.
            daily_comm_fee (float | Unset): Fee charged for the deals of the account during the reported day.
            daily_dividend (float | Unset): Dividends accrued to the account for the reported day.
            daily_taxes (float | Unset): Taxes withheld from the funds of the account for the reported day.
            daily_so_compensation (float | Unset): Negative balance compensation accrued to the account for the reported
                day.
            daily_so_compensation_credit (float | Unset): Credit funds withdrawn during the reported day as a result of a
                negative balance compensation.
            daily_agent (float | Unset): Agent commission charged for the trade operations of the reported day.
            daily_interest (float | Unset): Amount accrued to the account under the annual interest rate for the reported
                day.
            positions (list[MT5Position] | None | Unset): Open positions of the account; `null` in a lightweight report.
            orders (list[MT5Order] | None | Unset): Pending orders of the account; `null` in a lightweight report.
     """

    datetime_: int | Unset = UNSET
    datetime_prev: int | Unset = UNSET
    login: int | Unset = UNSET
    name: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    currency_digits: int | Unset = UNSET
    company: None | str | Unset = UNSET
    e_mail: None | str | Unset = UNSET
    balance: float | Unset = UNSET
    credit: float | Unset = UNSET
    interest_rate: float | Unset = UNSET
    commission_daily: float | Unset = UNSET
    commission_monthly: float | Unset = UNSET
    agent_daily: float | Unset = UNSET
    agent_monthly: float | Unset = UNSET
    balance_prev_day: float | Unset = UNSET
    balance_prev_month: float | Unset = UNSET
    equity_prev_day: float | Unset = UNSET
    equity_prev_month: float | Unset = UNSET
    margin: float | Unset = UNSET
    margin_free: float | Unset = UNSET
    margin_level: float | Unset = UNSET
    margin_leverage: int | Unset = UNSET
    profit: float | Unset = UNSET
    profit_storage: float | Unset = UNSET
    profit_equity: float | Unset = UNSET
    profit_assets: float | Unset = UNSET
    profit_liabilities: float | Unset = UNSET
    daily_profit: float | Unset = UNSET
    daily_balance: float | Unset = UNSET
    daily_credit: float | Unset = UNSET
    daily_charge: float | Unset = UNSET
    daily_correction: float | Unset = UNSET
    daily_bonus: float | Unset = UNSET
    daily_storage: float | Unset = UNSET
    daily_comm_instant: float | Unset = UNSET
    daily_comm_round: float | Unset = UNSET
    daily_comm_fee: float | Unset = UNSET
    daily_dividend: float | Unset = UNSET
    daily_taxes: float | Unset = UNSET
    daily_so_compensation: float | Unset = UNSET
    daily_so_compensation_credit: float | Unset = UNSET
    daily_agent: float | Unset = UNSET
    daily_interest: float | Unset = UNSET
    positions: list[MT5Position] | None | Unset = UNSET
    orders: list[MT5Order] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_order import MT5Order
        from ..models.mt5_position import MT5Position
        datetime_ = self.datetime_

        datetime_prev = self.datetime_prev

        login = self.login

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        currency_digits = self.currency_digits

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        e_mail: None | str | Unset
        if isinstance(self.e_mail, Unset):
            e_mail = UNSET
        else:
            e_mail = self.e_mail

        balance = self.balance

        credit = self.credit

        interest_rate = self.interest_rate

        commission_daily = self.commission_daily

        commission_monthly = self.commission_monthly

        agent_daily = self.agent_daily

        agent_monthly = self.agent_monthly

        balance_prev_day = self.balance_prev_day

        balance_prev_month = self.balance_prev_month

        equity_prev_day = self.equity_prev_day

        equity_prev_month = self.equity_prev_month

        margin = self.margin

        margin_free = self.margin_free

        margin_level = self.margin_level

        margin_leverage = self.margin_leverage

        profit = self.profit

        profit_storage = self.profit_storage

        profit_equity = self.profit_equity

        profit_assets = self.profit_assets

        profit_liabilities = self.profit_liabilities

        daily_profit = self.daily_profit

        daily_balance = self.daily_balance

        daily_credit = self.daily_credit

        daily_charge = self.daily_charge

        daily_correction = self.daily_correction

        daily_bonus = self.daily_bonus

        daily_storage = self.daily_storage

        daily_comm_instant = self.daily_comm_instant

        daily_comm_round = self.daily_comm_round

        daily_comm_fee = self.daily_comm_fee

        daily_dividend = self.daily_dividend

        daily_taxes = self.daily_taxes

        daily_so_compensation = self.daily_so_compensation

        daily_so_compensation_credit = self.daily_so_compensation_credit

        daily_agent = self.daily_agent

        daily_interest = self.daily_interest

        positions: list[dict[str, Any]] | None | Unset
        if isinstance(self.positions, Unset):
            positions = UNSET
        elif isinstance(self.positions, list):
            positions = []
            for positions_type_0_item_data in self.positions:
                positions_type_0_item = positions_type_0_item_data.to_dict()
                positions.append(positions_type_0_item)


        else:
            positions = self.positions

        orders: list[dict[str, Any]] | None | Unset
        if isinstance(self.orders, Unset):
            orders = UNSET
        elif isinstance(self.orders, list):
            orders = []
            for orders_type_0_item_data in self.orders:
                orders_type_0_item = orders_type_0_item_data.to_dict()
                orders.append(orders_type_0_item)


        else:
            orders = self.orders


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if datetime_prev is not UNSET:
            field_dict["datetimePrev"] = datetime_prev
        if login is not UNSET:
            field_dict["login"] = login
        if name is not UNSET:
            field_dict["name"] = name
        if group is not UNSET:
            field_dict["group"] = group
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_digits is not UNSET:
            field_dict["currencyDigits"] = currency_digits
        if company is not UNSET:
            field_dict["company"] = company
        if e_mail is not UNSET:
            field_dict["eMail"] = e_mail
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if interest_rate is not UNSET:
            field_dict["interestRate"] = interest_rate
        if commission_daily is not UNSET:
            field_dict["commissionDaily"] = commission_daily
        if commission_monthly is not UNSET:
            field_dict["commissionMonthly"] = commission_monthly
        if agent_daily is not UNSET:
            field_dict["agentDaily"] = agent_daily
        if agent_monthly is not UNSET:
            field_dict["agentMonthly"] = agent_monthly
        if balance_prev_day is not UNSET:
            field_dict["balancePrevDay"] = balance_prev_day
        if balance_prev_month is not UNSET:
            field_dict["balancePrevMonth"] = balance_prev_month
        if equity_prev_day is not UNSET:
            field_dict["equityPrevDay"] = equity_prev_day
        if equity_prev_month is not UNSET:
            field_dict["equityPrevMonth"] = equity_prev_month
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
        if profit_storage is not UNSET:
            field_dict["profitStorage"] = profit_storage
        if profit_equity is not UNSET:
            field_dict["profitEquity"] = profit_equity
        if profit_assets is not UNSET:
            field_dict["profitAssets"] = profit_assets
        if profit_liabilities is not UNSET:
            field_dict["profitLiabilities"] = profit_liabilities
        if daily_profit is not UNSET:
            field_dict["dailyProfit"] = daily_profit
        if daily_balance is not UNSET:
            field_dict["dailyBalance"] = daily_balance
        if daily_credit is not UNSET:
            field_dict["dailyCredit"] = daily_credit
        if daily_charge is not UNSET:
            field_dict["dailyCharge"] = daily_charge
        if daily_correction is not UNSET:
            field_dict["dailyCorrection"] = daily_correction
        if daily_bonus is not UNSET:
            field_dict["dailyBonus"] = daily_bonus
        if daily_storage is not UNSET:
            field_dict["dailyStorage"] = daily_storage
        if daily_comm_instant is not UNSET:
            field_dict["dailyCommInstant"] = daily_comm_instant
        if daily_comm_round is not UNSET:
            field_dict["dailyCommRound"] = daily_comm_round
        if daily_comm_fee is not UNSET:
            field_dict["dailyCommFee"] = daily_comm_fee
        if daily_dividend is not UNSET:
            field_dict["dailyDividend"] = daily_dividend
        if daily_taxes is not UNSET:
            field_dict["dailyTaxes"] = daily_taxes
        if daily_so_compensation is not UNSET:
            field_dict["dailySOCompensation"] = daily_so_compensation
        if daily_so_compensation_credit is not UNSET:
            field_dict["dailySOCompensationCredit"] = daily_so_compensation_credit
        if daily_agent is not UNSET:
            field_dict["dailyAgent"] = daily_agent
        if daily_interest is not UNSET:
            field_dict["dailyInterest"] = daily_interest
        if positions is not UNSET:
            field_dict["positions"] = positions
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_order import MT5Order
        from ..models.mt5_position import MT5Position
        d = dict(src_dict)
        datetime_ = d.pop("datetime", UNSET)

        datetime_prev = d.pop("datetimePrev", UNSET)

        login = d.pop("login", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        currency_digits = d.pop("currencyDigits", UNSET)

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_e_mail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_mail = _parse_e_mail(d.pop("eMail", UNSET))


        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        commission_daily = d.pop("commissionDaily", UNSET)

        commission_monthly = d.pop("commissionMonthly", UNSET)

        agent_daily = d.pop("agentDaily", UNSET)

        agent_monthly = d.pop("agentMonthly", UNSET)

        balance_prev_day = d.pop("balancePrevDay", UNSET)

        balance_prev_month = d.pop("balancePrevMonth", UNSET)

        equity_prev_day = d.pop("equityPrevDay", UNSET)

        equity_prev_month = d.pop("equityPrevMonth", UNSET)

        margin = d.pop("margin", UNSET)

        margin_free = d.pop("marginFree", UNSET)

        margin_level = d.pop("marginLevel", UNSET)

        margin_leverage = d.pop("marginLeverage", UNSET)

        profit = d.pop("profit", UNSET)

        profit_storage = d.pop("profitStorage", UNSET)

        profit_equity = d.pop("profitEquity", UNSET)

        profit_assets = d.pop("profitAssets", UNSET)

        profit_liabilities = d.pop("profitLiabilities", UNSET)

        daily_profit = d.pop("dailyProfit", UNSET)

        daily_balance = d.pop("dailyBalance", UNSET)

        daily_credit = d.pop("dailyCredit", UNSET)

        daily_charge = d.pop("dailyCharge", UNSET)

        daily_correction = d.pop("dailyCorrection", UNSET)

        daily_bonus = d.pop("dailyBonus", UNSET)

        daily_storage = d.pop("dailyStorage", UNSET)

        daily_comm_instant = d.pop("dailyCommInstant", UNSET)

        daily_comm_round = d.pop("dailyCommRound", UNSET)

        daily_comm_fee = d.pop("dailyCommFee", UNSET)

        daily_dividend = d.pop("dailyDividend", UNSET)

        daily_taxes = d.pop("dailyTaxes", UNSET)

        daily_so_compensation = d.pop("dailySOCompensation", UNSET)

        daily_so_compensation_credit = d.pop("dailySOCompensationCredit", UNSET)

        daily_agent = d.pop("dailyAgent", UNSET)

        daily_interest = d.pop("dailyInterest", UNSET)

        def _parse_positions(data: object) -> list[MT5Position] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positions_type_0 = []
                _positions_type_0 = data
                for positions_type_0_item_data in (_positions_type_0):
                    positions_type_0_item = MT5Position.from_dict(positions_type_0_item_data)



                    positions_type_0.append(positions_type_0_item)

                return positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Position] | None | Unset, data)

        positions = _parse_positions(d.pop("positions", UNSET))


        def _parse_orders(data: object) -> list[MT5Order] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                orders_type_0 = []
                _orders_type_0 = data
                for orders_type_0_item_data in (_orders_type_0):
                    orders_type_0_item = MT5Order.from_dict(orders_type_0_item_data)



                    orders_type_0.append(orders_type_0_item)

                return orders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Order] | None | Unset, data)

        orders = _parse_orders(d.pop("orders", UNSET))


        mt5_daily = cls(
            datetime_=datetime_,
            datetime_prev=datetime_prev,
            login=login,
            name=name,
            group=group,
            currency=currency,
            currency_digits=currency_digits,
            company=company,
            e_mail=e_mail,
            balance=balance,
            credit=credit,
            interest_rate=interest_rate,
            commission_daily=commission_daily,
            commission_monthly=commission_monthly,
            agent_daily=agent_daily,
            agent_monthly=agent_monthly,
            balance_prev_day=balance_prev_day,
            balance_prev_month=balance_prev_month,
            equity_prev_day=equity_prev_day,
            equity_prev_month=equity_prev_month,
            margin=margin,
            margin_free=margin_free,
            margin_level=margin_level,
            margin_leverage=margin_leverage,
            profit=profit,
            profit_storage=profit_storage,
            profit_equity=profit_equity,
            profit_assets=profit_assets,
            profit_liabilities=profit_liabilities,
            daily_profit=daily_profit,
            daily_balance=daily_balance,
            daily_credit=daily_credit,
            daily_charge=daily_charge,
            daily_correction=daily_correction,
            daily_bonus=daily_bonus,
            daily_storage=daily_storage,
            daily_comm_instant=daily_comm_instant,
            daily_comm_round=daily_comm_round,
            daily_comm_fee=daily_comm_fee,
            daily_dividend=daily_dividend,
            daily_taxes=daily_taxes,
            daily_so_compensation=daily_so_compensation,
            daily_so_compensation_credit=daily_so_compensation_credit,
            daily_agent=daily_agent,
            daily_interest=daily_interest,
            positions=positions,
            orders=orders,
        )

        return mt5_daily

