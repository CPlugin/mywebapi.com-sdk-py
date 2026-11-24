from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5LeverageTier")



@_attrs_define
class MT5LeverageTier:
    """ Tier of a floating margin rule: one range and the margin rates inside it.

        Attributes:
            range_from (float | None | Unset): Start of the range (volume or value, as the rule measures it).
            range_to (float | None | Unset): End of the range; zero means the range is open-ended.
            margin_rate_initial (float | None | Unset): Initial margin rate charged inside the range.
            margin_rate_maintenance (float | None | Unset): Maintenance margin rate charged inside the range.
     """

    range_from: float | None | Unset = UNSET
    range_to: float | None | Unset = UNSET
    margin_rate_initial: float | None | Unset = UNSET
    margin_rate_maintenance: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        range_from: float | None | Unset
        if isinstance(self.range_from, Unset):
            range_from = UNSET
        else:
            range_from = self.range_from

        range_to: float | None | Unset
        if isinstance(self.range_to, Unset):
            range_to = UNSET
        else:
            range_to = self.range_to

        margin_rate_initial: float | None | Unset
        if isinstance(self.margin_rate_initial, Unset):
            margin_rate_initial = UNSET
        else:
            margin_rate_initial = self.margin_rate_initial

        margin_rate_maintenance: float | None | Unset
        if isinstance(self.margin_rate_maintenance, Unset):
            margin_rate_maintenance = UNSET
        else:
            margin_rate_maintenance = self.margin_rate_maintenance


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if range_from is not UNSET:
            field_dict["rangeFrom"] = range_from
        if range_to is not UNSET:
            field_dict["rangeTo"] = range_to
        if margin_rate_initial is not UNSET:
            field_dict["marginRateInitial"] = margin_rate_initial
        if margin_rate_maintenance is not UNSET:
            field_dict["marginRateMaintenance"] = margin_rate_maintenance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_range_from(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_from = _parse_range_from(d.pop("rangeFrom", UNSET))


        def _parse_range_to(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_to = _parse_range_to(d.pop("rangeTo", UNSET))


        def _parse_margin_rate_initial(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_rate_initial = _parse_margin_rate_initial(d.pop("marginRateInitial", UNSET))


        def _parse_margin_rate_maintenance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_rate_maintenance = _parse_margin_rate_maintenance(d.pop("marginRateMaintenance", UNSET))


        mt5_leverage_tier = cls(
            range_from=range_from,
            range_to=range_to,
            margin_rate_initial=margin_rate_initial,
            margin_rate_maintenance=margin_rate_maintenance,
        )

        return mt5_leverage_tier

