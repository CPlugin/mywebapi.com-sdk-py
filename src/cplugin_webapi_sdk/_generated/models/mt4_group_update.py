from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.margin_controlling_type import MarginControllingType
from ..models.margin_mode import MarginMode
from ..models.news_mode import NewsMode
from ..models.otp_mode import OTPMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GroupUpdate")



@_attrs_define
class MT4GroupUpdate:
    """ Input shape for `CfgUpdateGroup`: the editable part of an MT4 trading group.

        Attributes:
            group (None | str | Unset): Group name to update (required identity; never changed by this call)
            enable (int | None | Unset): 0 = group disabled, non-zero = enabled
            timeout (int | None | Unset): Trade confirmation timeout, seconds
            otp_mode (None | OTPMode | Unset): One-time password requirement mode
            company (None | str | Unset): Company name shown on statements
            signature (None | str | Unset): Statement signature line
            support_page (None | str | Unset): Support page URL
            support_email (None | str | Unset): Support email
            copies (int | None | Unset): Statement copy count
            reports (int | None | Unset): 0 = statements disabled, non-zero = enabled
            default_leverage (int | None | Unset): Default leverage when accounts omit their own
            default_deposit (float | None | Unset): Default deposit when accounts omit their own balance
            max_securities (int | None | Unset): Max simultaneously open securities
            currency (None | str | Unset): Deposit currency
            credit (float | None | Unset): Virtual credit applied to group's accounts
            margin_call (int | None | Unset): Margin call threshold (percent)
            margin_mode (MarginMode | None | Unset): Margin calculation mode
            margin_stopout (int | None | Unset): Stop-out threshold
            interest_rate (float | None | Unset): Annual interest rate (percent)
            use_swap (int | None | Unset): 0 = no rollovers, non-zero = use them
            news_mode (NewsMode | None | Unset): News delivery mode
            group_rights (None | str | Unset): Permissions bit mask
            check_ie_prices (int | None | Unset): 0 = no IE check, non-zero = check IE prices
            max_positions (int | None | Unset): Maximum simultaneous orders and open positions
            close_reopen (int | None | Unset): 0 = standard, non-zero = close-and-reopen mode
            hedge_prohibited (int | None | Unset): 0 = hedging allowed, non-zero = prohibited
            close_fifo (int | None | Unset): 0 = LIFO, non-zero = FIFO close rule
            hedge_large_leg (int | None | Unset): 0 = standard, non-zero = treat large hedged leg specially
            margin_controlling_type (MarginControllingType | None | Unset): Margin controlling unit (percent vs deposit
                currency)
            archive_period (int | None | Unset): Inactivity period (days) before account archival
            archive_max_balance (int | None | Unset): Max balance under which an account becomes archivable
            stopout_skip_hedged (int | None | Unset): 0 = include hedged in stop-out checks, non-zero = skip them
            archive_pending_period (int | None | Unset): Pending orders clean-up period (days)
     """

    group: None | str | Unset = UNSET
    enable: int | None | Unset = UNSET
    timeout: int | None | Unset = UNSET
    otp_mode: None | OTPMode | Unset = UNSET
    company: None | str | Unset = UNSET
    signature: None | str | Unset = UNSET
    support_page: None | str | Unset = UNSET
    support_email: None | str | Unset = UNSET
    copies: int | None | Unset = UNSET
    reports: int | None | Unset = UNSET
    default_leverage: int | None | Unset = UNSET
    default_deposit: float | None | Unset = UNSET
    max_securities: int | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    credit: float | None | Unset = UNSET
    margin_call: int | None | Unset = UNSET
    margin_mode: MarginMode | None | Unset = UNSET
    margin_stopout: int | None | Unset = UNSET
    interest_rate: float | None | Unset = UNSET
    use_swap: int | None | Unset = UNSET
    news_mode: NewsMode | None | Unset = UNSET
    group_rights: None | str | Unset = UNSET
    check_ie_prices: int | None | Unset = UNSET
    max_positions: int | None | Unset = UNSET
    close_reopen: int | None | Unset = UNSET
    hedge_prohibited: int | None | Unset = UNSET
    close_fifo: int | None | Unset = UNSET
    hedge_large_leg: int | None | Unset = UNSET
    margin_controlling_type: MarginControllingType | None | Unset = UNSET
    archive_period: int | None | Unset = UNSET
    archive_max_balance: int | None | Unset = UNSET
    stopout_skip_hedged: int | None | Unset = UNSET
    archive_pending_period: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        enable: int | None | Unset
        if isinstance(self.enable, Unset):
            enable = UNSET
        else:
            enable = self.enable

        timeout: int | None | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        otp_mode: None | str | Unset
        if isinstance(self.otp_mode, Unset):
            otp_mode = UNSET
        elif isinstance(self.otp_mode, OTPMode):
            otp_mode = self.otp_mode.value
        else:
            otp_mode = self.otp_mode

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        signature: None | str | Unset
        if isinstance(self.signature, Unset):
            signature = UNSET
        else:
            signature = self.signature

        support_page: None | str | Unset
        if isinstance(self.support_page, Unset):
            support_page = UNSET
        else:
            support_page = self.support_page

        support_email: None | str | Unset
        if isinstance(self.support_email, Unset):
            support_email = UNSET
        else:
            support_email = self.support_email

        copies: int | None | Unset
        if isinstance(self.copies, Unset):
            copies = UNSET
        else:
            copies = self.copies

        reports: int | None | Unset
        if isinstance(self.reports, Unset):
            reports = UNSET
        else:
            reports = self.reports

        default_leverage: int | None | Unset
        if isinstance(self.default_leverage, Unset):
            default_leverage = UNSET
        else:
            default_leverage = self.default_leverage

        default_deposit: float | None | Unset
        if isinstance(self.default_deposit, Unset):
            default_deposit = UNSET
        else:
            default_deposit = self.default_deposit

        max_securities: int | None | Unset
        if isinstance(self.max_securities, Unset):
            max_securities = UNSET
        else:
            max_securities = self.max_securities

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        credit: float | None | Unset
        if isinstance(self.credit, Unset):
            credit = UNSET
        else:
            credit = self.credit

        margin_call: int | None | Unset
        if isinstance(self.margin_call, Unset):
            margin_call = UNSET
        else:
            margin_call = self.margin_call

        margin_mode: None | str | Unset
        if isinstance(self.margin_mode, Unset):
            margin_mode = UNSET
        elif isinstance(self.margin_mode, MarginMode):
            margin_mode = self.margin_mode.value
        else:
            margin_mode = self.margin_mode

        margin_stopout: int | None | Unset
        if isinstance(self.margin_stopout, Unset):
            margin_stopout = UNSET
        else:
            margin_stopout = self.margin_stopout

        interest_rate: float | None | Unset
        if isinstance(self.interest_rate, Unset):
            interest_rate = UNSET
        else:
            interest_rate = self.interest_rate

        use_swap: int | None | Unset
        if isinstance(self.use_swap, Unset):
            use_swap = UNSET
        else:
            use_swap = self.use_swap

        news_mode: None | str | Unset
        if isinstance(self.news_mode, Unset):
            news_mode = UNSET
        elif isinstance(self.news_mode, NewsMode):
            news_mode = self.news_mode.value
        else:
            news_mode = self.news_mode

        group_rights: None | str | Unset
        if isinstance(self.group_rights, Unset):
            group_rights = UNSET
        else:
            group_rights = self.group_rights

        check_ie_prices: int | None | Unset
        if isinstance(self.check_ie_prices, Unset):
            check_ie_prices = UNSET
        else:
            check_ie_prices = self.check_ie_prices

        max_positions: int | None | Unset
        if isinstance(self.max_positions, Unset):
            max_positions = UNSET
        else:
            max_positions = self.max_positions

        close_reopen: int | None | Unset
        if isinstance(self.close_reopen, Unset):
            close_reopen = UNSET
        else:
            close_reopen = self.close_reopen

        hedge_prohibited: int | None | Unset
        if isinstance(self.hedge_prohibited, Unset):
            hedge_prohibited = UNSET
        else:
            hedge_prohibited = self.hedge_prohibited

        close_fifo: int | None | Unset
        if isinstance(self.close_fifo, Unset):
            close_fifo = UNSET
        else:
            close_fifo = self.close_fifo

        hedge_large_leg: int | None | Unset
        if isinstance(self.hedge_large_leg, Unset):
            hedge_large_leg = UNSET
        else:
            hedge_large_leg = self.hedge_large_leg

        margin_controlling_type: None | str | Unset
        if isinstance(self.margin_controlling_type, Unset):
            margin_controlling_type = UNSET
        elif isinstance(self.margin_controlling_type, MarginControllingType):
            margin_controlling_type = self.margin_controlling_type.value
        else:
            margin_controlling_type = self.margin_controlling_type

        archive_period: int | None | Unset
        if isinstance(self.archive_period, Unset):
            archive_period = UNSET
        else:
            archive_period = self.archive_period

        archive_max_balance: int | None | Unset
        if isinstance(self.archive_max_balance, Unset):
            archive_max_balance = UNSET
        else:
            archive_max_balance = self.archive_max_balance

        stopout_skip_hedged: int | None | Unset
        if isinstance(self.stopout_skip_hedged, Unset):
            stopout_skip_hedged = UNSET
        else:
            stopout_skip_hedged = self.stopout_skip_hedged

        archive_pending_period: int | None | Unset
        if isinstance(self.archive_pending_period, Unset):
            archive_pending_period = UNSET
        else:
            archive_pending_period = self.archive_pending_period


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if enable is not UNSET:
            field_dict["enable"] = enable
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if otp_mode is not UNSET:
            field_dict["otpMode"] = otp_mode
        if company is not UNSET:
            field_dict["company"] = company
        if signature is not UNSET:
            field_dict["signature"] = signature
        if support_page is not UNSET:
            field_dict["supportPage"] = support_page
        if support_email is not UNSET:
            field_dict["supportEmail"] = support_email
        if copies is not UNSET:
            field_dict["copies"] = copies
        if reports is not UNSET:
            field_dict["reports"] = reports
        if default_leverage is not UNSET:
            field_dict["defaultLeverage"] = default_leverage
        if default_deposit is not UNSET:
            field_dict["defaultDeposit"] = default_deposit
        if max_securities is not UNSET:
            field_dict["maxSecurities"] = max_securities
        if currency is not UNSET:
            field_dict["currency"] = currency
        if credit is not UNSET:
            field_dict["credit"] = credit
        if margin_call is not UNSET:
            field_dict["marginCall"] = margin_call
        if margin_mode is not UNSET:
            field_dict["marginMode"] = margin_mode
        if margin_stopout is not UNSET:
            field_dict["marginStopout"] = margin_stopout
        if interest_rate is not UNSET:
            field_dict["interestRate"] = interest_rate
        if use_swap is not UNSET:
            field_dict["useSwap"] = use_swap
        if news_mode is not UNSET:
            field_dict["newsMode"] = news_mode
        if group_rights is not UNSET:
            field_dict["groupRights"] = group_rights
        if check_ie_prices is not UNSET:
            field_dict["checkIEPrices"] = check_ie_prices
        if max_positions is not UNSET:
            field_dict["maxPositions"] = max_positions
        if close_reopen is not UNSET:
            field_dict["closeReopen"] = close_reopen
        if hedge_prohibited is not UNSET:
            field_dict["hedgeProhibited"] = hedge_prohibited
        if close_fifo is not UNSET:
            field_dict["closeFIFO"] = close_fifo
        if hedge_large_leg is not UNSET:
            field_dict["hedgeLargeLeg"] = hedge_large_leg
        if margin_controlling_type is not UNSET:
            field_dict["marginControllingType"] = margin_controlling_type
        if archive_period is not UNSET:
            field_dict["archivePeriod"] = archive_period
        if archive_max_balance is not UNSET:
            field_dict["archiveMaxBalance"] = archive_max_balance
        if stopout_skip_hedged is not UNSET:
            field_dict["stopoutSkipHedged"] = stopout_skip_hedged
        if archive_pending_period is not UNSET:
            field_dict["archivePendingPeriod"] = archive_pending_period

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_enable(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        enable = _parse_enable(d.pop("enable", UNSET))


        def _parse_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))


        def _parse_otp_mode(data: object) -> None | OTPMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                otp_mode_type_1 = OTPMode(data)



                return otp_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OTPMode | Unset, data)

        otp_mode = _parse_otp_mode(d.pop("otpMode", UNSET))


        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_signature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature = _parse_signature(d.pop("signature", UNSET))


        def _parse_support_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_page = _parse_support_page(d.pop("supportPage", UNSET))


        def _parse_support_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_email = _parse_support_email(d.pop("supportEmail", UNSET))


        def _parse_copies(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        copies = _parse_copies(d.pop("copies", UNSET))


        def _parse_reports(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reports = _parse_reports(d.pop("reports", UNSET))


        def _parse_default_leverage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_leverage = _parse_default_leverage(d.pop("defaultLeverage", UNSET))


        def _parse_default_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_deposit = _parse_default_deposit(d.pop("defaultDeposit", UNSET))


        def _parse_max_securities(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_securities = _parse_max_securities(d.pop("maxSecurities", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_credit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credit = _parse_credit(d.pop("credit", UNSET))


        def _parse_margin_call(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        margin_call = _parse_margin_call(d.pop("marginCall", UNSET))


        def _parse_margin_mode(data: object) -> MarginMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_mode_type_1 = MarginMode(data)



                return margin_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarginMode | None | Unset, data)

        margin_mode = _parse_margin_mode(d.pop("marginMode", UNSET))


        def _parse_margin_stopout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        margin_stopout = _parse_margin_stopout(d.pop("marginStopout", UNSET))


        def _parse_interest_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        interest_rate = _parse_interest_rate(d.pop("interestRate", UNSET))


        def _parse_use_swap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        use_swap = _parse_use_swap(d.pop("useSwap", UNSET))


        def _parse_news_mode(data: object) -> NewsMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                news_mode_type_1 = NewsMode(data)



                return news_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewsMode | None | Unset, data)

        news_mode = _parse_news_mode(d.pop("newsMode", UNSET))


        def _parse_group_rights(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_rights = _parse_group_rights(d.pop("groupRights", UNSET))


        def _parse_check_ie_prices(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_ie_prices = _parse_check_ie_prices(d.pop("checkIEPrices", UNSET))


        def _parse_max_positions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_positions = _parse_max_positions(d.pop("maxPositions", UNSET))


        def _parse_close_reopen(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        close_reopen = _parse_close_reopen(d.pop("closeReopen", UNSET))


        def _parse_hedge_prohibited(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hedge_prohibited = _parse_hedge_prohibited(d.pop("hedgeProhibited", UNSET))


        def _parse_close_fifo(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        close_fifo = _parse_close_fifo(d.pop("closeFIFO", UNSET))


        def _parse_hedge_large_leg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hedge_large_leg = _parse_hedge_large_leg(d.pop("hedgeLargeLeg", UNSET))


        def _parse_margin_controlling_type(data: object) -> MarginControllingType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_controlling_type_type_1 = MarginControllingType(data)



                return margin_controlling_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarginControllingType | None | Unset, data)

        margin_controlling_type = _parse_margin_controlling_type(d.pop("marginControllingType", UNSET))


        def _parse_archive_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_period = _parse_archive_period(d.pop("archivePeriod", UNSET))


        def _parse_archive_max_balance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_max_balance = _parse_archive_max_balance(d.pop("archiveMaxBalance", UNSET))


        def _parse_stopout_skip_hedged(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stopout_skip_hedged = _parse_stopout_skip_hedged(d.pop("stopoutSkipHedged", UNSET))


        def _parse_archive_pending_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_pending_period = _parse_archive_pending_period(d.pop("archivePendingPeriod", UNSET))


        mt4_group_update = cls(
            group=group,
            enable=enable,
            timeout=timeout,
            otp_mode=otp_mode,
            company=company,
            signature=signature,
            support_page=support_page,
            support_email=support_email,
            copies=copies,
            reports=reports,
            default_leverage=default_leverage,
            default_deposit=default_deposit,
            max_securities=max_securities,
            currency=currency,
            credit=credit,
            margin_call=margin_call,
            margin_mode=margin_mode,
            margin_stopout=margin_stopout,
            interest_rate=interest_rate,
            use_swap=use_swap,
            news_mode=news_mode,
            group_rights=group_rights,
            check_ie_prices=check_ie_prices,
            max_positions=max_positions,
            close_reopen=close_reopen,
            hedge_prohibited=hedge_prohibited,
            close_fifo=close_fifo,
            hedge_large_leg=hedge_large_leg,
            margin_controlling_type=margin_controlling_type,
            archive_period=archive_period,
            archive_max_balance=archive_max_balance,
            stopout_skip_hedged=stopout_skip_hedged,
            archive_pending_period=archive_pending_period,
        )

        return mt4_group_update

