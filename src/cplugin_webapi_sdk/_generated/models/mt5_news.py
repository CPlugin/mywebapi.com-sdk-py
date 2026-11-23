from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5News")



@_attrs_define
class MT5News:
    """ News item received by the manager account of the trade server.

        Attributes:
            id (int | Unset): News item identifier.
            subject (None | str | Unset): Subject of the news item.
            category (None | str | Unset): Category of the news item, as set by the sender.
            time (datetime.datetime | None | Unset): Time the news item was sent, in the time zone of the trade server. The
                platform stores the
                value without a zone, so it is returned as a wall-clock time.
            language (int | Unset): Language identifier of the news item.
            flags (int | Unset): News item flags as a bit mask: priority, read state, absence of a body, economic calendar.
            body_size (int | Unset): Size of the body in bytes.
            body (None | str | Unset): Body of the news item as stored by the trade server. Absent in the list route. The
                platform
                treats the body as arbitrary data, so it is transferred without interpretation.
     """

    id: int | Unset = UNSET
    subject: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    language: int | Unset = UNSET
    flags: int | Unset = UNSET
    body_size: int | Unset = UNSET
    body: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        language = self.language

        flags = self.flags

        body_size = self.body_size

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if category is not UNSET:
            field_dict["category"] = category
        if time is not UNSET:
            field_dict["time"] = time
        if language is not UNSET:
            field_dict["language"] = language
        if flags is not UNSET:
            field_dict["flags"] = flags
        if body_size is not UNSET:
            field_dict["bodySize"] = body_size
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


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


        language = d.pop("language", UNSET)

        flags = d.pop("flags", UNSET)

        body_size = d.pop("bodySize", UNSET)

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        mt5_news = cls(
            id=id,
            subject=subject,
            category=category,
            time=time,
            language=language,
            flags=flags,
            body_size=body_size,
            body=body,
        )

        return mt5_news

