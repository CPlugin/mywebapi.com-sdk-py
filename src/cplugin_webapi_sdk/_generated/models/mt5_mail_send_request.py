from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_mail_attachment import MT5MailAttachment





T = TypeVar("T", bound="MT5MailSendRequest")



@_attrs_define
class MT5MailSendRequest:
    """ Message to send through the internal mail system of the trade server.

        Attributes:
            to (int | Unset): Login of the recipient.
            to_name (None | str | Unset): Name of the recipient.
            subject (None | str | Unset): Subject of the message.
            body (None | str | Unset): Body of the message. Transferred whole, without interpretation.
            attachments (list[MT5MailAttachment] | None | Unset): Files to attach to the message.
     """

    to: int | Unset = UNSET
    to_name: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    attachments: list[MT5MailAttachment] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_mail_attachment import MT5MailAttachment
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

        attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)


        else:
            attachments = self.attachments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if to is not UNSET:
            field_dict["to"] = to
        if to_name is not UNSET:
            field_dict["toName"] = to_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_mail_attachment import MT5MailAttachment
        d = dict(src_dict)
        to = d.pop("to", UNSET)

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


        def _parse_attachments(data: object) -> list[MT5MailAttachment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in (_attachments_type_0):
                    attachments_type_0_item = MT5MailAttachment.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5MailAttachment] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        mt5_mail_send_request = cls(
            to=to,
            to_name=to_name,
            subject=subject,
            body=body,
            attachments=attachments,
        )

        return mt5_mail_send_request

