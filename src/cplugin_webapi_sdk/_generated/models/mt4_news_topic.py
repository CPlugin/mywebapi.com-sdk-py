from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4NewsTopic")



@_attrs_define
class MT4NewsTopic:
    r""" v2 DTO describing a single news topic header as held in the platform's
    pumping cache. Curated subset of the platform's NewsTopic: enough to render
    a list / browse view of broker-distributed news (Key for follow-up
    NewsBodyGet / NewsBodyRequest, Time, Topic, Category, Keywords, Priority,
    LangId). The news body is not part of the topic; fetch it with
    `NewsBodyGet(key)`.

        Attributes:
            key (int | Unset): News key — the identifier used by `NewsBodyGet` and
                `NewsBodyRequest` to fetch the body for this topic.
            time (datetime.datetime | Unset): Published time of the news topic (UTC).
            topic (None | str | Unset): News headline / subject (max 256 chars at the platform layer).
            category (None | str | Unset): News category. Slash-separated path on the platform side (e.g.
                "Markets\Asian Markets News") used by the MT4 client terminal to
                build a tree view. Max 64 chars at the platform layer.
            keywords (None | str | Unset): Comma-separated keyword list (max 256 chars). Used by quote-feed
                brokers as a symbol filter — for example `"!EURUSD, EUR*"`
                selects all EUR pairs except EURUSD.
            priority (int | Unset): News priority: 0 = general, 1 = high.
            lang_id (int | Unset): Windows LCID language id. 0 means unspecified; otherwise the low
                16 bits of a Windows LCID (the language portion).
     """

    key: int | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    topic: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    keywords: None | str | Unset = UNSET
    priority: int | Unset = UNSET
    lang_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

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

        keywords: None | str | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        priority = self.priority

        lang_id = self.lang_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if time is not UNSET:
            field_dict["time"] = time
        if topic is not UNSET:
            field_dict["topic"] = topic
        if category is not UNSET:
            field_dict["category"] = category
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if priority is not UNSET:
            field_dict["priority"] = priority
        if lang_id is not UNSET:
            field_dict["langId"] = lang_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




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


        def _parse_keywords(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        priority = d.pop("priority", UNSET)

        lang_id = d.pop("langId", UNSET)

        mt4_news_topic = cls(
            key=key,
            time=time,
            topic=topic,
            category=category,
            keywords=keywords,
            priority=priority,
            lang_id=lang_id,
        )

        return mt4_news_topic

