from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.mt5_book_item import MT5BookItem





T = TypeVar("T", bound="MT5Book")



@_attrs_define
class MT5Book:
    """ Full Depth of Market of one symbol, v2 read DTO.

        Attributes:
            symbol (None | str | Unset): Symbol the Depth of Market belongs to.
            flags (None | str | Unset): Depth of Market flags, comma-separated: `None`, `PreAuction` or `Snapshot`.
            time (datetime.datetime | None | Unset): Time of the last Depth of Market change, as the trade server counts it.
                Absent when the server sent no time.
            time_msc (datetime.datetime | None | Unset): Time of the last Depth of Market change with millisecond precision.
                Absent when the server sent no time.
            items (list[MT5BookItem] | None | Unset): Depth of Market entries.
     """

    symbol: None | str | Unset = UNSET
    flags: None | str | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    time_msc: datetime.datetime | None | Unset = UNSET
    items: list[MT5BookItem] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_book_item import MT5BookItem
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        time_msc: None | str | Unset
        if isinstance(self.time_msc, Unset):
            time_msc = UNSET
        elif isinstance(self.time_msc, datetime.datetime):
            time_msc = self.time_msc.isoformat()
        else:
            time_msc = self.time_msc

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if flags is not UNSET:
            field_dict["flags"] = flags
        if time is not UNSET:
            field_dict["time"] = time
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_book_item import MT5BookItem
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


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


        def _parse_time_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_msc = _parse_time_msc(d.pop("timeMsc", UNSET))


        def _parse_items(data: object) -> list[MT5BookItem] | None | Unset:
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
                    items_type_0_item = MT5BookItem.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5BookItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        mt5_book = cls(
            symbol=symbol,
            flags=flags,
            time=time,
            time_msc=time_msc,
            items=items,
        )

        return mt5_book

