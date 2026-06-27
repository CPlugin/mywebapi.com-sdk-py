from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Holiday")



@_attrs_define
class MT4Holiday:
    """ v2 DTO for a single MT4 holiday-calendar entry. Curated subset of the
    wrapper's ConHoliday struct — exposes the broker-facing fields and
    drops the internal Reserved/Next pointer block. Date is split into
    Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
    conversion to avoid timezone ambiguity for date-only entries).

        Attributes:
            year (int | Unset): Calendar year of the holiday (e.g. 2026)
            month (int | Unset): Calendar month, 1..12
            day (int | Unset): Day-of-month, 1..31
            from_ (int | Unset): Work-day start time, in minutes from midnight (0 if closed all day)
            to (int | Unset): Work-day end time, in minutes from midnight
            symbol (None | str | Unset): Symbol name, symbol group name, or "All" for global holiday
            description (None | str | Unset): Free-form description of the holiday
            enable (bool | Unset): Whether the holiday entry is active
     """

    year: int | Unset = UNSET
    month: int | Unset = UNSET
    day: int | Unset = UNSET
    from_: int | Unset = UNSET
    to: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    enable: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month = self.month

        day = self.day

        from_ = self.from_

        to = self.to

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enable = self.enable


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if description is not UNSET:
            field_dict["description"] = description
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        enable = d.pop("enable", UNSET)

        mt4_holiday = cls(
            year=year,
            month=month,
            day=day,
            from_=from_,
            to=to,
            symbol=symbol,
            description=description,
            enable=enable,
        )

        return mt4_holiday

