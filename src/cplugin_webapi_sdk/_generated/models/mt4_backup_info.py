from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4BackupInfo")



@_attrs_define
class MT4BackupInfo:
    """ v2 DTO for a single MT4 backup file descriptor. Curated subset of
    the platform's `BackupInfo` — drops the 6-int reserved blob and
    keeps only the three consumer-facing fields.

        Attributes:
            file (None | str | Unset): Backup file name (basename, server-relative)
            size (int | Unset): File size in bytes. Source field is a 32-bit signed int —
                widened to `long` here to give the client JSON-safe
                numeric range without re-shaping after a future platform fix.
            time (datetime.datetime | Unset): File modification time (UTC, from MetaQuotes `__time32_t`)
     """

    file: None | str | Unset = UNSET
    size: int | Unset = UNSET
    time: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        size = self.size

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file
        if size is not UNSET:
            field_dict["size"] = size
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))


        size = d.pop("size", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




        mt4_backup_info = cls(
            file=file,
            size=size,
            time=time,
        )

        return mt4_backup_info

