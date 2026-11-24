from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5EmailSendRequest")



@_attrs_define
class MT5EmailSendRequest:
    """ An email to send through one of the mail configurations of the trade server.

        Attributes:
            account (None | str | Unset): Name of the mail configuration used for sending.
            to (None | str | Unset): Recipient address.
            to_name (None | str | Unset): Recipient name shown by the mail client.
            subject (None | str | Unset): Subject line.
            body (None | str | Unset): Message body.
     """

    account: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    to_name: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        to_name: None | str | Unset
        if isinstance(self.to_name, Unset):
            to_name = UNSET
        else:
            to_name = self.to_name

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account is not UNSET:
            field_dict["account"] = account
        if to is not UNSET:
            field_dict["to"] = to
        if to_name is not UNSET:
            field_dict["toName"] = to_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        def _parse_to_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_name = _parse_to_name(d.pop("toName", UNSET))


        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))


        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        mt5_email_send_request = cls(
            account=account,
            to=to,
            to_name=to_name,
            subject=subject,
            body=body,
        )

        return mt5_email_send_request

