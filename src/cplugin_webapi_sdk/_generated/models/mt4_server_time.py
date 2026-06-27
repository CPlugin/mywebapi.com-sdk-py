from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4ServerTime")



@_attrs_define
class MT4ServerTime:
    """ v2 DTO for the MT4 server's per-hour access matrix (wrapper's
    `ConTime.Days` field). 168-element flat array; each element
    is `0` (denied) or `1` (allowed) for one hour of the
    week. Layout: `index = day * 24 + hour`, day-of-week 0..6
    matches MT4's native convention where day 0 = Sunday.
    <br>
    Example: `AccessHours[24..47]` covers Monday's 24 hours.
    Internal `DaysControl` and `Reserved` wrapper fields
    are not part of the v2 contract.

        Attributes:
            access_hours (list[int] | None | Unset): 7×24 = 168 hourly access flags. Index = day*24 + hour;
                day 0 = Sunday (MT4 convention). 0 = denied, 1 = allowed.
     """

    access_hours: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        access_hours: list[int] | None | Unset
        if isinstance(self.access_hours, Unset):
            access_hours = UNSET
        elif isinstance(self.access_hours, list):
            access_hours = self.access_hours


        else:
            access_hours = self.access_hours


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if access_hours is not UNSET:
            field_dict["accessHours"] = access_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_access_hours(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_hours_type_0 = cast(list[int], data)

                return access_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        access_hours = _parse_access_hours(d.pop("accessHours", UNSET))


        mt4_server_time = cls(
            access_hours=access_hours,
        )

        return mt4_server_time

