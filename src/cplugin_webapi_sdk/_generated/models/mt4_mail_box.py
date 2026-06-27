from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4MailBox")



@_attrs_define
class MT4MailBox:
    """ v2 DTO for a single mailbox entry returned by `GET MailsRequest`
    (sidecar-only). Curated subset of the wrapper's `MailBox` —
    keeps the consumer-facing fields, drops the internal
    `ReceiversCount` bookkeeping.

        Attributes:
            time (datetime.datetime | Unset): Receive time (UTC)
            sender_login (int | Unset): Sender login (0 when sent by anonymous source)
            sender_name (None | str | Unset): Sender display name
            subject (None | str | Unset): Subject line
            body (None | str | Unset): Body text
     """

    time: datetime.datetime | Unset = UNSET
    sender_login: int | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if sender_login is not UNSET:
            field_dict["senderLogin"] = sender_login
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




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


        mt4_mail_box = cls(
            time=time,
            sender_login=sender_login,
            sender_name=sender_name,
            subject=subject,
            body=body,
        )

        return mt4_mail_box

