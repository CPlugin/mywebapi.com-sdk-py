from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.mt5_mail_attachment import MT5MailAttachment





T = TypeVar("T", bound="MT5Mail")



@_attrs_define
class MT5Mail:
    """ Message of the internal mail system of the trade server.

        Attributes:
            id (int | Unset): Message identifier.
            parent (int | Unset): Identifier of the message this one answers; zero when it starts a thread.
            subject (None | str | Unset): Subject of the message.
            from_ (int | Unset): Login of the sender.
            from_name (None | str | Unset): Name of the sender.
            to (int | Unset): Login of the recipient.
            to_name (None | str | Unset): Name of the recipient.
            time (datetime.datetime | None | Unset): Time the message was sent, in UTC.
            body_size (int | Unset): Size of the body in bytes.
            attachments_total (int | Unset): Number of files attached to the message.
            body (None | str | Unset): Body of the message as stored by the trade server. Absent in the list route; request
                the
                message by its identifier to receive it. The platform treats the body as arbitrary data,
                so it is transferred without interpretation.
            attachments (list[MT5MailAttachment] | None | Unset): Files attached to the message, with their content. Absent
                in the list route.
     """

    id: int | Unset = UNSET
    parent: int | Unset = UNSET
    subject: None | str | Unset = UNSET
    from_: int | Unset = UNSET
    from_name: None | str | Unset = UNSET
    to: int | Unset = UNSET
    to_name: None | str | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    body_size: int | Unset = UNSET
    attachments_total: int | Unset = UNSET
    body: None | str | Unset = UNSET
    attachments: list[MT5MailAttachment] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_mail_attachment import MT5MailAttachment
        id = self.id

        parent = self.parent

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        from_ = self.from_

        from_name: None | str | Unset
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        to = self.to

        to_name: None | str | Unset
        if isinstance(self.to_name, Unset):
            to_name = UNSET
        else:
            to_name = self.to_name

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        body_size = self.body_size

        attachments_total = self.attachments_total

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
        if id is not UNSET:
            field_dict["id"] = id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if subject is not UNSET:
            field_dict["subject"] = subject
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if to is not UNSET:
            field_dict["to"] = to
        if to_name is not UNSET:
            field_dict["toName"] = to_name
        if time is not UNSET:
            field_dict["time"] = time
        if body_size is not UNSET:
            field_dict["bodySize"] = body_size
        if attachments_total is not UNSET:
            field_dict["attachmentsTotal"] = attachments_total
        if body is not UNSET:
            field_dict["body"] = body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_mail_attachment import MT5MailAttachment
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        parent = d.pop("parent", UNSET)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))


        from_ = d.pop("from", UNSET)

        def _parse_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_name = _parse_from_name(d.pop("fromName", UNSET))


        to = d.pop("to", UNSET)

        def _parse_to_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_name = _parse_to_name(d.pop("toName", UNSET))


        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)



                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        body_size = d.pop("bodySize", UNSET)

        attachments_total = d.pop("attachmentsTotal", UNSET)

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


        mt5_mail = cls(
            id=id,
            parent=parent,
            subject=subject,
            from_=from_,
            from_name=from_name,
            to=to,
            to_name=to_name,
            time=time,
            body_size=body_size,
            attachments_total=attachments_total,
            body=body,
            attachments=attachments,
        )

        return mt5_mail

