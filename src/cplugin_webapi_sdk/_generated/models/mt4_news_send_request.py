from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4NewsSendRequest")



@_attrs_define
class MT4NewsSendRequest:
    """ v2 request DTO for `POST NewsSend` — pushes a single news item
    to the MT4 server, which fans it out to all connected client
    terminals. Platform signature: `ResultCode NewsSend(NewsTopic news)`.

        Attributes:
            topic (None | str | Unset): News headline (required, up to 256 chars)
            category (None | str | Unset): News category (optional, up to 64 chars)
            body (None | str | Unset): News body text (required)
            high_priority (bool | Unset): High-priority flag (`true` = priority 1, `false` = priority 0)
     """

    topic: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    high_priority: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        topic: None | str | Unset
        if isinstance(self.topic, Unset):
            topic = UNSET
        else:
            topic = self.topic

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        high_priority = self.high_priority


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if topic is not UNSET:
            field_dict["topic"] = topic
        if category is not UNSET:
            field_dict["category"] = category
        if body is not UNSET:
            field_dict["body"] = body
        if high_priority is not UNSET:
            field_dict["highPriority"] = high_priority

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_topic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topic = _parse_topic(d.pop("topic", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        high_priority = d.pop("highPriority", UNSET)

        mt4_news_send_request = cls(
            topic=topic,
            category=category,
            body=body,
            high_priority=high_priority,
        )

        return mt4_news_send_request

