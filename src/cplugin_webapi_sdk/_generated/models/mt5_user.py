from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5User")



@_attrs_define
class MT5User:
    """ MT5 user, v2 read DTO — full field set (A4 expansion). Includes all editable
                fields mirrored from MT5UserUpdate plus read-only financial/metadata fields.
                `Rights` is a flags string: the names of the set bits, `"Enabled, Password"`.

        Attributes:
            login (int | Unset): User login (identity, read-only).
            group (None | str | Unset): User group name.
            name (None | str | Unset): Full display name of the account holder.
            company (None | str | Unset): Company or organisation name.
            country (None | str | Unset): Client country.
            city (None | str | Unset): Client city.
            state (None | str | Unset): Client state or province.
            zip_code (None | str | Unset): Client postal code.
            phone (None | str | Unset): Client phone number.
            e_mail (None | str | Unset): Client email address.
            comment (None | str | Unset): Internal comment on the account.
            color (int | Unset): Colour tag assigned to the account in MT5 Manager (ARGB uint).
            leverage (int | Unset): Account leverage (e.g. 100 = 1:100).
            account (None | str | Unset): Account ID string (external account identifier).
            language (int | Unset): Client language code (MT5 locale uint).
            address (None | str | Unset): Client postal/physical address.
            id (None | str | Unset): Client document ID (passport, national ID, etc.).
            status (None | str | Unset): Client KYC / account status label.
            agent (int | Unset): Introducing agent login.
            lead_campaign (None | str | Unset): Marketing lead campaign name.
            lead_source (None | str | Unset): Marketing lead source name.
            client_id (int | Unset): External CRM client ID.
            first_name (None | str | Unset): Given name (first name).
            last_name (None | str | Unset): Family name (last name).
            middle_name (None | str | Unset): Patronymic / middle name.
            rights (str | Unset): MT5 user permission flags. Values mirror CIMTUser.EnUsersRights.<br/>Flags: names of the
                set bits joined by ", " ("Enabled, Password"), "None" when none is set; a set bit without a name is "Bit<n>"
                (bit number). Bits: Enabled = 0x1, Password = 0x2, TradeDisabled = 0x4, Investor = 0x8, Confirmed = 0x10,
                Trailing = 0x20, Expert = 0x40, Obsolete = 0x80, Reports = 0x100, Readonly = 0x200, ResetPass = 0x400,
                OTPEnabled = 0x800, SponsoredHosting = 0x2000, APIEnabled = 0x4000, PushNotification = 0x8000, Technical =
                0x10000, ExcludeReports = 0x20000. Example: Enabled, Password.
            cert_serial_number (int | Unset): SSL certificate serial number (read-only).
            registration (datetime.datetime | None | Unset): Account registration timestamp (UTC). Null when not set (unix
                0).
            last_access (datetime.datetime | None | Unset): Last login timestamp (UTC). Null when not set.
            last_pass_change (datetime.datetime | None | Unset): Last password change timestamp (UTC). Null when not set.
            last_ip (None | str | Unset): Last known client IP address.
            balance (float | Unset): Current account balance.
            credit (float | Unset): Current credit facility amount.
            interest_rate (float | Unset): Annual interest rate on credit.
            commission_daily (float | Unset): Accumulated commission for the current day.
            commission_monthly (float | Unset): Accumulated commission for the current month.
            commission_agent_daily (float | Unset): Agent commission accrued today.
            commission_agent_monthly (float | Unset): Agent commission accrued this month.
            balance_prev_day (float | Unset): Balance at end of previous trading day.
            balance_prev_month (float | Unset): Balance at end of previous calendar month.
            equity_prev_day (float | Unset): Equity at end of previous trading day.
            equity_prev_month (float | Unset): Equity at end of previous calendar month.
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    e_mail: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    color: int | Unset = UNSET
    leverage: int | Unset = UNSET
    account: None | str | Unset = UNSET
    language: int | Unset = UNSET
    address: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    agent: int | Unset = UNSET
    lead_campaign: None | str | Unset = UNSET
    lead_source: None | str | Unset = UNSET
    client_id: int | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    rights: str | Unset = UNSET
    cert_serial_number: int | Unset = UNSET
    registration: datetime.datetime | None | Unset = UNSET
    last_access: datetime.datetime | None | Unset = UNSET
    last_pass_change: datetime.datetime | None | Unset = UNSET
    last_ip: None | str | Unset = UNSET
    balance: float | Unset = UNSET
    credit: float | Unset = UNSET
    interest_rate: float | Unset = UNSET
    commission_daily: float | Unset = UNSET
    commission_monthly: float | Unset = UNSET
    commission_agent_daily: float | Unset = UNSET
    commission_agent_monthly: float | Unset = UNSET
    balance_prev_day: float | Unset = UNSET
    balance_prev_month: float | Unset = UNSET
    equity_prev_day: float | Unset = UNSET
    equity_prev_month: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        zip_code: None | str | Unset
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        e_mail: None | str | Unset
        if isinstance(self.e_mail, Unset):
            e_mail = UNSET
        else:
            e_mail = self.e_mail

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        color = self.color

        leverage = self.leverage

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        language = self.language

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        agent = self.agent

        lead_campaign: None | str | Unset
        if isinstance(self.lead_campaign, Unset):
            lead_campaign = UNSET
        else:
            lead_campaign = self.lead_campaign

        lead_source: None | str | Unset
        if isinstance(self.lead_source, Unset):
            lead_source = UNSET
        else:
            lead_source = self.lead_source

        client_id = self.client_id

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        rights = self.rights

        cert_serial_number = self.cert_serial_number

        registration: None | str | Unset
        if isinstance(self.registration, Unset):
            registration = UNSET
        elif isinstance(self.registration, datetime.datetime):
            registration = self.registration.isoformat()
        else:
            registration = self.registration

        last_access: None | str | Unset
        if isinstance(self.last_access, Unset):
            last_access = UNSET
        elif isinstance(self.last_access, datetime.datetime):
            last_access = self.last_access.isoformat()
        else:
            last_access = self.last_access

        last_pass_change: None | str | Unset
        if isinstance(self.last_pass_change, Unset):
            last_pass_change = UNSET
        elif isinstance(self.last_pass_change, datetime.datetime):
            last_pass_change = self.last_pass_change.isoformat()
        else:
            last_pass_change = self.last_pass_change

        last_ip: None | str | Unset
        if isinstance(self.last_ip, Unset):
            last_ip = UNSET
        else:
            last_ip = self.last_ip

        balance = self.balance

        credit = self.credit

        interest_rate = self.interest_rate

        commission_daily = self.commission_daily

        commission_monthly = self.commission_monthly

        commission_agent_daily = self.commission_agent_daily

        commission_agent_monthly = self.commission_agent_monthly

        balance_prev_day = self.balance_prev_day

        balance_prev_month = self.balance_prev_month

        equity_prev_day = self.equity_prev_day

        equity_prev_month = self.equity_prev_month


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if phone is not UNSET:
            field_dict["phone"] = phone
        if e_mail is not UNSET:
            field_dict["eMail"] = e_mail
        if comment is not UNSET:
            field_dict["comment"] = comment
        if color is not UNSET:
            field_dict["color"] = color
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if account is not UNSET:
            field_dict["account"] = account
        if language is not UNSET:
            field_dict["language"] = language
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if agent is not UNSET:
            field_dict["agent"] = agent
        if lead_campaign is not UNSET:
            field_dict["leadCampaign"] = lead_campaign
        if lead_source is not UNSET:
            field_dict["leadSource"] = lead_source
        if client_id is not UNSET:
            field_dict["clientID"] = client_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if rights is not UNSET:
            field_dict["rights"] = rights
        if cert_serial_number is not UNSET:
            field_dict["certSerialNumber"] = cert_serial_number
        if registration is not UNSET:
            field_dict["registration"] = registration
        if last_access is not UNSET:
            field_dict["lastAccess"] = last_access
        if last_pass_change is not UNSET:
            field_dict["lastPassChange"] = last_pass_change
        if last_ip is not UNSET:
            field_dict["lastIP"] = last_ip
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
        if commission_agent_daily is not UNSET:
            field_dict["commissionAgentDaily"] = commission_agent_daily
        if commission_agent_monthly is not UNSET:
            field_dict["commissionAgentMonthly"] = commission_agent_monthly
        if balance_prev_day is not UNSET:
            field_dict["balancePrevDay"] = balance_prev_day
        if balance_prev_month is not UNSET:
            field_dict["balancePrevMonth"] = balance_prev_month
        if equity_prev_day is not UNSET:
            field_dict["equityPrevDay"] = equity_prev_day
        if equity_prev_month is not UNSET:
            field_dict["equityPrevMonth"] = equity_prev_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_e_mail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_mail = _parse_e_mail(d.pop("eMail", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        color = d.pop("color", UNSET)

        leverage = d.pop("leverage", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))


        language = d.pop("language", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        agent = d.pop("agent", UNSET)

        def _parse_lead_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_campaign = _parse_lead_campaign(d.pop("leadCampaign", UNSET))


        def _parse_lead_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_source = _parse_lead_source(d.pop("leadSource", UNSET))


        client_id = d.pop("clientID", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))


        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))


        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))


        rights = d.pop("rights", UNSET)

        cert_serial_number = d.pop("certSerialNumber", UNSET)

        def _parse_registration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_type_0 = datetime.datetime.fromisoformat(data)



                return registration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        registration = _parse_registration(d.pop("registration", UNSET))


        def _parse_last_access(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_access_type_0 = datetime.datetime.fromisoformat(data)



                return last_access_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_access = _parse_last_access(d.pop("lastAccess", UNSET))


        def _parse_last_pass_change(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_pass_change_type_0 = datetime.datetime.fromisoformat(data)



                return last_pass_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_pass_change = _parse_last_pass_change(d.pop("lastPassChange", UNSET))


        def _parse_last_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_ip = _parse_last_ip(d.pop("lastIP", UNSET))


        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        commission_daily = d.pop("commissionDaily", UNSET)

        commission_monthly = d.pop("commissionMonthly", UNSET)

        commission_agent_daily = d.pop("commissionAgentDaily", UNSET)

        commission_agent_monthly = d.pop("commissionAgentMonthly", UNSET)

        balance_prev_day = d.pop("balancePrevDay", UNSET)

        balance_prev_month = d.pop("balancePrevMonth", UNSET)

        equity_prev_day = d.pop("equityPrevDay", UNSET)

        equity_prev_month = d.pop("equityPrevMonth", UNSET)

        mt5_user = cls(
            login=login,
            group=group,
            name=name,
            company=company,
            country=country,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
            e_mail=e_mail,
            comment=comment,
            color=color,
            leverage=leverage,
            account=account,
            language=language,
            address=address,
            id=id,
            status=status,
            agent=agent,
            lead_campaign=lead_campaign,
            lead_source=lead_source,
            client_id=client_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            rights=rights,
            cert_serial_number=cert_serial_number,
            registration=registration,
            last_access=last_access,
            last_pass_change=last_pass_change,
            last_ip=last_ip,
            balance=balance,
            credit=credit,
            interest_rate=interest_rate,
            commission_daily=commission_daily,
            commission_monthly=commission_monthly,
            commission_agent_daily=commission_agent_daily,
            commission_agent_monthly=commission_agent_monthly,
            balance_prev_day=balance_prev_day,
            balance_prev_month=balance_prev_month,
            equity_prev_day=equity_prev_day,
            equity_prev_month=equity_prev_month,
        )

        return mt5_user

