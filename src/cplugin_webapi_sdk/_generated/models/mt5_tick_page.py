from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_tick_v2 import MT5TickV2





T = TypeVar("T", bound="MT5TickPage")



@_attrs_define
class MT5TickPage:
    """ Ticks of one history request, v2 read DTO.

        Attributes:
            ticks (list[MT5TickV2] | None | Unset): Ticks of this page, ordered by time ascending.
            total (int | Unset): Total number of ticks in the requested window.
            truncated (bool | Unset): True when `Total` exceeds the page and more ticks were available than returned.
     """

    ticks: list[MT5TickV2] | None | Unset = UNSET
    total: int | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_tick_v2 import MT5TickV2
        ticks: list[dict[str, Any]] | None | Unset
        if isinstance(self.ticks, Unset):
            ticks = UNSET
        elif isinstance(self.ticks, list):
            ticks = []
            for ticks_type_0_item_data in self.ticks:
                ticks_type_0_item = ticks_type_0_item_data.to_dict()
                ticks.append(ticks_type_0_item)


        else:
            ticks = self.ticks

        total = self.total

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ticks is not UNSET:
            field_dict["ticks"] = ticks
        if total is not UNSET:
            field_dict["total"] = total
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_tick_v2 import MT5TickV2
        d = dict(src_dict)
        def _parse_ticks(data: object) -> list[MT5TickV2] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ticks_type_0 = []
                _ticks_type_0 = data
                for ticks_type_0_item_data in (_ticks_type_0):
                    ticks_type_0_item = MT5TickV2.from_dict(ticks_type_0_item_data)



                    ticks_type_0.append(ticks_type_0_item)

                return ticks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5TickV2] | None | Unset, data)

        ticks = _parse_ticks(d.pop("ticks", UNSET))


        total = d.pop("total", UNSET)

        truncated = d.pop("truncated", UNSET)

        mt5_tick_page = cls(
            ticks=ticks,
            total=total,
            truncated=truncated,
        )

        return mt5_tick_page

