from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4MailSendRequest")



@_attrs_define
class MT4MailSendRequest:
    """ v2 request DTO for `POST MailSend` (sidecar-only). Sends an
    email to one or more client logins. Platform signature:
    `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.

        Attributes:
            sender_login (int | Unset): Sender login (0 = no reply allowed; otherwise valid manager login)
            sender_name (None | str | Unset): Sender display name (optional, up to 64 chars)
            subject (None | str | Unset): Email subject line (up to 128 chars)
            body (None | str | Unset): Email body (required, non-empty)
            logins (list[int] | None | Unset): Recipient logins (at least 1, batch cap 10000)
     """

    sender_login: int | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    logins: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        sender_login = self.sender_login

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

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

        logins: list[int] | None | Unset
        if isinstance(self.logins, Unset):
            logins = UNSET
        elif isinstance(self.logins, list):
            logins = self.logins


        else:
            logins = self.logins


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if sender_login is not UNSET:
            field_dict["senderLogin"] = sender_login
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if logins is not UNSET:
            field_dict["logins"] = logins

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_login = d.pop("senderLogin", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("senderName", UNSET))


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


        def _parse_logins(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logins_type_0 = cast(list[int], data)

                return logins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        logins = _parse_logins(d.pop("logins", UNSET))


        mt4_mail_send_request = cls(
            sender_login=sender_login,
            sender_name=sender_name,
            subject=subject,
            body=body,
            logins=logins,
        )

        return mt4_mail_send_request

