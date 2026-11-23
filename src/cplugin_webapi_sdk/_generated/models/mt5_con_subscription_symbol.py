from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_subscription_symbol_level import MT5SubscriptionSymbolLevel
from ..models.mt5_subscription_tick_history import MT5SubscriptionTickHistory
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5ConSubscriptionSymbol")



@_attrs_define
class MT5ConSubscriptionSymbol:
    """ A trading instrument covered by a subscription configuration.

        Attributes:
            symbol (None | str | Unset): Name of the trading instrument, including its group path.
            level (MT5SubscriptionSymbolLevel | None | Unset): Depth of the price history available by the
                subscription.<br/>One of: Delayed, RealtimeLevel1, RealtimeLevel2. Case-insensitive; the numeric value is
                accepted too. Any other value is refused with error code Validation.
            tick_history (MT5SubscriptionTickHistory | None | Unset): Depth of the tick history available by the
                subscription.<br/>One of: None, LastDay, LastWeek, LastMonth, Last3Months, Last6Months, LastYear, Last2Years,
                Last3Years, Last5Years, All. Case-insensitive; the numeric value is accepted too. Any other value is refused
                with error code Validation.
     """

    symbol: None | str | Unset = UNSET
    level: MT5SubscriptionSymbolLevel | None | Unset = UNSET
    tick_history: MT5SubscriptionTickHistory | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        level: None | str | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        elif isinstance(self.level, MT5SubscriptionSymbolLevel):
            level = self.level.value
        else:
            level = self.level

        tick_history: None | str | Unset
        if isinstance(self.tick_history, Unset):
            tick_history = UNSET
        elif isinstance(self.tick_history, MT5SubscriptionTickHistory):
            tick_history = self.tick_history.value
        else:
            tick_history = self.tick_history


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if level is not UNSET:
            field_dict["level"] = level
        if tick_history is not UNSET:
            field_dict["tickHistory"] = tick_history

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


        def _parse_level(data: object) -> MT5SubscriptionSymbolLevel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                level_type_1 = MT5SubscriptionSymbolLevel(data)



                return level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SubscriptionSymbolLevel | None | Unset, data)

        level = _parse_level(d.pop("level", UNSET))


        def _parse_tick_history(data: object) -> MT5SubscriptionTickHistory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tick_history_type_1 = MT5SubscriptionTickHistory(data)



                return tick_history_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SubscriptionTickHistory | None | Unset, data)

        tick_history = _parse_tick_history(d.pop("tickHistory", UNSET))


        mt5_con_subscription_symbol = cls(
            symbol=symbol,
            level=level,
            tick_history=tick_history,
        )

        return mt5_con_subscription_symbol

