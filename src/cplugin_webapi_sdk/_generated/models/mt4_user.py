from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4User")



@_attrs_define
class MT4User:
    """ v2 DTO describing a trading account. Curated subset of the wrapper's
    `UserRecord` — exposes identity, contact, financial and flag fields
    that callers actually need.

    Deliberately omitted from v2 (vs v1's full UserRecord shape):
      * Password / PasswordInvestor / PasswordPhone / OtpSecret / ApiData /
        SecureReserved — credentials and secrets must never cross the v2
        boundary regardless of access level.
      * Unused / Reserved2 / EnableReserved / TimeStamp — wrapper bookkeeping
        with no caller-visible semantics.

    Account flags are exposed as a single CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4User.EnableFlags bitfield
    (the wrapper's native representation). Bit semantics are documented under
    that property — splitting it into separate booleans would hide the fact
    that MetaQuotes occasionally reuses bit positions across builds.

        Attributes:
            login (int | Unset): Trading account number (login)
            group (None | str | Unset): Group name the account belongs to
            name (None | str | Unset): Display name of the account holder
            registration_date (datetime.datetime | Unset): UTC timestamp when the account was created
            last_date (datetime.datetime | Unset): UTC timestamp of the last MT4 server interaction
            external_id (None | str | Unset): External customer identifier (e.g. CRM/KYC link). Wrapper's `Id` field.
            status (None | str | Unset): MT4-internal status string (e.g. live/demo state)
            country (None | str | Unset): Country (free text per broker's enrolment workflow)
            city (None | str | Unset): City
            state (None | str | Unset): State / region
            zip_code (None | str | Unset): Postal / ZIP code
            address (None | str | Unset): Street address
            lead_source (None | str | Unset): Lead source / referral channel tag
            phone (None | str | Unset): Contact phone
            email (None | str | Unset): Contact email
            comment (None | str | Unset): Free-form back-office comment
            leverage (int | Unset): Account leverage (e.g. 100 means 1:100)
            agent_account (int | Unset): IB / agent account number that referred this client
            last_ip (int | Unset): Last connection IP as raw int (use platform helpers to format)
            balance (float | Unset): Current balance
            credit (float | Unset): Credit on the account
            prev_month_balance (float | Unset): Balance at the start of the previous calendar month
            prev_balance (float | Unset): Balance at the previous reporting close
            prev_month_equity (float | Unset): Equity at the start of the previous calendar month
            prev_equity (float | Unset): Equity at the previous reporting close
            interest_rate (float | Unset): Interest rate (broker-defined, often used for swaps)
            taxes (float | Unset): Tax rate applied to the account
            enable_flags (int | Unset): Account flag bitfield (wrapper's `EnableFlags`). Documented bits:
                  * 0x01 = account enabled (login allowed)
                  * 0x02 = client may change password
                  * 0x04 = account is read-only (no trading)
                  * 0x08 = OTP enrolment required at login
                Bit positions reflect MT4 build 1455. Verify against the current MT4
                Manager docs if pinning behaviour to a specific bit.
            send_reports (int | Unset): 0 = no reports, non-zero = nightly email reports enabled
            mqid (int | Unset): MetaQuotes ID for mobile push notifications (0 if not linked).
                Typed as `long` in v2 even though current builds store it in
                32 bits — the wrapper exposes a wider underlying type and a checked
                narrowing cast would crash for accounts whose mqid sits above
                Int32.MaxValue. Future-proofs the contract against MQ widening.
            user_color (int | Unset): UI tint color in terminal client lists
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    registration_date: datetime.datetime | Unset = UNSET
    last_date: datetime.datetime | Unset = UNSET
    external_id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    lead_source: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    leverage: int | Unset = UNSET
    agent_account: int | Unset = UNSET
    last_ip: int | Unset = UNSET
    balance: float | Unset = UNSET
    credit: float | Unset = UNSET
    prev_month_balance: float | Unset = UNSET
    prev_balance: float | Unset = UNSET
    prev_month_equity: float | Unset = UNSET
    prev_equity: float | Unset = UNSET
    interest_rate: float | Unset = UNSET
    taxes: float | Unset = UNSET
    enable_flags: int | Unset = UNSET
    send_reports: int | Unset = UNSET
    mqid: int | Unset = UNSET
    user_color: int | Unset = UNSET





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

        registration_date: str | Unset = UNSET
        if not isinstance(self.registration_date, Unset):
            registration_date = self.registration_date.isoformat()

        last_date: str | Unset = UNSET
        if not isinstance(self.last_date, Unset):
            last_date = self.last_date.isoformat()

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        lead_source: None | str | Unset
        if isinstance(self.lead_source, Unset):
            lead_source = UNSET
        else:
            lead_source = self.lead_source

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        leverage = self.leverage

        agent_account = self.agent_account

        last_ip = self.last_ip

        balance = self.balance

        credit = self.credit

        prev_month_balance = self.prev_month_balance

        prev_balance = self.prev_balance

        prev_month_equity = self.prev_month_equity

        prev_equity = self.prev_equity

        interest_rate = self.interest_rate

        taxes = self.taxes

        enable_flags = self.enable_flags

        send_reports = self.send_reports

        mqid = self.mqid

        user_color = self.user_color


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group
        if name is not UNSET:
            field_dict["name"] = name
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if last_date is not UNSET:
            field_dict["lastDate"] = last_date
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if status is not UNSET:
            field_dict["status"] = status
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if address is not UNSET:
            field_dict["address"] = address
        if lead_source is not UNSET:
            field_dict["leadSource"] = lead_source
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if comment is not UNSET:
            field_dict["comment"] = comment
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if agent_account is not UNSET:
            field_dict["agentAccount"] = agent_account
        if last_ip is not UNSET:
            field_dict["lastIP"] = last_ip
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if prev_month_balance is not UNSET:
            field_dict["prevMonthBalance"] = prev_month_balance
        if prev_balance is not UNSET:
            field_dict["prevBalance"] = prev_balance
        if prev_month_equity is not UNSET:
            field_dict["prevMonthEquity"] = prev_month_equity
        if prev_equity is not UNSET:
            field_dict["prevEquity"] = prev_equity
        if interest_rate is not UNSET:
            field_dict["interestRate"] = interest_rate
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if enable_flags is not UNSET:
            field_dict["enableFlags"] = enable_flags
        if send_reports is not UNSET:
            field_dict["sendReports"] = send_reports
        if mqid is not UNSET:
            field_dict["mqid"] = mqid
        if user_color is not UNSET:
            field_dict["userColor"] = user_color

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


        _registration_date = d.pop("registrationDate", UNSET)
        registration_date: datetime.datetime | Unset
        if isinstance(_registration_date,  Unset):
            registration_date = UNSET
        else:
            registration_date = datetime.datetime.fromisoformat(_registration_date)




        _last_date = d.pop("lastDate", UNSET)
        last_date: datetime.datetime | Unset
        if isinstance(_last_date,  Unset):
            last_date = UNSET
        else:
            last_date = datetime.datetime.fromisoformat(_last_date)




        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


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


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_lead_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_source = _parse_lead_source(d.pop("leadSource", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        leverage = d.pop("leverage", UNSET)

        agent_account = d.pop("agentAccount", UNSET)

        last_ip = d.pop("lastIP", UNSET)

        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        prev_month_balance = d.pop("prevMonthBalance", UNSET)

        prev_balance = d.pop("prevBalance", UNSET)

        prev_month_equity = d.pop("prevMonthEquity", UNSET)

        prev_equity = d.pop("prevEquity", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        taxes = d.pop("taxes", UNSET)

        enable_flags = d.pop("enableFlags", UNSET)

        send_reports = d.pop("sendReports", UNSET)

        mqid = d.pop("mqid", UNSET)

        user_color = d.pop("userColor", UNSET)

        mt4_user = cls(
            login=login,
            group=group,
            name=name,
            registration_date=registration_date,
            last_date=last_date,
            external_id=external_id,
            status=status,
            country=country,
            city=city,
            state=state,
            zip_code=zip_code,
            address=address,
            lead_source=lead_source,
            phone=phone,
            email=email,
            comment=comment,
            leverage=leverage,
            agent_account=agent_account,
            last_ip=last_ip,
            balance=balance,
            credit=credit,
            prev_month_balance=prev_month_balance,
            prev_balance=prev_balance,
            prev_month_equity=prev_month_equity,
            prev_equity=prev_equity,
            interest_rate=interest_rate,
            taxes=taxes,
            enable_flags=enable_flags,
            send_reports=send_reports,
            mqid=mqid,
            user_color=user_color,
        )

        return mt4_user

