from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_comm_action_mode import EnCommActionMode
from ..models.en_comm_charge_mode import EnCommChargeMode
from ..models.en_comm_entry_mode import EnCommEntryMode
from ..models.en_comm_mode import EnCommMode
from ..models.en_comm_profit_mode import EnCommProfitMode
from ..models.en_comm_range_mode import EnCommRangeMode
from ..models.en_comm_reason_flags import EnCommReasonFlags
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_con_comm_tier import MT5ConCommTier





T = TypeVar("T", bound="MT5ConCommission")



@_attrs_define
class MT5ConCommission:
    """ 
        Attributes:
            name (None | str | Unset): commission name
            description (None | str | Unset): description
            path (None | str | Unset): symbols path
            mode (EnCommMode | None | Unset): EnCommMode
            range_mode (EnCommRangeMode | None | Unset): EnCommRangeMode
            charge_mode (EnCommChargeMode | None | Unset): EnCommChargeMode
            tiers (list[MT5ConCommTier] | None | Unset): commission tiers. Index in array from 0 means Position of the
                range.
            turnover_currency (None | str | Unset): - turnover calculation currency
            entry_mode (EnCommEntryMode | None | Unset): EnCommEntryMode
            action_mode (EnCommActionMode | None | Unset): EnCommActionMode
            profit_mode (EnCommProfitMode | None | Unset): EnCommProfitMode
            reason_flags (EnCommReasonFlags | None | Unset): EnCommReasonFlags
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    mode: EnCommMode | None | Unset = UNSET
    range_mode: EnCommRangeMode | None | Unset = UNSET
    charge_mode: EnCommChargeMode | None | Unset = UNSET
    tiers: list[MT5ConCommTier] | None | Unset = UNSET
    turnover_currency: None | str | Unset = UNSET
    entry_mode: EnCommEntryMode | None | Unset = UNSET
    action_mode: EnCommActionMode | None | Unset = UNSET
    profit_mode: EnCommProfitMode | None | Unset = UNSET
    reason_flags: EnCommReasonFlags | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_con_comm_tier import MT5ConCommTier
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

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, EnCommMode):
            mode = self.mode.value
        else:
            mode = self.mode

        range_mode: None | str | Unset
        if isinstance(self.range_mode, Unset):
            range_mode = UNSET
        elif isinstance(self.range_mode, EnCommRangeMode):
            range_mode = self.range_mode.value
        else:
            range_mode = self.range_mode

        charge_mode: None | str | Unset
        if isinstance(self.charge_mode, Unset):
            charge_mode = UNSET
        elif isinstance(self.charge_mode, EnCommChargeMode):
            charge_mode = self.charge_mode.value
        else:
            charge_mode = self.charge_mode

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

        turnover_currency: None | str | Unset
        if isinstance(self.turnover_currency, Unset):
            turnover_currency = UNSET
        else:
            turnover_currency = self.turnover_currency

        entry_mode: None | str | Unset
        if isinstance(self.entry_mode, Unset):
            entry_mode = UNSET
        elif isinstance(self.entry_mode, EnCommEntryMode):
            entry_mode = self.entry_mode.value
        else:
            entry_mode = self.entry_mode

        action_mode: None | str | Unset
        if isinstance(self.action_mode, Unset):
            action_mode = UNSET
        elif isinstance(self.action_mode, EnCommActionMode):
            action_mode = self.action_mode.value
        else:
            action_mode = self.action_mode

        profit_mode: None | str | Unset
        if isinstance(self.profit_mode, Unset):
            profit_mode = UNSET
        elif isinstance(self.profit_mode, EnCommProfitMode):
            profit_mode = self.profit_mode.value
        else:
            profit_mode = self.profit_mode

        reason_flags: None | str | Unset
        if isinstance(self.reason_flags, Unset):
            reason_flags = UNSET
        elif isinstance(self.reason_flags, EnCommReasonFlags):
            reason_flags = self.reason_flags.value
        else:
            reason_flags = self.reason_flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if path is not UNSET:
            field_dict["path"] = path
        if mode is not UNSET:
            field_dict["mode"] = mode
        if range_mode is not UNSET:
            field_dict["rangeMode"] = range_mode
        if charge_mode is not UNSET:
            field_dict["chargeMode"] = charge_mode
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if turnover_currency is not UNSET:
            field_dict["turnoverCurrency"] = turnover_currency
        if entry_mode is not UNSET:
            field_dict["entryMode"] = entry_mode
        if action_mode is not UNSET:
            field_dict["actionMode"] = action_mode
        if profit_mode is not UNSET:
            field_dict["profitMode"] = profit_mode
        if reason_flags is not UNSET:
            field_dict["reasonFlags"] = reason_flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_con_comm_tier import MT5ConCommTier
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


        def _parse_mode(data: object) -> EnCommMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = EnCommMode(data)



                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        def _parse_range_mode(data: object) -> EnCommRangeMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                range_mode_type_1 = EnCommRangeMode(data)



                return range_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommRangeMode | None | Unset, data)

        range_mode = _parse_range_mode(d.pop("rangeMode", UNSET))


        def _parse_charge_mode(data: object) -> EnCommChargeMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                charge_mode_type_1 = EnCommChargeMode(data)



                return charge_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommChargeMode | None | Unset, data)

        charge_mode = _parse_charge_mode(d.pop("chargeMode", UNSET))


        def _parse_tiers(data: object) -> list[MT5ConCommTier] | None | Unset:
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
                    tiers_type_0_item = MT5ConCommTier.from_dict(tiers_type_0_item_data)



                    tiers_type_0.append(tiers_type_0_item)

                return tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5ConCommTier] | None | Unset, data)

        tiers = _parse_tiers(d.pop("tiers", UNSET))


        def _parse_turnover_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        turnover_currency = _parse_turnover_currency(d.pop("turnoverCurrency", UNSET))


        def _parse_entry_mode(data: object) -> EnCommEntryMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entry_mode_type_1 = EnCommEntryMode(data)



                return entry_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommEntryMode | None | Unset, data)

        entry_mode = _parse_entry_mode(d.pop("entryMode", UNSET))


        def _parse_action_mode(data: object) -> EnCommActionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_mode_type_1 = EnCommActionMode(data)



                return action_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommActionMode | None | Unset, data)

        action_mode = _parse_action_mode(d.pop("actionMode", UNSET))


        def _parse_profit_mode(data: object) -> EnCommProfitMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profit_mode_type_1 = EnCommProfitMode(data)



                return profit_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommProfitMode | None | Unset, data)

        profit_mode = _parse_profit_mode(d.pop("profitMode", UNSET))


        def _parse_reason_flags(data: object) -> EnCommReasonFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_flags_type_1 = EnCommReasonFlags(data)



                return reason_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommReasonFlags | None | Unset, data)

        reason_flags = _parse_reason_flags(d.pop("reasonFlags", UNSET))


        mt5_con_commission = cls(
            name=name,
            description=description,
            path=path,
            mode=mode,
            range_mode=range_mode,
            charge_mode=charge_mode,
            tiers=tiers,
            turnover_currency=turnover_currency,
            entry_mode=entry_mode,
            action_mode=action_mode,
            profit_mode=profit_mode,
            reason_flags=reason_flags,
        )

        return mt5_con_commission

