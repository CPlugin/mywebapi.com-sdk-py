from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5AttachmentInfo")



@_attrs_define
class MT5AttachmentInfo:
    """ Reference to a file attached to a document or a comment: identifier, name and size, without the content.

        Attributes:
            record_id (int | Unset): Attachment identifier.
            file_name (None | str | Unset): File name.
            file_size (int | Unset): Size of the file in bytes.
     """

    record_id: int | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size = self.file_size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if record_id is not UNSET:
            field_dict["recordID"] = record_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_id = d.pop("recordID", UNSET)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        file_size = d.pop("fileSize", UNSET)

        mt5_attachment_info = cls(
            record_id=record_id,
            file_name=file_name,
            file_size=file_size,
        )

        return mt5_attachment_info

