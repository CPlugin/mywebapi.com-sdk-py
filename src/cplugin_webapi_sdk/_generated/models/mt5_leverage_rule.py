from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_leverage_range_mode import MT5LeverageRangeMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_leverage_tier import MT5LeverageTier





T = TypeVar("T", bound="MT5LeverageRule")



@_attrs_define
class MT5LeverageRule:
    r""" One rule of a floating margin configuration.

        Attributes:
            name (None | str | Unset): Rule name, unique inside its configuration.
            description (None | str | Unset): Free-form description of the rule.
            path (None | str | Unset): Path the rule is limited to: a symbol or a group, including the subgroup
                (`Forex\EURUSD`).
                Empty means the rule applies to every symbol.
            range_mode (MT5LeverageRangeMode | None | Unset): What the tier ranges of the rule are measured in.<br/>One of:
                Volume, VolumePerSymbol, Value, ValuePerSymbol. Case-insensitive; the numeric value is accepted too. Any other
                value is refused with error code Validation.
            range_value_currency (None | str | Unset): Currency used when the ranges are measured by value; empty for volume
                ranges.
            tiers (list[MT5LeverageTier] | None | Unset): Tiers of the rule, ordered by range start.
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    range_mode: MT5LeverageRangeMode | None | Unset = UNSET
    range_value_currency: None | str | Unset = UNSET
    tiers: list[MT5LeverageTier] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_leverage_tier import MT5LeverageTier
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        range_mode: None | str | Unset
        if isinstance(self.range_mode, Unset):
            range_mode = UNSET
        elif isinstance(self.range_mode, MT5LeverageRangeMode):
            range_mode = self.range_mode.value
        else:
            range_mode = self.range_mode

        range_value_currency: None | str | Unset
        if isinstance(self.range_value_currency, Unset):
            range_value_currency = UNSET
        else:
            range_value_currency = self.range_value_currency

        tiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.tiers, Unset):
            tiers = UNSET
        elif isinstance(self.tiers, list):
            tiers = []
            for tiers_type_0_item_data in self.tiers:
                tiers_type_0_item = tiers_type_0_item_data.to_dict()
                tiers.append(tiers_type_0_item)


        else:
            tiers = self.tiers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if path is not UNSET:
            field_dict["path"] = path
        if range_mode is not UNSET:
            field_dict["rangeMode"] = range_mode
        if range_value_currency is not UNSET:
            field_dict["rangeValueCurrency"] = range_value_currency
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_leverage_tier import MT5LeverageTier
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))


        def _parse_range_mode(data: object) -> MT5LeverageRangeMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                range_mode_type_1 = MT5LeverageRangeMode(data)



                return range_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5LeverageRangeMode | None | Unset, data)

        range_mode = _parse_range_mode(d.pop("rangeMode", UNSET))


        def _parse_range_value_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        range_value_currency = _parse_range_value_currency(d.pop("rangeValueCurrency", UNSET))


        def _parse_tiers(data: object) -> list[MT5LeverageTier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tiers_type_0 = []
                _tiers_type_0 = data
                for tiers_type_0_item_data in (_tiers_type_0):
                    tiers_type_0_item = MT5LeverageTier.from_dict(tiers_type_0_item_data)



                    tiers_type_0.append(tiers_type_0_item)

                return tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5LeverageTier] | None | Unset, data)

        tiers = _parse_tiers(d.pop("tiers", UNSET))


        mt5_leverage_rule = cls(
            name=name,
            description=description,
            path=path,
            range_mode=range_mode,
            range_value_currency=range_value_currency,
            tiers=tiers,
        )

        return mt5_leverage_rule

