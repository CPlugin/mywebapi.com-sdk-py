from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5UserAddRequest")



@_attrs_define
class MT5UserAddRequest:
    """ Request body of the account-creation operation: the editable record plus the
                optional login and the two passwords.

        Attributes:
            login (int | None | Unset): Account login to create. Omit or send zero to let the trade server allocate one.
            password (None | str | Unset): Master password. Optional — generated when missing.
            password_investor (None | str | Unset): Investor (read-only) password. Optional — generated when missing.
            group (None | str | Unset): User group name.
            name (None | str | Unset): Full display name of the account holder.
            company (None | str | Unset): Company or organisation name.
            country (None | str | Unset): Client country.
            city (None | str | Unset): Client city.
            state (None | str | Unset): Client state or province.
            zip_code (None | str | Unset): Client postal code.
            phone (None | str | Unset): Client phone number.
            phone_password (None | str | Unset): Phone password used for telephone trading.
            e_mail (None | str | Unset): Client email address.
            comment (None | str | Unset): Internal comment on the account.
            color (int | None | Unset): Colour tag assigned to the account in MT5 Manager (ARGB uint).
            leverage (int | None | Unset): Account leverage (e.g. 100 = 1:100).
            rights (None | str | Unset): Account permission flags: names of the set bits, `"Enabled, Password"` (the
                MT5UserRights schema).
            account (None | str | Unset): Account ID string (external account identifier).
            language (int | None | Unset): Client language code (MT5 locale uint).
            address (None | str | Unset): Client postal/physical address.
            id (None | str | Unset): Client document ID (passport, national ID, etc.).
            status (None | str | Unset): Client KYC / account status label.
            agent (int | None | Unset): Introducing agent login.
            lead_campaign (None | str | Unset): Marketing lead campaign name.
            lead_source (None | str | Unset): Marketing lead source name.
            client_id (int | None | Unset): External CRM client ID.
            first_name (None | str | Unset): Given name (first name).
            last_name (None | str | Unset): Family name (last name).
            middle_name (None | str | Unset): Patronymic / middle name.
            registration (datetime.datetime | None | Unset): Account registration date and time.
            otp_secret (None | str | Unset): Shared secret for two-factor authentication (OTP).
     """

    login: int | None | Unset = UNSET
    password: None | str | Unset = UNSET
    password_investor: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    phone_password: None | str | Unset = UNSET
    e_mail: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    color: int | None | Unset = UNSET
    leverage: int | None | Unset = UNSET
    rights: None | str | Unset = UNSET
    account: None | str | Unset = UNSET
    language: int | None | Unset = UNSET
    address: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    agent: int | None | Unset = UNSET
    lead_campaign: None | str | Unset = UNSET
    lead_source: None | str | Unset = UNSET
    client_id: int | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    registration: datetime.datetime | None | Unset = UNSET
    otp_secret: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login: int | None | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        password_investor: None | str | Unset
        if isinstance(self.password_investor, Unset):
            password_investor = UNSET
        else:
            password_investor = self.password_investor

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

        phone_password: None | str | Unset
        if isinstance(self.phone_password, Unset):
            phone_password = UNSET
        else:
            phone_password = self.phone_password

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

        color: int | None | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        leverage: int | None | Unset
        if isinstance(self.leverage, Unset):
            leverage = UNSET
        else:
            leverage = self.leverage

        rights: None | str | Unset
        if isinstance(self.rights, Unset):
            rights = UNSET
        else:
            rights = self.rights

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        language: int | None | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
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

        agent: int | None | Unset
        if isinstance(self.agent, Unset):
            agent = UNSET
        else:
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

        client_id: int | None | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
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

        registration: None | str | Unset
        if isinstance(self.registration, Unset):
            registration = UNSET
        elif isinstance(self.registration, datetime.datetime):
            registration = self.registration.isoformat()
        else:
            registration = self.registration

        otp_secret: None | str | Unset
        if isinstance(self.otp_secret, Unset):
            otp_secret = UNSET
        else:
            otp_secret = self.otp_secret


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if password_investor is not UNSET:
            field_dict["passwordInvestor"] = password_investor
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
        if phone_password is not UNSET:
            field_dict["phonePassword"] = phone_password
        if e_mail is not UNSET:
            field_dict["eMail"] = e_mail
        if comment is not UNSET:
            field_dict["comment"] = comment
        if color is not UNSET:
            field_dict["color"] = color
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if rights is not UNSET:
            field_dict["rights"] = rights
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
        if registration is not UNSET:
            field_dict["registration"] = registration
        if otp_secret is not UNSET:
            field_dict["otpSecret"] = otp_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        def _parse_password_investor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password_investor = _parse_password_investor(d.pop("passwordInvestor", UNSET))


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


        def _parse_phone_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_password = _parse_phone_password(d.pop("phonePassword", UNSET))


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


        def _parse_color(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        color = _parse_color(d.pop("color", UNSET))


        def _parse_leverage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        leverage = _parse_leverage(d.pop("leverage", UNSET))


        def _parse_rights(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rights = _parse_rights(d.pop("rights", UNSET))


        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))


        def _parse_language(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


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


        def _parse_agent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agent = _parse_agent(d.pop("agent", UNSET))


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


        def _parse_client_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_id = _parse_client_id(d.pop("clientID", UNSET))


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


        def _parse_otp_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otp_secret = _parse_otp_secret(d.pop("otpSecret", UNSET))


        mt5_user_add_request = cls(
            login=login,
            password=password,
            password_investor=password_investor,
            group=group,
            name=name,
            company=company,
            country=country,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
            phone_password=phone_password,
            e_mail=e_mail,
            comment=comment,
            color=color,
            leverage=leverage,
            rights=rights,
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
            registration=registration,
            otp_secret=otp_secret,
        )

        return mt5_user_add_request

