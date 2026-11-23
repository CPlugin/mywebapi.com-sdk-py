from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Attachment")



@_attrs_define
class MT5Attachment:
    """ File attached to a client, a document or a comment.

        Attributes:
            record_id (int | None | Unset): Attachment identifier. Assigned by the server when the file is stored.
            related_client (int | None | Unset): Identifier of the client the attachment belongs to (required when a file is
                stored).
            file_type (None | str | Unset): File type name.<br/>One of: FILE_TYPE_OTHER, FILE_TYPE_FIRST, FILE_TYPE_TXT,
                FILE_TYPE_DOC, FILE_TYPE_PDF, FILE_TYPE_JPG, FILE_TYPE_PNG, FILE_TYPE_BMP, FILE_TYPE_ZIP, FILE_TYPE_LAST. Case-
                insensitive; the numeric value is accepted too. Any other value is refused with error code Validation.
            file_name (None | str | Unset): File name.
            file_content (None | str | Unset): File content. Sent as base64 in JSON; the whole file travels in the request
                and the response.
            file_size (int | None | Unset): Size of the file in bytes. Read-only: filled by the server.
            file_flags (None | str | Unset): File flags as a string of the set flag names.
            document_id (int | None | Unset): Document the file is linked to. Used only when a file is stored; empty means
                no document link.
            comment_id (int | None | Unset): Comment the file is linked to. Used only when a file is stored; empty means no
                comment link.
     """

    record_id: int | None | Unset = UNSET
    related_client: int | None | Unset = UNSET
    file_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_content: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    file_flags: None | str | Unset = UNSET
    document_id: int | None | Unset = UNSET
    comment_id: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        else:
            file_type = self.file_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_content: None | str | Unset
        if isinstance(self.file_content, Unset):
            file_content = UNSET
        else:
            file_content = self.file_content

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        file_flags: None | str | Unset
        if isinstance(self.file_flags, Unset):
            file_flags = UNSET
        else:
            file_flags = self.file_flags

        document_id: int | None | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        comment_id: int | None | Unset
        if isinstance(self.comment_id, Unset):
            comment_id = UNSET
        else:
            comment_id = self.comment_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if record_id is not UNSET:
            field_dict["recordID"] = record_id
        if related_client is not UNSET:
            field_dict["relatedClient"] = related_client
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_content is not UNSET:
            field_dict["fileContent"] = file_content
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if file_flags is not UNSET:
            field_dict["fileFlags"] = file_flags
        if document_id is not UNSET:
            field_dict["documentID"] = document_id
        if comment_id is not UNSET:
            field_dict["commentID"] = comment_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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


        def _parse_file_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_type = _parse_file_type(d.pop("fileType", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        def _parse_file_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_content = _parse_file_content(d.pop("fileContent", UNSET))


        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("fileSize", UNSET))


        def _parse_file_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_flags = _parse_file_flags(d.pop("fileFlags", UNSET))


        def _parse_document_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        document_id = _parse_document_id(d.pop("documentID", UNSET))


        def _parse_comment_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment_id = _parse_comment_id(d.pop("commentID", UNSET))


        mt5_attachment = cls(
            record_id=record_id,
            related_client=related_client,
            file_type=file_type,
            file_name=file_name,
            file_content=file_content,
            file_size=file_size,
            file_flags=file_flags,
            document_id=document_id,
            comment_id=comment_id,
        )

        return mt5_attachment

