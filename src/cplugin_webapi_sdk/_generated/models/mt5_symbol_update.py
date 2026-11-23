from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_calc_mode import EnCalcMode
from ..models.en_execution_mode import EnExecutionMode
from ..models.en_trade_mode import EnTradeMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SymbolUpdate")



@_attrs_define
class MT5SymbolUpdate:
    """ Editable surface of a symbol record: 15 fields that are safely writable, every one optional.

        Attributes:
            description (None | str | Unset): Human-readable symbol description shown in the terminal.
            digits (int | None | Unset): Number of decimal places in the price quote.
            spread (int | None | Unset): Current spread in points (0 = floating spread).
            stops_level (int | None | Unset): Minimum stop loss / take profit distance from current price, in points.
            freeze_level (int | None | Unset): Distance from current price at which orders are frozen before execution, in
                points.
            contract_size (float | None | Unset): Contract size — units of base currency per standard lot.
            margin_initial (float | None | Unset): Initial margin requirement per lot.
            margin_maintenance (float | None | Unset): Maintenance margin requirement per lot (below this level triggers a
                margin call).
            tick_size (float | None | Unset): Minimum price change step (pip size).
            tick_value (float | None | Unset): Monetary value of one tick move for one standard lot.
            volume_min (int | None | Unset): Minimum trade volume, in MT5 volume units (1 lot = 10000 units).
            volume_max (int | None | Unset): Maximum trade volume, in MT5 volume units (1 lot = 10000 units).
            trade_mode (EnTradeMode | None | Unset): Trade mode controlling which order types are allowed (full, close-only,
                no-trading, etc.).
            calc_mode (EnCalcMode | None | Unset): Margin calculation mode (forex, futures, CFD, etc.).
            exec_mode (EnExecutionMode | None | Unset): Order execution mode (instant, market, exchange, request).
     """

    description: None | str | Unset = UNSET
    digits: int | None | Unset = UNSET
    spread: int | None | Unset = UNSET
    stops_level: int | None | Unset = UNSET
    freeze_level: int | None | Unset = UNSET
    contract_size: float | None | Unset = UNSET
    margin_initial: float | None | Unset = UNSET
    margin_maintenance: float | None | Unset = UNSET
    tick_size: float | None | Unset = UNSET
    tick_value: float | None | Unset = UNSET
    volume_min: int | None | Unset = UNSET
    volume_max: int | None | Unset = UNSET
    trade_mode: EnTradeMode | None | Unset = UNSET
    calc_mode: EnCalcMode | None | Unset = UNSET
    exec_mode: EnExecutionMode | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        digits: int | None | Unset
        if isinstance(self.digits, Unset):
            digits = UNSET
        else:
            digits = self.digits

        spread: int | None | Unset
        if isinstance(self.spread, Unset):
            spread = UNSET
        else:
            spread = self.spread

        stops_level: int | None | Unset
        if isinstance(self.stops_level, Unset):
            stops_level = UNSET
        else:
            stops_level = self.stops_level

        freeze_level: int | None | Unset
        if isinstance(self.freeze_level, Unset):
            freeze_level = UNSET
        else:
            freeze_level = self.freeze_level

        contract_size: float | None | Unset
        if isinstance(self.contract_size, Unset):
            contract_size = UNSET
        else:
            contract_size = self.contract_size

        margin_initial: float | None | Unset
        if isinstance(self.margin_initial, Unset):
            margin_initial = UNSET
        else:
            margin_initial = self.margin_initial

        margin_maintenance: float | None | Unset
        if isinstance(self.margin_maintenance, Unset):
            margin_maintenance = UNSET
        else:
            margin_maintenance = self.margin_maintenance

        tick_size: float | None | Unset
        if isinstance(self.tick_size, Unset):
            tick_size = UNSET
        else:
            tick_size = self.tick_size

        tick_value: float | None | Unset
        if isinstance(self.tick_value, Unset):
            tick_value = UNSET
        else:
            tick_value = self.tick_value

        volume_min: int | None | Unset
        if isinstance(self.volume_min, Unset):
            volume_min = UNSET
        else:
            volume_min = self.volume_min

        volume_max: int | None | Unset
        if isinstance(self.volume_max, Unset):
            volume_max = UNSET
        else:
            volume_max = self.volume_max

        trade_mode: None | str | Unset
        if isinstance(self.trade_mode, Unset):
            trade_mode = UNSET
        elif isinstance(self.trade_mode, EnTradeMode):
            trade_mode = self.trade_mode.value
        else:
            trade_mode = self.trade_mode

        calc_mode: None | str | Unset
        if isinstance(self.calc_mode, Unset):
            calc_mode = UNSET
        elif isinstance(self.calc_mode, EnCalcMode):
            calc_mode = self.calc_mode.value
        else:
            calc_mode = self.calc_mode

        exec_mode: None | str | Unset
        if isinstance(self.exec_mode, Unset):
            exec_mode = UNSET
        elif isinstance(self.exec_mode, EnExecutionMode):
            exec_mode = self.exec_mode.value
        else:
            exec_mode = self.exec_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if digits is not UNSET:
            field_dict["digits"] = digits
        if spread is not UNSET:
            field_dict["spread"] = spread
        if stops_level is not UNSET:
            field_dict["stopsLevel"] = stops_level
        if freeze_level is not UNSET:
            field_dict["freezeLevel"] = freeze_level
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if margin_initial is not UNSET:
            field_dict["marginInitial"] = margin_initial
        if margin_maintenance is not UNSET:
            field_dict["marginMaintenance"] = margin_maintenance
        if tick_size is not UNSET:
            field_dict["tickSize"] = tick_size
        if tick_value is not UNSET:
            field_dict["tickValue"] = tick_value
        if volume_min is not UNSET:
            field_dict["volumeMin"] = volume_min
        if volume_max is not UNSET:
            field_dict["volumeMax"] = volume_max
        if trade_mode is not UNSET:
            field_dict["tradeMode"] = trade_mode
        if calc_mode is not UNSET:
            field_dict["calcMode"] = calc_mode
        if exec_mode is not UNSET:
            field_dict["execMode"] = exec_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits = _parse_digits(d.pop("digits", UNSET))


        def _parse_spread(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spread = _parse_spread(d.pop("spread", UNSET))


        def _parse_stops_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stops_level = _parse_stops_level(d.pop("stopsLevel", UNSET))


        def _parse_freeze_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        freeze_level = _parse_freeze_level(d.pop("freezeLevel", UNSET))


        def _parse_contract_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        contract_size = _parse_contract_size(d.pop("contractSize", UNSET))


        def _parse_margin_initial(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_initial = _parse_margin_initial(d.pop("marginInitial", UNSET))


        def _parse_margin_maintenance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_maintenance = _parse_margin_maintenance(d.pop("marginMaintenance", UNSET))


        def _parse_tick_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_size = _parse_tick_size(d.pop("tickSize", UNSET))


        def _parse_tick_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_value = _parse_tick_value(d.pop("tickValue", UNSET))


        def _parse_volume_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_min = _parse_volume_min(d.pop("volumeMin", UNSET))


        def _parse_volume_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_max = _parse_volume_max(d.pop("volumeMax", UNSET))


        def _parse_trade_mode(data: object) -> EnTradeMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trade_mode_type_1 = EnTradeMode(data)



                return trade_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnTradeMode | None | Unset, data)

        trade_mode = _parse_trade_mode(d.pop("tradeMode", UNSET))


        def _parse_calc_mode(data: object) -> EnCalcMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                calc_mode_type_1 = EnCalcMode(data)



                return calc_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCalcMode | None | Unset, data)

        calc_mode = _parse_calc_mode(d.pop("calcMode", UNSET))


        def _parse_exec_mode(data: object) -> EnExecutionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exec_mode_type_1 = EnExecutionMode(data)



                return exec_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnExecutionMode | None | Unset, data)

        exec_mode = _parse_exec_mode(d.pop("execMode", UNSET))


        mt5_symbol_update = cls(
            description=description,
            digits=digits,
            spread=spread,
            stops_level=stops_level,
            freeze_level=freeze_level,
            contract_size=contract_size,
            margin_initial=margin_initial,
            margin_maintenance=margin_maintenance,
            tick_size=tick_size,
            tick_value=tick_value,
            volume_min=volume_min,
            volume_max=volume_max,
            trade_mode=trade_mode,
            calc_mode=calc_mode,
            exec_mode=exec_mode,
        )

        return mt5_symbol_update

