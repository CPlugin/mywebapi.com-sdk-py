from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT4SymbolSession")



@_attrs_define
class MT4SymbolSession:
    """ v2 DTO for one open/close session window. The wrapper stores three of these
    per direction (Quote/Trade) per weekday — see CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4SymbolDaySessions.
    All four time components are server-local (the wrapper itself has no
    timezone — the trading server's clock is the reference frame).

        Attributes:
            open_hour (int | Unset): Session opens at this hour (0–23)
            open_minute (int | Unset): Session opens at this minute (0–59)
            close_hour (int | Unset): Session closes at this hour (0–23)
            close_minute (int | Unset): Session closes at this minute (0–59)
     """

    open_hour: int | Unset = UNSET
    open_minute: int | Unset = UNSET
    close_hour: int | Unset = UNSET
    close_minute: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        open_hour = self.open_hour

        open_minute = self.open_minute

        close_hour = self.close_hour

        close_minute = self.close_minute


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if open_hour is not UNSET:
            field_dict["openHour"] = open_hour
        if open_minute is not UNSET:
            field_dict["openMinute"] = open_minute
        if close_hour is not UNSET:
            field_dict["closeHour"] = close_hour
        if close_minute is not UNSET:
            field_dict["closeMinute"] = close_minute

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_hour = d.pop("openHour", UNSET)

        open_minute = d.pop("openMinute", UNSET)

        close_hour = d.pop("closeHour", UNSET)

        close_minute = d.pop("closeMinute", UNSET)

        mt4_symbol_session = cls(
            open_hour=open_hour,
            open_minute=open_minute,
            close_hour=close_hour,
            close_minute=close_minute,
        )

        return mt4_symbol_session

