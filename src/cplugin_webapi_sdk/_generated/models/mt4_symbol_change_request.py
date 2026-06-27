from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.symbol_exec_mode import SymbolExecMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4SymbolChangeRequest")



@_attrs_define
class MT4SymbolChangeRequest:
    """ POST body for the Manager-live `SymbolChange` endpoint. Maps 1:1 to the
    wrapper's `SymbolProperties` struct (the public properties, not the
    underscore-prefixed backing fields). The struct's 8-int `Reserved`
    padding is dropped from the v2 contract.

    <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
    stops level, smoothing, or quote-color metadata without touching the broader
    symbol configuration. Heavier write operations (currency, calc mode,
    margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.

        Attributes:
            symbol (None | str | Unset): Symbol name (max 12 chars — wrapper's fixed slot)
            color (int | Unset): Quote display color (raw int; broker UI convention)
            spread (int | Unset): Spread (in points; 0 = market spread)
            spread_balance (int | Unset): Spread imbalance offset (in points)
            stops_level (int | Unset): Minimum allowed stops distance from market (in points)
            smoothing (int | Unset): Quote-smoothing parameter (raw int; broker-defined)
            exe_mode (SymbolExecMode | Unset):
     """

    symbol: None | str | Unset = UNSET
    color: int | Unset = UNSET
    spread: int | Unset = UNSET
    spread_balance: int | Unset = UNSET
    stops_level: int | Unset = UNSET
    smoothing: int | Unset = UNSET
    exe_mode: SymbolExecMode | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        color = self.color

        spread = self.spread

        spread_balance = self.spread_balance

        stops_level = self.stops_level

        smoothing = self.smoothing

        exe_mode: str | Unset = UNSET
        if not isinstance(self.exe_mode, Unset):
            exe_mode = self.exe_mode.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if color is not UNSET:
            field_dict["color"] = color
        if spread is not UNSET:
            field_dict["spread"] = spread
        if spread_balance is not UNSET:
            field_dict["spreadBalance"] = spread_balance
        if stops_level is not UNSET:
            field_dict["stopsLevel"] = stops_level
        if smoothing is not UNSET:
            field_dict["smoothing"] = smoothing
        if exe_mode is not UNSET:
            field_dict["exeMode"] = exe_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        color = d.pop("color", UNSET)

        spread = d.pop("spread", UNSET)

        spread_balance = d.pop("spreadBalance", UNSET)

        stops_level = d.pop("stopsLevel", UNSET)

        smoothing = d.pop("smoothing", UNSET)

        _exe_mode = d.pop("exeMode", UNSET)
        exe_mode: SymbolExecMode | Unset
        if isinstance(_exe_mode,  Unset):
            exe_mode = UNSET
        else:
            exe_mode = SymbolExecMode(_exe_mode)




        mt4_symbol_change_request = cls(
            symbol=symbol,
            color=color,
            spread=spread,
            spread_balance=spread_balance,
            stops_level=stops_level,
            smoothing=smoothing,
            exe_mode=exe_mode,
        )

        return mt4_symbol_change_request

