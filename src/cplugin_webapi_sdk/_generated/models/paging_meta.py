from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PagingMeta")



@_attrs_define
class PagingMeta:
    """ Paging metadata returned alongside a list-shaped payload.
    `NextCursor` is an opaque base64 string the client passes back as
    `?cursor=` to fetch the next page; null when there are no more items.
    `HasMore` is the explicit boolean form of the same signal so clients
    can avoid string-null checks.

        Attributes:
            next_cursor (None | str | Unset): Opaque token for the next page; pass it back as ?cursor=. Null when there are
                no more items.
            has_more (bool | Unset): True if more items are available; explicit boolean form of NextCursor != null.
     """

    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        has_more = d.pop("hasMore", UNSET)

        paging_meta = cls(
            next_cursor=next_cursor,
            has_more=has_more,
        )

        return paging_meta

