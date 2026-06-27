from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SymbolSession")



@_attrs_define
class MT5SymbolSession:
    """ 
        Attributes:
            open_ (int | None | Unset): The session opening time in minutes from 00:00. For example, 100 denotes 01:40.
            open_hours (int | None | Unset): Get the number of hours in the opening time of trading or quoting session of a
                symbol.
            open_minutes (int | None | Unset): The number of minutes in the opening time of trading or quoting session of a
                symbol.
            close (int | None | Unset): The session closing time in minutes from 00:00. For example, 100 denotes 01:40.
            close_hours (int | None | Unset): The number of hours in the closing time of trading or quoting session of a
                symbol.
            close_minutes (int | None | Unset): The number of minutes in the closing time of trading or quoting session of a
                symbol.
     """

    open_: int | None | Unset = UNSET
    open_hours: int | None | Unset = UNSET
    open_minutes: int | None | Unset = UNSET
    close: int | None | Unset = UNSET
    close_hours: int | None | Unset = UNSET
    close_minutes: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        open_: int | None | Unset
        if isinstance(self.open_, Unset):
            open_ = UNSET
        else:
            open_ = self.open_

        open_hours: int | None | Unset
        if isinstance(self.open_hours, Unset):
            open_hours = UNSET
        else:
            open_hours = self.open_hours

        open_minutes: int | None | Unset
        if isinstance(self.open_minutes, Unset):
            open_minutes = UNSET
        else:
            open_minutes = self.open_minutes

        close: int | None | Unset
        if isinstance(self.close, Unset):
            close = UNSET
        else:
            close = self.close

        close_hours: int | None | Unset
        if isinstance(self.close_hours, Unset):
            close_hours = UNSET
        else:
            close_hours = self.close_hours

        close_minutes: int | None | Unset
        if isinstance(self.close_minutes, Unset):
            close_minutes = UNSET
        else:
            close_minutes = self.close_minutes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if open_ is not UNSET:
            field_dict["open"] = open_
        if open_hours is not UNSET:
            field_dict["openHours"] = open_hours
        if open_minutes is not UNSET:
            field_dict["openMinutes"] = open_minutes
        if close is not UNSET:
            field_dict["close"] = close
        if close_hours is not UNSET:
            field_dict["closeHours"] = close_hours
        if close_minutes is not UNSET:
            field_dict["closeMinutes"] = close_minutes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_open_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_ = _parse_open_(d.pop("open", UNSET))


        def _parse_open_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_hours = _parse_open_hours(d.pop("openHours", UNSET))


        def _parse_open_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_minutes = _parse_open_minutes(d.pop("openMinutes", UNSET))


        def _parse_close(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        close = _parse_close(d.pop("close", UNSET))


        def _parse_close_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        close_hours = _parse_close_hours(d.pop("closeHours", UNSET))


        def _parse_close_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        close_minutes = _parse_close_minutes(d.pop("closeMinutes", UNSET))


        mt5_symbol_session = cls(
            open_=open_,
            open_hours=open_hours,
            open_minutes=open_minutes,
            close=close,
            close_hours=close_hours,
            close_minutes=close_minutes,
        )

        return mt5_symbol_session

