from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4UserUpdate")



@_attrs_define
class MT4UserUpdate:
    """ Input shape for `UserRecordUpdate`: the editable part of an MT4 account record.

        Attributes:
            login (int | Unset): Login of the account to update (required identity; never changed by this call)
            group (None | str | Unset): Group name the account belongs to
            name (None | str | Unset): Display name of the account holder
            external_id (None | str | Unset): External customer identifier (CRM/KYC link)
            status (None | str | Unset): MT4-internal status string
            country (None | str | Unset): Country
            city (None | str | Unset): City
            state (None | str | Unset): State / region
            zip_code (None | str | Unset): Postal / ZIP code
            address (None | str | Unset): Street address
            lead_source (None | str | Unset): Lead source / referral channel tag
            phone (None | str | Unset): Contact phone
            email (None | str | Unset): Contact email
            comment (None | str | Unset): Free-form back-office comment
            leverage (int | None | Unset): Account leverage (e.g. 100 means 1:100)
            agent_account (int | None | Unset): IB / agent account number that referred this client
            balance (float | None | Unset): Current balance (prefer dedicated balance ops for audit trail)
            credit (float | None | Unset): Credit on the account
            interest_rate (float | None | Unset): Interest rate
            taxes (float | None | Unset): Tax rate
            enable_flags (int | None | Unset): Account flag bitfield — see MT4User.EnableFlags for bit semantics
            send_reports (int | None | Unset): 0 = no reports, non-zero = nightly email reports enabled
            mqid (int | None | Unset): MetaQuotes ID for mobile push notifications
            user_color (int | None | Unset): UI tint color in terminal client lists
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
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
    leverage: int | None | Unset = UNSET
    agent_account: int | None | Unset = UNSET
    balance: float | None | Unset = UNSET
    credit: float | None | Unset = UNSET
    interest_rate: float | None | Unset = UNSET
    taxes: float | None | Unset = UNSET
    enable_flags: int | None | Unset = UNSET
    send_reports: int | None | Unset = UNSET
    mqid: int | None | Unset = UNSET
    user_color: int | None | Unset = UNSET





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

        leverage: int | None | Unset
        if isinstance(self.leverage, Unset):
            leverage = UNSET
        else:
            leverage = self.leverage

        agent_account: int | None | Unset
        if isinstance(self.agent_account, Unset):
            agent_account = UNSET
        else:
            agent_account = self.agent_account

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

        interest_rate: float | None | Unset
        if isinstance(self.interest_rate, Unset):
            interest_rate = UNSET
        else:
            interest_rate = self.interest_rate

        taxes: float | None | Unset
        if isinstance(self.taxes, Unset):
            taxes = UNSET
        else:
            taxes = self.taxes

        enable_flags: int | None | Unset
        if isinstance(self.enable_flags, Unset):
            enable_flags = UNSET
        else:
            enable_flags = self.enable_flags

        send_reports: int | None | Unset
        if isinstance(self.send_reports, Unset):
            send_reports = UNSET
        else:
            send_reports = self.send_reports

        mqid: int | None | Unset
        if isinstance(self.mqid, Unset):
            mqid = UNSET
        else:
            mqid = self.mqid

        user_color: int | None | Unset
        if isinstance(self.user_color, Unset):
            user_color = UNSET
        else:
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
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
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


        def _parse_leverage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        leverage = _parse_leverage(d.pop("leverage", UNSET))


        def _parse_agent_account(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agent_account = _parse_agent_account(d.pop("agentAccount", UNSET))


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


        def _parse_interest_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        interest_rate = _parse_interest_rate(d.pop("interestRate", UNSET))


        def _parse_taxes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        taxes = _parse_taxes(d.pop("taxes", UNSET))


        def _parse_enable_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        enable_flags = _parse_enable_flags(d.pop("enableFlags", UNSET))


        def _parse_send_reports(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        send_reports = _parse_send_reports(d.pop("sendReports", UNSET))


        def _parse_mqid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mqid = _parse_mqid(d.pop("mqid", UNSET))


        def _parse_user_color(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_color = _parse_user_color(d.pop("userColor", UNSET))


        mt4_user_update = cls(
            login=login,
            group=group,
            name=name,
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
            balance=balance,
            credit=credit,
            interest_rate=interest_rate,
            taxes=taxes,
            enable_flags=enable_flags,
            send_reports=send_reports,
            mqid=mqid,
            user_color=user_color,
        )

        return mt4_user_update

