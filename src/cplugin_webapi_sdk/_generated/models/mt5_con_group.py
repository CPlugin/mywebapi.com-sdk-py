from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_auth_mode import EnAuthMode
from ..models.en_auth_otp_mode import EnAuthOTPMode
from ..models.en_free_margin_mode import EnFreeMarginMode
from ..models.en_history_limit import EnHistoryLimit
from ..models.en_mail_mode import EnMailMode
from ..models.en_margin_mode import EnMarginMode
from ..models.en_news_mode import EnNewsMode
from ..models.en_reports_mode import EnReportsMode
from ..models.en_stop_out_mode import EnStopOutMode
from ..models.en_transfer_mode import EnTransferMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_con_group_commissions_type_0 import MT5ConGroupCommissionsType0





T = TypeVar("T", bound="MT5ConGroup")



@_attrs_define
class MT5ConGroup:
    """ 
        Attributes:
            group (None | str | Unset): group name
            server (int | None | Unset): group trade server ID
            permissions_flags (None | str | Unset): EnPermissionsFlags
            auth_mode (EnAuthMode | None | Unset): EnAuthMode
            auth_password_min (int | None | Unset): minimal password length
            company (None | str | Unset): company name
            company_page (None | str | Unset): company web page URL
            company_email (None | str | Unset): company email
            company_support_page (None | str | Unset): company support site URL
            company_support_email (None | str | Unset): company support email
            company_catalog (None | str | Unset): company catalog name (for reports and email templates)
            currency (None | str | Unset): deposit currency
            currency_digits (int | None | Unset):
            reports_mode (EnReportsMode | None | Unset): EnReportsMode
            reports_flags (None | str | Unset): EnReportsFlags
            reports_smtp (None | str | Unset): reports SMTP server address:ports
            reports_smtp_login (None | str | Unset): reports SMTP server login
            reports_smtp_pass (None | str | Unset): reports SMTP server password
            news_mode (EnNewsMode | None | Unset): EnNewsMode
            news_category (None | str | Unset): news category filter string
            news_lang (list[int] | None | Unset): <strong>Setter not yet implemented. If you want to send this value to MT5,
                ask vendor to implement this feature. Exception will be thrown if you send anything but null here.</strong>
                <br />
                <br />
                            allowed news languages (Windows API LANGID used)
            mail_mode (EnMailMode | None | Unset): EnMailMode
            trade_flags (None | str | Unset): EnTradeFlags
            trade_interest_rate (float | None | Unset): interest rate for free deposit money
            trade_virtual_credit (float | None | Unset): virtual credit
            margin_free_mode (EnFreeMarginMode | None | Unset): EnFreeMarginMode
            margin_so_mode (EnStopOutMode | None | Unset): EnStopOutMode
            margin_call (float | None | Unset): Margin Call level value
            margin_stop_out (float | None | Unset): Sto-Out level value
            demo_leverage (int | None | Unset): default demo accounts leverage
            demo_deposit (float | None | Unset): default demo accounts deposit
            limit_history (EnHistoryLimit | None | Unset): EnHistoryLimit
            limit_orders (int | None | Unset): max. order limit
            limit_symbols (int | None | Unset): max. selected symbols limit
            commissions (MT5ConGroupCommissionsType0 | None | Unset): /// <strong>Setter not yet implemented. If you want to
                send this value to MT5, ask vendor to implement this feature. Exception will be thrown if you send anything but
                null here.</strong><br /><br />
            margin_free_profit_mode (int | None | Unset): margin free profit accounting mode
            margin_mode (EnMarginMode | None | Unset): group risk management mode - EnMarginMode
            auth_otp_mode (EnAuthOTPMode | None | Unset): OTP authentication mode - EnAuthOTPMode
            trade_transfer_mode (EnTransferMode | None | Unset): deposit transfer mode - EnTransferMode
            margin_flags (None | str | Unset): margin calculation flags EnMarginFlags
            limit_positions (int | None | Unset): max. positions limit
            reports_email (None | str | Unset): reports SMTP email account
            company_deposit_page (None | str | Unset): company deposit URL
            company_withdrawal_page (None | str | Unset): company deposit URL
            demo_inactivity_period (int | None | Unset): demo groups in days, orders and positions will be deleted after
                this period
     """

    group: None | str | Unset = UNSET
    server: int | None | Unset = UNSET
    permissions_flags: None | str | Unset = UNSET
    auth_mode: EnAuthMode | None | Unset = UNSET
    auth_password_min: int | None | Unset = UNSET
    company: None | str | Unset = UNSET
    company_page: None | str | Unset = UNSET
    company_email: None | str | Unset = UNSET
    company_support_page: None | str | Unset = UNSET
    company_support_email: None | str | Unset = UNSET
    company_catalog: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    currency_digits: int | None | Unset = UNSET
    reports_mode: EnReportsMode | None | Unset = UNSET
    reports_flags: None | str | Unset = UNSET
    reports_smtp: None | str | Unset = UNSET
    reports_smtp_login: None | str | Unset = UNSET
    reports_smtp_pass: None | str | Unset = UNSET
    news_mode: EnNewsMode | None | Unset = UNSET
    news_category: None | str | Unset = UNSET
    news_lang: list[int] | None | Unset = UNSET
    mail_mode: EnMailMode | None | Unset = UNSET
    trade_flags: None | str | Unset = UNSET
    trade_interest_rate: float | None | Unset = UNSET
    trade_virtual_credit: float | None | Unset = UNSET
    margin_free_mode: EnFreeMarginMode | None | Unset = UNSET
    margin_so_mode: EnStopOutMode | None | Unset = UNSET
    margin_call: float | None | Unset = UNSET
    margin_stop_out: float | None | Unset = UNSET
    demo_leverage: int | None | Unset = UNSET
    demo_deposit: float | None | Unset = UNSET
    limit_history: EnHistoryLimit | None | Unset = UNSET
    limit_orders: int | None | Unset = UNSET
    limit_symbols: int | None | Unset = UNSET
    commissions: MT5ConGroupCommissionsType0 | None | Unset = UNSET
    margin_free_profit_mode: int | None | Unset = UNSET
    margin_mode: EnMarginMode | None | Unset = UNSET
    auth_otp_mode: EnAuthOTPMode | None | Unset = UNSET
    trade_transfer_mode: EnTransferMode | None | Unset = UNSET
    margin_flags: None | str | Unset = UNSET
    limit_positions: int | None | Unset = UNSET
    reports_email: None | str | Unset = UNSET
    company_deposit_page: None | str | Unset = UNSET
    company_withdrawal_page: None | str | Unset = UNSET
    demo_inactivity_period: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_con_group_commissions_type_0 import MT5ConGroupCommissionsType0
        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        server: int | None | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        permissions_flags: None | str | Unset
        if isinstance(self.permissions_flags, Unset):
            permissions_flags = UNSET
        else:
            permissions_flags = self.permissions_flags

        auth_mode: None | str | Unset
        if isinstance(self.auth_mode, Unset):
            auth_mode = UNSET
        elif isinstance(self.auth_mode, EnAuthMode):
            auth_mode = self.auth_mode.value
        else:
            auth_mode = self.auth_mode

        auth_password_min: int | None | Unset
        if isinstance(self.auth_password_min, Unset):
            auth_password_min = UNSET
        else:
            auth_password_min = self.auth_password_min

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        company_page: None | str | Unset
        if isinstance(self.company_page, Unset):
            company_page = UNSET
        else:
            company_page = self.company_page

        company_email: None | str | Unset
        if isinstance(self.company_email, Unset):
            company_email = UNSET
        else:
            company_email = self.company_email

        company_support_page: None | str | Unset
        if isinstance(self.company_support_page, Unset):
            company_support_page = UNSET
        else:
            company_support_page = self.company_support_page

        company_support_email: None | str | Unset
        if isinstance(self.company_support_email, Unset):
            company_support_email = UNSET
        else:
            company_support_email = self.company_support_email

        company_catalog: None | str | Unset
        if isinstance(self.company_catalog, Unset):
            company_catalog = UNSET
        else:
            company_catalog = self.company_catalog

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        currency_digits: int | None | Unset
        if isinstance(self.currency_digits, Unset):
            currency_digits = UNSET
        else:
            currency_digits = self.currency_digits

        reports_mode: None | str | Unset
        if isinstance(self.reports_mode, Unset):
            reports_mode = UNSET
        elif isinstance(self.reports_mode, EnReportsMode):
            reports_mode = self.reports_mode.value
        else:
            reports_mode = self.reports_mode

        reports_flags: None | str | Unset
        if isinstance(self.reports_flags, Unset):
            reports_flags = UNSET
        else:
            reports_flags = self.reports_flags

        reports_smtp: None | str | Unset
        if isinstance(self.reports_smtp, Unset):
            reports_smtp = UNSET
        else:
            reports_smtp = self.reports_smtp

        reports_smtp_login: None | str | Unset
        if isinstance(self.reports_smtp_login, Unset):
            reports_smtp_login = UNSET
        else:
            reports_smtp_login = self.reports_smtp_login

        reports_smtp_pass: None | str | Unset
        if isinstance(self.reports_smtp_pass, Unset):
            reports_smtp_pass = UNSET
        else:
            reports_smtp_pass = self.reports_smtp_pass

        news_mode: None | str | Unset
        if isinstance(self.news_mode, Unset):
            news_mode = UNSET
        elif isinstance(self.news_mode, EnNewsMode):
            news_mode = self.news_mode.value
        else:
            news_mode = self.news_mode

        news_category: None | str | Unset
        if isinstance(self.news_category, Unset):
            news_category = UNSET
        else:
            news_category = self.news_category

        news_lang: list[int] | None | Unset
        if isinstance(self.news_lang, Unset):
            news_lang = UNSET
        elif isinstance(self.news_lang, list):
            news_lang = self.news_lang


        else:
            news_lang = self.news_lang

        mail_mode: None | str | Unset
        if isinstance(self.mail_mode, Unset):
            mail_mode = UNSET
        elif isinstance(self.mail_mode, EnMailMode):
            mail_mode = self.mail_mode.value
        else:
            mail_mode = self.mail_mode

        trade_flags: None | str | Unset
        if isinstance(self.trade_flags, Unset):
            trade_flags = UNSET
        else:
            trade_flags = self.trade_flags

        trade_interest_rate: float | None | Unset
        if isinstance(self.trade_interest_rate, Unset):
            trade_interest_rate = UNSET
        else:
            trade_interest_rate = self.trade_interest_rate

        trade_virtual_credit: float | None | Unset
        if isinstance(self.trade_virtual_credit, Unset):
            trade_virtual_credit = UNSET
        else:
            trade_virtual_credit = self.trade_virtual_credit

        margin_free_mode: None | str | Unset
        if isinstance(self.margin_free_mode, Unset):
            margin_free_mode = UNSET
        elif isinstance(self.margin_free_mode, EnFreeMarginMode):
            margin_free_mode = self.margin_free_mode.value
        else:
            margin_free_mode = self.margin_free_mode

        margin_so_mode: None | str | Unset
        if isinstance(self.margin_so_mode, Unset):
            margin_so_mode = UNSET
        elif isinstance(self.margin_so_mode, EnStopOutMode):
            margin_so_mode = self.margin_so_mode.value
        else:
            margin_so_mode = self.margin_so_mode

        margin_call: float | None | Unset
        if isinstance(self.margin_call, Unset):
            margin_call = UNSET
        else:
            margin_call = self.margin_call

        margin_stop_out: float | None | Unset
        if isinstance(self.margin_stop_out, Unset):
            margin_stop_out = UNSET
        else:
            margin_stop_out = self.margin_stop_out

        demo_leverage: int | None | Unset
        if isinstance(self.demo_leverage, Unset):
            demo_leverage = UNSET
        else:
            demo_leverage = self.demo_leverage

        demo_deposit: float | None | Unset
        if isinstance(self.demo_deposit, Unset):
            demo_deposit = UNSET
        else:
            demo_deposit = self.demo_deposit

        limit_history: None | str | Unset
        if isinstance(self.limit_history, Unset):
            limit_history = UNSET
        elif isinstance(self.limit_history, EnHistoryLimit):
            limit_history = self.limit_history.value
        else:
            limit_history = self.limit_history

        limit_orders: int | None | Unset
        if isinstance(self.limit_orders, Unset):
            limit_orders = UNSET
        else:
            limit_orders = self.limit_orders

        limit_symbols: int | None | Unset
        if isinstance(self.limit_symbols, Unset):
            limit_symbols = UNSET
        else:
            limit_symbols = self.limit_symbols

        commissions: dict[str, Any] | None | Unset
        if isinstance(self.commissions, Unset):
            commissions = UNSET
        elif isinstance(self.commissions, MT5ConGroupCommissionsType0):
            commissions = self.commissions.to_dict()
        else:
            commissions = self.commissions

        margin_free_profit_mode: int | None | Unset
        if isinstance(self.margin_free_profit_mode, Unset):
            margin_free_profit_mode = UNSET
        else:
            margin_free_profit_mode = self.margin_free_profit_mode

        margin_mode: None | str | Unset
        if isinstance(self.margin_mode, Unset):
            margin_mode = UNSET
        elif isinstance(self.margin_mode, EnMarginMode):
            margin_mode = self.margin_mode.value
        else:
            margin_mode = self.margin_mode

        auth_otp_mode: None | str | Unset
        if isinstance(self.auth_otp_mode, Unset):
            auth_otp_mode = UNSET
        elif isinstance(self.auth_otp_mode, EnAuthOTPMode):
            auth_otp_mode = self.auth_otp_mode.value
        else:
            auth_otp_mode = self.auth_otp_mode

        trade_transfer_mode: None | str | Unset
        if isinstance(self.trade_transfer_mode, Unset):
            trade_transfer_mode = UNSET
        elif isinstance(self.trade_transfer_mode, EnTransferMode):
            trade_transfer_mode = self.trade_transfer_mode.value
        else:
            trade_transfer_mode = self.trade_transfer_mode

        margin_flags: None | str | Unset
        if isinstance(self.margin_flags, Unset):
            margin_flags = UNSET
        else:
            margin_flags = self.margin_flags

        limit_positions: int | None | Unset
        if isinstance(self.limit_positions, Unset):
            limit_positions = UNSET
        else:
            limit_positions = self.limit_positions

        reports_email: None | str | Unset
        if isinstance(self.reports_email, Unset):
            reports_email = UNSET
        else:
            reports_email = self.reports_email

        company_deposit_page: None | str | Unset
        if isinstance(self.company_deposit_page, Unset):
            company_deposit_page = UNSET
        else:
            company_deposit_page = self.company_deposit_page

        company_withdrawal_page: None | str | Unset
        if isinstance(self.company_withdrawal_page, Unset):
            company_withdrawal_page = UNSET
        else:
            company_withdrawal_page = self.company_withdrawal_page

        demo_inactivity_period: int | None | Unset
        if isinstance(self.demo_inactivity_period, Unset):
            demo_inactivity_period = UNSET
        else:
            demo_inactivity_period = self.demo_inactivity_period


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if server is not UNSET:
            field_dict["server"] = server
        if permissions_flags is not UNSET:
            field_dict["permissionsFlags"] = permissions_flags
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if auth_password_min is not UNSET:
            field_dict["authPasswordMin"] = auth_password_min
        if company is not UNSET:
            field_dict["company"] = company
        if company_page is not UNSET:
            field_dict["companyPage"] = company_page
        if company_email is not UNSET:
            field_dict["companyEmail"] = company_email
        if company_support_page is not UNSET:
            field_dict["companySupportPage"] = company_support_page
        if company_support_email is not UNSET:
            field_dict["companySupportEmail"] = company_support_email
        if company_catalog is not UNSET:
            field_dict["companyCatalog"] = company_catalog
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_digits is not UNSET:
            field_dict["currencyDigits"] = currency_digits
        if reports_mode is not UNSET:
            field_dict["reportsMode"] = reports_mode
        if reports_flags is not UNSET:
            field_dict["reportsFlags"] = reports_flags
        if reports_smtp is not UNSET:
            field_dict["reportsSMTP"] = reports_smtp
        if reports_smtp_login is not UNSET:
            field_dict["reportsSMTPLogin"] = reports_smtp_login
        if reports_smtp_pass is not UNSET:
            field_dict["reportsSMTPPass"] = reports_smtp_pass
        if news_mode is not UNSET:
            field_dict["newsMode"] = news_mode
        if news_category is not UNSET:
            field_dict["newsCategory"] = news_category
        if news_lang is not UNSET:
            field_dict["newsLang"] = news_lang
        if mail_mode is not UNSET:
            field_dict["mailMode"] = mail_mode
        if trade_flags is not UNSET:
            field_dict["tradeFlags"] = trade_flags
        if trade_interest_rate is not UNSET:
            field_dict["tradeInterestRate"] = trade_interest_rate
        if trade_virtual_credit is not UNSET:
            field_dict["tradeVirtualCredit"] = trade_virtual_credit
        if margin_free_mode is not UNSET:
            field_dict["marginFreeMode"] = margin_free_mode
        if margin_so_mode is not UNSET:
            field_dict["marginSOMode"] = margin_so_mode
        if margin_call is not UNSET:
            field_dict["marginCall"] = margin_call
        if margin_stop_out is not UNSET:
            field_dict["marginStopOut"] = margin_stop_out
        if demo_leverage is not UNSET:
            field_dict["demoLeverage"] = demo_leverage
        if demo_deposit is not UNSET:
            field_dict["demoDeposit"] = demo_deposit
        if limit_history is not UNSET:
            field_dict["limitHistory"] = limit_history
        if limit_orders is not UNSET:
            field_dict["limitOrders"] = limit_orders
        if limit_symbols is not UNSET:
            field_dict["limitSymbols"] = limit_symbols
        if commissions is not UNSET:
            field_dict["commissions"] = commissions
        if margin_free_profit_mode is not UNSET:
            field_dict["marginFreeProfitMode"] = margin_free_profit_mode
        if margin_mode is not UNSET:
            field_dict["marginMode"] = margin_mode
        if auth_otp_mode is not UNSET:
            field_dict["authOTPMode"] = auth_otp_mode
        if trade_transfer_mode is not UNSET:
            field_dict["tradeTransferMode"] = trade_transfer_mode
        if margin_flags is not UNSET:
            field_dict["marginFlags"] = margin_flags
        if limit_positions is not UNSET:
            field_dict["limitPositions"] = limit_positions
        if reports_email is not UNSET:
            field_dict["reportsEmail"] = reports_email
        if company_deposit_page is not UNSET:
            field_dict["companyDepositPage"] = company_deposit_page
        if company_withdrawal_page is not UNSET:
            field_dict["companyWithdrawalPage"] = company_withdrawal_page
        if demo_inactivity_period is not UNSET:
            field_dict["demoInactivityPeriod"] = demo_inactivity_period

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_con_group_commissions_type_0 import MT5ConGroupCommissionsType0
        d = dict(src_dict)
        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_server(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server = _parse_server(d.pop("server", UNSET))


        def _parse_permissions_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permissions_flags = _parse_permissions_flags(d.pop("permissionsFlags", UNSET))


        def _parse_auth_mode(data: object) -> EnAuthMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_mode_type_1 = EnAuthMode(data)



                return auth_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnAuthMode | None | Unset, data)

        auth_mode = _parse_auth_mode(d.pop("authMode", UNSET))


        def _parse_auth_password_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auth_password_min = _parse_auth_password_min(d.pop("authPasswordMin", UNSET))


        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_company_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_page = _parse_company_page(d.pop("companyPage", UNSET))


        def _parse_company_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_email = _parse_company_email(d.pop("companyEmail", UNSET))


        def _parse_company_support_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_support_page = _parse_company_support_page(d.pop("companySupportPage", UNSET))


        def _parse_company_support_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_support_email = _parse_company_support_email(d.pop("companySupportEmail", UNSET))


        def _parse_company_catalog(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_catalog = _parse_company_catalog(d.pop("companyCatalog", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_currency_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_digits = _parse_currency_digits(d.pop("currencyDigits", UNSET))


        def _parse_reports_mode(data: object) -> EnReportsMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reports_mode_type_1 = EnReportsMode(data)



                return reports_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnReportsMode | None | Unset, data)

        reports_mode = _parse_reports_mode(d.pop("reportsMode", UNSET))


        def _parse_reports_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_flags = _parse_reports_flags(d.pop("reportsFlags", UNSET))


        def _parse_reports_smtp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_smtp = _parse_reports_smtp(d.pop("reportsSMTP", UNSET))


        def _parse_reports_smtp_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_smtp_login = _parse_reports_smtp_login(d.pop("reportsSMTPLogin", UNSET))


        def _parse_reports_smtp_pass(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_smtp_pass = _parse_reports_smtp_pass(d.pop("reportsSMTPPass", UNSET))


        def _parse_news_mode(data: object) -> EnNewsMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                news_mode_type_1 = EnNewsMode(data)



                return news_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnNewsMode | None | Unset, data)

        news_mode = _parse_news_mode(d.pop("newsMode", UNSET))


        def _parse_news_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        news_category = _parse_news_category(d.pop("newsCategory", UNSET))


        def _parse_news_lang(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                news_lang_type_0 = cast(list[int], data)

                return news_lang_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        news_lang = _parse_news_lang(d.pop("newsLang", UNSET))


        def _parse_mail_mode(data: object) -> EnMailMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mail_mode_type_1 = EnMailMode(data)



                return mail_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnMailMode | None | Unset, data)

        mail_mode = _parse_mail_mode(d.pop("mailMode", UNSET))


        def _parse_trade_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_flags = _parse_trade_flags(d.pop("tradeFlags", UNSET))


        def _parse_trade_interest_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trade_interest_rate = _parse_trade_interest_rate(d.pop("tradeInterestRate", UNSET))


        def _parse_trade_virtual_credit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trade_virtual_credit = _parse_trade_virtual_credit(d.pop("tradeVirtualCredit", UNSET))


        def _parse_margin_free_mode(data: object) -> EnFreeMarginMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_free_mode_type_1 = EnFreeMarginMode(data)



                return margin_free_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnFreeMarginMode | None | Unset, data)

        margin_free_mode = _parse_margin_free_mode(d.pop("marginFreeMode", UNSET))


        def _parse_margin_so_mode(data: object) -> EnStopOutMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_so_mode_type_1 = EnStopOutMode(data)



                return margin_so_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnStopOutMode | None | Unset, data)

        margin_so_mode = _parse_margin_so_mode(d.pop("marginSOMode", UNSET))


        def _parse_margin_call(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_call = _parse_margin_call(d.pop("marginCall", UNSET))


        def _parse_margin_stop_out(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_stop_out = _parse_margin_stop_out(d.pop("marginStopOut", UNSET))


        def _parse_demo_leverage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        demo_leverage = _parse_demo_leverage(d.pop("demoLeverage", UNSET))


        def _parse_demo_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        demo_deposit = _parse_demo_deposit(d.pop("demoDeposit", UNSET))


        def _parse_limit_history(data: object) -> EnHistoryLimit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_history_type_1 = EnHistoryLimit(data)



                return limit_history_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnHistoryLimit | None | Unset, data)

        limit_history = _parse_limit_history(d.pop("limitHistory", UNSET))


        def _parse_limit_orders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit_orders = _parse_limit_orders(d.pop("limitOrders", UNSET))


        def _parse_limit_symbols(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit_symbols = _parse_limit_symbols(d.pop("limitSymbols", UNSET))


        def _parse_commissions(data: object) -> MT5ConGroupCommissionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commissions_type_0 = MT5ConGroupCommissionsType0.from_dict(data)



                return commissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5ConGroupCommissionsType0 | None | Unset, data)

        commissions = _parse_commissions(d.pop("commissions", UNSET))


        def _parse_margin_free_profit_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        margin_free_profit_mode = _parse_margin_free_profit_mode(d.pop("marginFreeProfitMode", UNSET))


        def _parse_margin_mode(data: object) -> EnMarginMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_mode_type_1 = EnMarginMode(data)



                return margin_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnMarginMode | None | Unset, data)

        margin_mode = _parse_margin_mode(d.pop("marginMode", UNSET))


        def _parse_auth_otp_mode(data: object) -> EnAuthOTPMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_otp_mode_type_1 = EnAuthOTPMode(data)



                return auth_otp_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnAuthOTPMode | None | Unset, data)

        auth_otp_mode = _parse_auth_otp_mode(d.pop("authOTPMode", UNSET))


        def _parse_trade_transfer_mode(data: object) -> EnTransferMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trade_transfer_mode_type_1 = EnTransferMode(data)



                return trade_transfer_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnTransferMode | None | Unset, data)

        trade_transfer_mode = _parse_trade_transfer_mode(d.pop("tradeTransferMode", UNSET))


        def _parse_margin_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        margin_flags = _parse_margin_flags(d.pop("marginFlags", UNSET))


        def _parse_limit_positions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit_positions = _parse_limit_positions(d.pop("limitPositions", UNSET))


        def _parse_reports_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_email = _parse_reports_email(d.pop("reportsEmail", UNSET))


        def _parse_company_deposit_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_deposit_page = _parse_company_deposit_page(d.pop("companyDepositPage", UNSET))


        def _parse_company_withdrawal_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_withdrawal_page = _parse_company_withdrawal_page(d.pop("companyWithdrawalPage", UNSET))


        def _parse_demo_inactivity_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        demo_inactivity_period = _parse_demo_inactivity_period(d.pop("demoInactivityPeriod", UNSET))


        mt5_con_group = cls(
            group=group,
            server=server,
            permissions_flags=permissions_flags,
            auth_mode=auth_mode,
            auth_password_min=auth_password_min,
            company=company,
            company_page=company_page,
            company_email=company_email,
            company_support_page=company_support_page,
            company_support_email=company_support_email,
            company_catalog=company_catalog,
            currency=currency,
            currency_digits=currency_digits,
            reports_mode=reports_mode,
            reports_flags=reports_flags,
            reports_smtp=reports_smtp,
            reports_smtp_login=reports_smtp_login,
            reports_smtp_pass=reports_smtp_pass,
            news_mode=news_mode,
            news_category=news_category,
            news_lang=news_lang,
            mail_mode=mail_mode,
            trade_flags=trade_flags,
            trade_interest_rate=trade_interest_rate,
            trade_virtual_credit=trade_virtual_credit,
            margin_free_mode=margin_free_mode,
            margin_so_mode=margin_so_mode,
            margin_call=margin_call,
            margin_stop_out=margin_stop_out,
            demo_leverage=demo_leverage,
            demo_deposit=demo_deposit,
            limit_history=limit_history,
            limit_orders=limit_orders,
            limit_symbols=limit_symbols,
            commissions=commissions,
            margin_free_profit_mode=margin_free_profit_mode,
            margin_mode=margin_mode,
            auth_otp_mode=auth_otp_mode,
            trade_transfer_mode=trade_transfer_mode,
            margin_flags=margin_flags,
            limit_positions=limit_positions,
            reports_email=reports_email,
            company_deposit_page=company_deposit_page,
            company_withdrawal_page=company_withdrawal_page,
            demo_inactivity_period=demo_inactivity_period,
        )

        return mt5_con_group

