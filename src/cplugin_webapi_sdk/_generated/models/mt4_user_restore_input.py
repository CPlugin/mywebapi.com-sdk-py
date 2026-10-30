from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4UserRestoreInput")



@_attrs_define
class MT4UserRestoreInput:
    """ v2 narrow input DTO for `BackupRestoreUsers`. Carries the
    account identity + persistent metadata + money/leverage state that a
    disaster-recovery flow needs to recreate.

        Attributes:
            login (int | Unset): Account login (record key)
            group (None | str | Unset): Group name
            name (None | str | Unset): Account holder display name
            email (None | str | Unset): Email address
            country (None | str | Unset): Country
            leverage (int | Unset): Trading leverage (e.g. 100 for 1:100)
            balance (float | Unset): Account balance (broker base currency)
            credit (float | Unset): Account credit (e.g. promotional bonus)
            enable (int | Unset): Account enabled flag (0 = disabled, 1 = enabled — raw platform int)
            enable_read_only (int | Unset): Read-only flag (1 = cannot open positions)
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    leverage: int | Unset = UNSET
    balance: float | Unset = UNSET
    credit: float | Unset = UNSET
    enable: int | Unset = UNSET
    enable_read_only: int | Unset = UNSET





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

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        leverage = self.leverage

        balance = self.balance

        credit = self.credit

        enable = self.enable

        enable_read_only = self.enable_read_only


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if country is not UNSET:
            field_dict["country"] = country
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if enable is not UNSET:
            field_dict["enable"] = enable
        if enable_read_only is not UNSET:
            field_dict["enableReadOnly"] = enable_read_only

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


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        leverage = d.pop("leverage", UNSET)

        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        enable = d.pop("enable", UNSET)

        enable_read_only = d.pop("enableReadOnly", UNSET)

        mt4_user_restore_input = cls(
            login=login,
            group=group,
            name=name,
            email=email,
            country=country,
            leverage=leverage,
            balance=balance,
            credit=credit,
            enable=enable,
            enable_read_only=enable_read_only,
        )

        return mt4_user_restore_input

