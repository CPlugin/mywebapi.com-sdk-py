from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_market_chart_bar import MT5MarketChartBar





T = TypeVar("T", bound="MT5MarketChartWriteRequest")



@_attrs_define
class MT5MarketChartWriteRequest:
    """ Minute bars to write into the chart history of a symbol.

        Attributes:
            bars (list[MT5MarketChartBar] | None | Unset): Bars to write. Must be non-empty.
     """

    bars: list[MT5MarketChartBar] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_market_chart_bar import MT5MarketChartBar
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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bars is not UNSET:
            field_dict["bars"] = bars

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_market_chart_bar import MT5MarketChartBar
        d = dict(src_dict)
        def _parse_bars(data: object) -> list[MT5MarketChartBar] | None | Unset:
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
                    bars_type_0_item = MT5MarketChartBar.from_dict(bars_type_0_item_data)



                    bars_type_0.append(bars_type_0_item)

                return bars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5MarketChartBar] | None | Unset, data)

        bars = _parse_bars(d.pop("bars", UNSET))


        mt5_market_chart_write_request = cls(
            bars=bars,
        )

        return mt5_market_chart_write_request

