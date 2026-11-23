from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_online import MT5Online





T = TypeVar("T", bound="MT5OnlinePage")



@_attrs_define
class MT5OnlinePage:
    """ One positional window of the live connection list, v2 read DTO.

        Attributes:
            items (list[MT5Online] | None | Unset): Connections of this window.
            total (int | Unset): Total number of connections on the trade server at the moment of the request.
            from_ (int | Unset): Position the window starts at, echoed from the request.
     """

    items: list[MT5Online] | None | Unset = UNSET
    total: int | Unset = UNSET
    from_: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_online import MT5Online
        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        total = self.total

        from_ = self.from_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if total is not UNSET:
            field_dict["total"] = total
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_online import MT5Online
        d = dict(src_dict)
        def _parse_items(data: object) -> list[MT5Online] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = MT5Online.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Online] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        total = d.pop("total", UNSET)

        from_ = d.pop("from", UNSET)

        mt5_online_page = cls(
            items=items,
            total=total,
            from_=from_,
        )

        return mt5_online_page

