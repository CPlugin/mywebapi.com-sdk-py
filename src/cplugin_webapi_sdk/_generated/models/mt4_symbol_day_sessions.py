from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt4_symbol_session import MT4SymbolSession





T = TypeVar("T", bound="MT4SymbolDaySessions")



@_attrs_define
class MT4SymbolDaySessions:
    """ v2 DTO bundling the Quote and Trade sessions for one weekday on a symbol.
    `DayOfWeek` follows the .NET convention: 0=Sunday, 1=Monday, ..., 6=Saturday.

        Attributes:
            day_of_week (int | Unset): Day of week: 0=Sunday ... 6=Saturday (.NET DayOfWeek numeric)
            quote_overnight (int | Unset): Whether quote sessions roll over midnight
            trade_overnight (int | Unset): Whether trade sessions roll over midnight
            quote (list[MT4SymbolSession] | None | Unset): Up to three quote (price) session windows for the day
            trade (list[MT4SymbolSession] | None | Unset): Up to three trade (order acceptance) session windows for the day
     """

    day_of_week: int | Unset = UNSET
    quote_overnight: int | Unset = UNSET
    trade_overnight: int | Unset = UNSET
    quote: list[MT4SymbolSession] | None | Unset = UNSET
    trade: list[MT4SymbolSession] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt4_symbol_session import MT4SymbolSession
        day_of_week = self.day_of_week

        quote_overnight = self.quote_overnight

        trade_overnight = self.trade_overnight

        quote: list[dict[str, Any]] | None | Unset
        if isinstance(self.quote, Unset):
            quote = UNSET
        elif isinstance(self.quote, list):
            quote = []
            for quote_type_0_item_data in self.quote:
                quote_type_0_item = quote_type_0_item_data.to_dict()
                quote.append(quote_type_0_item)


        else:
            quote = self.quote

        trade: list[dict[str, Any]] | None | Unset
        if isinstance(self.trade, Unset):
            trade = UNSET
        elif isinstance(self.trade, list):
            trade = []
            for trade_type_0_item_data in self.trade:
                trade_type_0_item = trade_type_0_item_data.to_dict()
                trade.append(trade_type_0_item)


        else:
            trade = self.trade


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if quote_overnight is not UNSET:
            field_dict["quoteOvernight"] = quote_overnight
        if trade_overnight is not UNSET:
            field_dict["tradeOvernight"] = trade_overnight
        if quote is not UNSET:
            field_dict["quote"] = quote
        if trade is not UNSET:
            field_dict["trade"] = trade

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt4_symbol_session import MT4SymbolSession
        d = dict(src_dict)
        day_of_week = d.pop("dayOfWeek", UNSET)

        quote_overnight = d.pop("quoteOvernight", UNSET)

        trade_overnight = d.pop("tradeOvernight", UNSET)

        def _parse_quote(data: object) -> list[MT4SymbolSession] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                quote_type_0 = []
                _quote_type_0 = data
                for quote_type_0_item_data in (_quote_type_0):
                    quote_type_0_item = MT4SymbolSession.from_dict(quote_type_0_item_data)



                    quote_type_0.append(quote_type_0_item)

                return quote_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT4SymbolSession] | None | Unset, data)

        quote = _parse_quote(d.pop("quote", UNSET))


        def _parse_trade(data: object) -> list[MT4SymbolSession] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trade_type_0 = []
                _trade_type_0 = data
                for trade_type_0_item_data in (_trade_type_0):
                    trade_type_0_item = MT4SymbolSession.from_dict(trade_type_0_item_data)



                    trade_type_0.append(trade_type_0_item)

                return trade_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT4SymbolSession] | None | Unset, data)

        trade = _parse_trade(d.pop("trade", UNSET))


        mt4_symbol_day_sessions = cls(
            day_of_week=day_of_week,
            quote_overnight=quote_overnight,
            trade_overnight=trade_overnight,
            quote=quote,
            trade=trade,
        )

        return mt4_symbol_day_sessions

