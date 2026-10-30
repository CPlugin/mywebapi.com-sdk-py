from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_chart_bar_v2 import MT5ChartBarV2





T = TypeVar("T", bound="MT5ChartBarPage")



@_attrs_define
class MT5ChartBarPage:
    """ Bars of one chart history request, v2 read DTO.

        Attributes:
            bars (list[MT5ChartBarV2] | None | Unset): Bars of this page, ordered by time ascending.
            total (int | Unset): Total number of bars in the requested window.
            truncated (bool | Unset): True when `Total` exceeds the page and more bars were available than returned.
     """

    bars: list[MT5ChartBarV2] | None | Unset = UNSET
    total: int | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_chart_bar_v2 import MT5ChartBarV2
        bars: list[dict[str, Any]] | None | Unset
        if isinstance(self.bars, Unset):
            bars = UNSET
        elif isinstance(self.bars, list):
            bars = []
            for bars_type_0_item_data in self.bars:
                bars_type_0_item = bars_type_0_item_data.to_dict()
                bars.append(bars_type_0_item)


        else:
            bars = self.bars

        total = self.total

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bars is not UNSET:
            field_dict["bars"] = bars
        if total is not UNSET:
            field_dict["total"] = total
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_chart_bar_v2 import MT5ChartBarV2
        d = dict(src_dict)
        def _parse_bars(data: object) -> list[MT5ChartBarV2] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bars_type_0 = []
                _bars_type_0 = data
                for bars_type_0_item_data in (_bars_type_0):
                    bars_type_0_item = MT5ChartBarV2.from_dict(bars_type_0_item_data)



                    bars_type_0.append(bars_type_0_item)

                return bars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5ChartBarV2] | None | Unset, data)

        bars = _parse_bars(d.pop("bars", UNSET))


        total = d.pop("total", UNSET)

        truncated = d.pop("truncated", UNSET)

        mt5_chart_bar_page = cls(
            bars=bars,
            total=total,
            truncated=truncated,
        )

        return mt5_chart_bar_page

