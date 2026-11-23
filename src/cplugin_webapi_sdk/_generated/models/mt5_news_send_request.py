from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5NewsSendRequest")



@_attrs_define
class MT5NewsSendRequest:
    """ News item to publish through the trade server.

        Attributes:
            subject (None | str | Unset): Subject of the news item.
            category (None | str | Unset): Category of the news item.
            time (datetime.datetime | None | Unset): Publication time, in the time zone of the trade server. Omitted uses
                the current time of
                the trade server.
            language (int | None | Unset): Language identifier of the news item.
            flags (int | None | Unset): News item flags as a bit mask: priority, read state, absence of a body, economic
                calendar.
            body (None | str | Unset): Body of the news item. Transferred whole, without interpretation.
     """

    subject: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    language: int | None | Unset = UNSET
    flags: int | None | Unset = UNSET
    body: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        language: int | None | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        flags: int | None | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_language(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        def _parse_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        mt5_news_send_request = cls(
            subject=subject,
            category=category,
            time=time,
            language=language,
            flags=flags,
            body=body,
        )

        return mt5_news_send_request

