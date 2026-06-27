from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.group_rights import GroupRights
from ..models.margin_controlling_type import MarginControllingType
from ..models.margin_mode import MarginMode
from ..models.news_mode import NewsMode
from ..models.otp_mode import OTPMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Group")



@_attrs_define
class MT4Group:
    """ v2 DTO describing a trading group configuration. Curated subset of the
    wrapper's `ConGroup` — exposes the configuration fields that callers
    need to inspect margin/leverage/rights settings.

    Deliberately omitted from v2 (vs v1's full ConGroup shape):
      * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP
        credentials must never cross the v2 boundary regardless of access
        level. `SmtpServer` alone is dropped too because a server name
        is rarely useful without its credentials and exposes infra topology.
      * `Templates` — server-side filesystem path, irrelevant to API
        consumers and a minor information-disclosure risk.
      * `SecuritiesHash` — opaque byte[], wrapper bookkeeping.
      * `Reserved`, `UnusedRights`, `SecGroups[32]`,
        `SecMargins[128]` — reserved/internal arrays. The two nested
        arrays (SecGroups, SecMargins) deserve their own dedicated v2
        endpoints (`GroupSecGroupsGet/{group}`, `GroupSecMarginsGet/{group}`)
        planned for Wave 3 — including them here would balloon the DTO.
      * `NewsLanguages` (uint[]) and `NewsLanguagesTotal` —
        rarely consumed; can be added later once the use case is clear.

    Enums (`OTPMode`, `MarginMode`, `NewsMode`,
    `GroupRights`, `MarginControllingType`) serialize as strings
    because CPlugin.SaaSWebApps.WebAPI.Code.Json.V2JsonContext enables
    `UseStringEnumConverter`.

        Attributes:
            group (None | str | Unset): Group name (unique per platform, max 16 chars)
            enable (int | Unset): 0 = group disabled, non-zero = enabled (accounts in this group can log in)
            timeout (int | Unset): Trade confirmation timeout, seconds
            otp_mode (OTPMode | Unset):
            company (None | str | Unset): Company name shown on statements
            signature (None | str | Unset): Statement signature line
            support_page (None | str | Unset): Support page URL shown to clients
            support_email (None | str | Unset): Support email shown to clients
            copies (int | Unset): Number of statement copies sent to support address
            reports (int | Unset): 0 = statements disabled, non-zero = nightly statements enabled
            default_leverage (int | Unset): Default leverage applied when an account omits its own leverage
            default_deposit (float | Unset): Default deposit applied when an account omits its own balance
            max_securities (int | Unset): Max simultaneously open securities
            sec_margins_total (int | Unset): Count of special securities settings (SecMargins) in use
            currency (None | str | Unset): Deposit currency (e.g. "USD")
            credit (float | Unset): Virtual credit applied to the group's accounts
            margin_call (int | Unset): Margin call threshold (percent of equity)
            margin_mode (MarginMode | Unset):
            margin_stopout (int | Unset): Stop-out threshold
            interest_rate (float | Unset): Annual interest rate (percent)
            use_swap (int | Unset): 0 = no rollovers, non-zero = use rollovers and interest rate
            news_mode (NewsMode | Unset):
            group_rights (GroupRights | Unset):
            check_ie_prices (int | Unset): 0 = no IE check, non-zero = check Instant Execution prices
            max_positions (int | Unset): Maximum simultaneous orders and open positions
            close_reopen (int | Unset): 0 = standard close, non-zero = close-and-reopen mode
            hedge_prohibited (int | Unset): 0 = hedging allowed, non-zero = hedging prohibited
            close_fifo (int | Unset): 0 = LIFO, non-zero = FIFO close rule
            hedge_large_leg (int | Unset): 0 = standard hedge, non-zero = treat large hedged leg specially
            margin_controlling_type (MarginControllingType | Unset):
            archive_period (int | Unset): Inactivity period (days) before account moves to archive
            archive_max_balance (int | Unset): Maximum balance under which an account is eligible for archiving
            stopout_skip_hedged (int | Unset): 0 = include hedged accounts in stop-out checks, non-zero = skip them
            archive_pending_period (int | Unset): Pending orders clean-up period (days)
     """

    group: None | str | Unset = UNSET
    enable: int | Unset = UNSET
    timeout: int | Unset = UNSET
    otp_mode: OTPMode | Unset = UNSET
    company: None | str | Unset = UNSET
    signature: None | str | Unset = UNSET
    support_page: None | str | Unset = UNSET
    support_email: None | str | Unset = UNSET
    copies: int | Unset = UNSET
    reports: int | Unset = UNSET
    default_leverage: int | Unset = UNSET
    default_deposit: float | Unset = UNSET
    max_securities: int | Unset = UNSET
    sec_margins_total: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    credit: float | Unset = UNSET
    margin_call: int | Unset = UNSET
    margin_mode: MarginMode | Unset = UNSET
    margin_stopout: int | Unset = UNSET
    interest_rate: float | Unset = UNSET
    use_swap: int | Unset = UNSET
    news_mode: NewsMode | Unset = UNSET
    group_rights: GroupRights | Unset = UNSET
    check_ie_prices: int | Unset = UNSET
    max_positions: int | Unset = UNSET
    close_reopen: int | Unset = UNSET
    hedge_prohibited: int | Unset = UNSET
    close_fifo: int | Unset = UNSET
    hedge_large_leg: int | Unset = UNSET
    margin_controlling_type: MarginControllingType | Unset = UNSET
    archive_period: int | Unset = UNSET
    archive_max_balance: int | Unset = UNSET
    stopout_skip_hedged: int | Unset = UNSET
    archive_pending_period: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        enable = self.enable

        timeout = self.timeout

        otp_mode: str | Unset = UNSET
        if not isinstance(self.otp_mode, Unset):
            otp_mode = self.otp_mode.value


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

        copies = self.copies

        reports = self.reports

        default_leverage = self.default_leverage

        default_deposit = self.default_deposit

        max_securities = self.max_securities

        sec_margins_total = self.sec_margins_total

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        credit = self.credit

        margin_call = self.margin_call

        margin_mode: str | Unset = UNSET
        if not isinstance(self.margin_mode, Unset):
            margin_mode = self.margin_mode.value


        margin_stopout = self.margin_stopout

        interest_rate = self.interest_rate

        use_swap = self.use_swap

        news_mode: str | Unset = UNSET
        if not isinstance(self.news_mode, Unset):
            news_mode = self.news_mode.value


        group_rights: str | Unset = UNSET
        if not isinstance(self.group_rights, Unset):
            group_rights = self.group_rights.value


        check_ie_prices = self.check_ie_prices

        max_positions = self.max_positions

        close_reopen = self.close_reopen

        hedge_prohibited = self.hedge_prohibited

        close_fifo = self.close_fifo

        hedge_large_leg = self.hedge_large_leg

        margin_controlling_type: str | Unset = UNSET
        if not isinstance(self.margin_controlling_type, Unset):
            margin_controlling_type = self.margin_controlling_type.value


        archive_period = self.archive_period

        archive_max_balance = self.archive_max_balance

        stopout_skip_hedged = self.stopout_skip_hedged

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
        if sec_margins_total is not UNSET:
            field_dict["secMarginsTotal"] = sec_margins_total
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


        enable = d.pop("enable", UNSET)

        timeout = d.pop("timeout", UNSET)

        _otp_mode = d.pop("otpMode", UNSET)
        otp_mode: OTPMode | Unset
        if isinstance(_otp_mode,  Unset):
            otp_mode = UNSET
        else:
            otp_mode = OTPMode(_otp_mode)




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


        copies = d.pop("copies", UNSET)

        reports = d.pop("reports", UNSET)

        default_leverage = d.pop("defaultLeverage", UNSET)

        default_deposit = d.pop("defaultDeposit", UNSET)

        max_securities = d.pop("maxSecurities", UNSET)

        sec_margins_total = d.pop("secMarginsTotal", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        credit = d.pop("credit", UNSET)

        margin_call = d.pop("marginCall", UNSET)

        _margin_mode = d.pop("marginMode", UNSET)
        margin_mode: MarginMode | Unset
        if isinstance(_margin_mode,  Unset):
            margin_mode = UNSET
        else:
            margin_mode = MarginMode(_margin_mode)




        margin_stopout = d.pop("marginStopout", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        use_swap = d.pop("useSwap", UNSET)

        _news_mode = d.pop("newsMode", UNSET)
        news_mode: NewsMode | Unset
        if isinstance(_news_mode,  Unset):
            news_mode = UNSET
        else:
            news_mode = NewsMode(_news_mode)




        _group_rights = d.pop("groupRights", UNSET)
        group_rights: GroupRights | Unset
        if isinstance(_group_rights,  Unset):
            group_rights = UNSET
        else:
            group_rights = GroupRights(_group_rights)




        check_ie_prices = d.pop("checkIEPrices", UNSET)

        max_positions = d.pop("maxPositions", UNSET)

        close_reopen = d.pop("closeReopen", UNSET)

        hedge_prohibited = d.pop("hedgeProhibited", UNSET)

        close_fifo = d.pop("closeFIFO", UNSET)

        hedge_large_leg = d.pop("hedgeLargeLeg", UNSET)

        _margin_controlling_type = d.pop("marginControllingType", UNSET)
        margin_controlling_type: MarginControllingType | Unset
        if isinstance(_margin_controlling_type,  Unset):
            margin_controlling_type = UNSET
        else:
            margin_controlling_type = MarginControllingType(_margin_controlling_type)




        archive_period = d.pop("archivePeriod", UNSET)

        archive_max_balance = d.pop("archiveMaxBalance", UNSET)

        stopout_skip_hedged = d.pop("stopoutSkipHedged", UNSET)

        archive_pending_period = d.pop("archivePendingPeriod", UNSET)

        mt4_group = cls(
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
            sec_margins_total=sec_margins_total,
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

        return mt4_group

