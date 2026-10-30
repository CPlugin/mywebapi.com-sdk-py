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
    """ Type 1 mutator input — full-replace shape for `UserRecordUpdate`.
    Client submits every non-secret, non-read-only, non-computed field; the
    handler reads the current record from MT4 server, copies the secrets and
    read-only fields off it, applies this DTO over the rest, and writes the
    modified structure back.

    Read-only fields that do NOT appear here (preserved by the server-side
    read step):
      * `Login` — passed as a path parameter, immutable identity.
      * `RegistrationDate` — set once on creation, never updated.
      * `LastDate`, `LastIP` — assigned by MT4 server during login.
      * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
        `PrevEquity` — derived server-side at reporting close.

    Secret fields that do NOT appear here (preserved by the server-side
    read step; use dedicated endpoints to change them):
      * `Password`, `PasswordInvestor`, `PasswordPhone` —
        change via `POST UserPasswordSet`.
      * `OTPSecret` — provisioned via separate admin flow.
      * `APIData` — platform-internal blob, never client-controlled.

    <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
    platform `UserRecordUpdate` writes them directly. However, the audit-
    trail-preserving way to move money is the dedicated balance operation
    endpoints (forthcoming) — submitting Balance via this DTO bypasses the
    audit log on MT4 server side.

        Attributes:
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
            leverage (int | Unset): Account leverage (e.g. 100 means 1:100)
            agent_account (int | Unset): IB / agent account number that referred this client
            balance (float | Unset): Current balance (prefer dedicated balance ops for audit trail)
            credit (float | Unset): Credit on the account
            interest_rate (float | Unset): Interest rate
            taxes (float | Unset): Tax rate
            enable_flags (int | Unset): Account flag bitfield — see MT4User.EnableFlags for bit semantics
            send_reports (int | Unset): 0 = no reports, non-zero = nightly email reports enabled
            mqid (int | Unset): MetaQuotes ID for mobile push notifications
            user_color (int | Unset): UI tint color in terminal client lists
     """

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
    leverage: int | Unset = UNSET
    agent_account: int | Unset = UNSET
    balance: float | Unset = UNSET
    credit: float | Unset = UNSET
    interest_rate: float | Unset = UNSET
    taxes: float | Unset = UNSET
    enable_flags: int | Unset = UNSET
    send_reports: int | Unset = UNSET
    mqid: int | Unset = UNSET
    user_color: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        leverage = self.leverage

        agent_account = self.agent_account

        balance = self.balance

        credit = self.credit

        interest_rate = self.interest_rate

        taxes = self.taxes

        enable_flags = self.enable_flags

        send_reports = self.send_reports

        mqid = self.mqid

        user_color = self.user_color


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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


        leverage = d.pop("leverage", UNSET)

        agent_account = d.pop("agentAccount", UNSET)

        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        taxes = d.pop("taxes", UNSET)

        enable_flags = d.pop("enableFlags", UNSET)

        send_reports = d.pop("sendReports", UNSET)

        mqid = d.pop("mqid", UNSET)

        user_color = d.pop("userColor", UNSET)

        mt4_user_update = cls(
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

