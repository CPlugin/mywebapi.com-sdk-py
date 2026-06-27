from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt4_chart_bar import MT4ChartBar





T = TypeVar("T", bound="MT4ChartWriteRequest")



@_attrs_define
class MT4ChartWriteRequest:
    """ v2 request body for the `ChartAdd` / `ChartUpdate` / `ChartDelete`
    trio. Wraps the bars list so the request shape stays extensible — future
    metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
    change to clients that only sent `Rates`.

        Attributes:
            rates (list[MT4ChartBar] | None | Unset): OHLC bars to add / update / delete. Must be non-empty.
     """

    rates: list[MT4ChartBar] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt4_chart_bar import MT4ChartBar
        rates: list[dict[str, Any]] | None | Unset
        if isinstance(self.rates, Unset):
            rates = UNSET
        elif isinstance(self.rates, list):
            rates = []
            for rates_type_0_item_data in self.rates:
                rates_type_0_item = rates_type_0_item_data.to_dict()
                rates.append(rates_type_0_item)


        else:
            rates = self.rates


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt4_chart_bar import MT4ChartBar
        d = dict(src_dict)
        def _parse_rates(data: object) -> list[MT4ChartBar] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rates_type_0 = []
                _rates_type_0 = data
                for rates_type_0_item_data in (_rates_type_0):
                    rates_type_0_item = MT4ChartBar.from_dict(rates_type_0_item_data)



                    rates_type_0.append(rates_type_0_item)

                return rates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT4ChartBar] | None | Unset, data)

        rates = _parse_rates(d.pop("rates", UNSET))


        mt4_chart_write_request = cls(
            rates=rates,
        )

        return mt4_chart_write_request

