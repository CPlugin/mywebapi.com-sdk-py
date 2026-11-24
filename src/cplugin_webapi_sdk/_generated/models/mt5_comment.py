from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_attachment_info import MT5AttachmentInfo





T = TypeVar("T", bound="MT5Comment")



@_attrs_define
class MT5Comment:
    """ Comment on a client or on a client document — input and output of the comment routes.

        Attributes:
            record_id (int | None | Unset): Comment identifier. Assigned by the server on creation.
            related_client (int | None | Unset): Identifier of the client the comment belongs to (required).
            related_document (int | None | Unset): Identifier of the document the comment belongs to; empty means the
                comment is on the client.
            flags (None | str | Unset): Comment flags as a string of the set flag names.
            extra (None | str | Unset): Reserved extra data of the comment.
            text (None | str | Unset): Comment text.
            comment_type (None | str | Unset): Comment type name.<br/>One of: COMMENT_TYPE_UNDEFINED, COMMENT_TYPE_FIRST,
                COMMENT_TYPE_LOGRECORD, COMMENT_TYPE_CALLRECORD, COMMENT_TYPE_ROBOTRECORD, COMMENT_TYPE_LAST. Case-insensitive;
                the numeric value is accepted too. Any other value is refused with error code Validation.
            comment_result (None | str | Unset): Result of the client contact the comment records.<br/>One of:
                COMMENT_RESULT_UNDEFINED, COMMENT_RESULT_FIRST, COMMENT_RESULT_CALL_NO_ANSWER, COMMENT_RESULT_CALL_WRONG_NUMBER,
                COMMENT_RESULT_CALL_NOT_INTERESTED, COMMENT_RESULT_CALL_SUCCESSFUL, COMMENT_RESULT_LAST. Case-insensitive; the
                numeric value is accepted too. Any other value is refused with error code Validation.
            attachments (list[MT5AttachmentInfo] | None | Unset): Attachments linked to the comment. Read-only: a link is
                created by the attachment routes, and a value
                sent here is ignored.
     """

    record_id: int | None | Unset = UNSET
    related_client: int | None | Unset = UNSET
    related_document: int | None | Unset = UNSET
    flags: None | str | Unset = UNSET
    extra: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    comment_type: None | str | Unset = UNSET
    comment_result: None | str | Unset = UNSET
    attachments: list[MT5AttachmentInfo] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_attachment_info import MT5AttachmentInfo
        record_id: int | None | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        related_client: int | None | Unset
        if isinstance(self.related_client, Unset):
            related_client = UNSET
        else:
            related_client = self.related_client

        related_document: int | None | Unset
        if isinstance(self.related_document, Unset):
            related_document = UNSET
        else:
            related_document = self.related_document

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        extra: None | str | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        else:
            extra = self.extra

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        comment_type: None | str | Unset
        if isinstance(self.comment_type, Unset):
            comment_type = UNSET
        else:
            comment_type = self.comment_type

        comment_result: None | str | Unset
        if isinstance(self.comment_result, Unset):
            comment_result = UNSET
        else:
            comment_result = self.comment_result

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
        if record_id is not UNSET:
            field_dict["recordID"] = record_id
        if related_client is not UNSET:
            field_dict["relatedClient"] = related_client
        if related_document is not UNSET:
            field_dict["relatedDocument"] = related_document
        if flags is not UNSET:
            field_dict["flags"] = flags
        if extra is not UNSET:
            field_dict["extra"] = extra
        if text is not UNSET:
            field_dict["text"] = text
        if comment_type is not UNSET:
            field_dict["commentType"] = comment_type
        if comment_result is not UNSET:
            field_dict["commentResult"] = comment_result
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_attachment_info import MT5AttachmentInfo
        d = dict(src_dict)
        def _parse_record_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_id = _parse_record_id(d.pop("recordID", UNSET))


        def _parse_related_client(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        related_client = _parse_related_client(d.pop("relatedClient", UNSET))


        def _parse_related_document(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        related_document = _parse_related_document(d.pop("relatedDocument", UNSET))


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_extra(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_comment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_type = _parse_comment_type(d.pop("commentType", UNSET))


        def _parse_comment_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_result = _parse_comment_result(d.pop("commentResult", UNSET))


        def _parse_attachments(data: object) -> list[MT5AttachmentInfo] | None | Unset:
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
                    attachments_type_0_item = MT5AttachmentInfo.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5AttachmentInfo] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        mt5_comment = cls(
            record_id=record_id,
            related_client=related_client,
            related_document=related_document,
            flags=flags,
            extra=extra,
            text=text,
            comment_type=comment_type,
            comment_result=comment_result,
            attachments=attachments,
        )

        return mt5_comment

