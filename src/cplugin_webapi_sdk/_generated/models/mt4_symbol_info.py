from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.symbol_price_direction import SymbolPriceDirection
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4SymbolInfo")



@_attrs_define
class MT4SymbolInfo:
    """ v2 DTO describing a single symbol's market data and metadata as held in
    the wrapper's pumping cache. Curated subset of the wrapper's SymbolInfo:
    covers what clients monitoring tick feeds / building a quote panel
    actually need — current Bid/Ask, session High/Low, tick precision
    (Digits, Point), current Spread (in points), last-tick direction, and
    the last-tick timestamp. Internal bookkeeping (Count, UpdateFlag,
    Visible, SpreadBalance, Commission, CommType) is intentionally omitted:
    those are pump-side cache mechanics or broker-side commission config
    that don't belong on a real-time market-data wire.

        Attributes:
            symbol (None | str | Unset): Symbol name (e.g. "EURUSD")
            digits (int | Unset): Number of digits after decimal point for prices on this symbol
            type_ (int | Unset): Security group index this symbol belongs to (refers to ConGroupSec)
            point (float | Unset): Point size (e.g. 0.00001 for 5-digit FX); price increment per point
            spread (int | Unset): Current spread, in points
            direction (SymbolPriceDirection | Unset):
            bid (float | Unset): Current bid price
            ask (float | Unset): Current ask price
            high (float | Unset): Session high price
            low (float | Unset): Session low price
            last_time (datetime.datetime | None | Unset): Timestamp of the last tick; null when the pump has not yet
                            observed a tick for this symbol since connect.
     """

    symbol: None | str | Unset = UNSET
    digits: int | Unset = UNSET
    type_: int | Unset = UNSET
    point: float | Unset = UNSET
    spread: int | Unset = UNSET
    direction: SymbolPriceDirection | Unset = UNSET
    bid: float | Unset = UNSET
    ask: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    last_time: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        digits = self.digits

        type_ = self.type_

        point = self.point

        spread = self.spread

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        bid = self.bid

        ask = self.ask

        high = self.high

        low = self.low

        last_time: None | str | Unset
        if isinstance(self.last_time, Unset):
            last_time = UNSET
        elif isinstance(self.last_time, datetime.datetime):
            last_time = self.last_time.isoformat()
        else:
            last_time = self.last_time


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if digits is not UNSET:
            field_dict["digits"] = digits
        if type_ is not UNSET:
            field_dict["type"] = type_
        if point is not UNSET:
            field_dict["point"] = point
        if spread is not UNSET:
            field_dict["spread"] = spread
        if direction is not UNSET:
            field_dict["direction"] = direction
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if last_time is not UNSET:
            field_dict["lastTime"] = last_time

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


        digits = d.pop("digits", UNSET)

        type_ = d.pop("type", UNSET)

        point = d.pop("point", UNSET)

        spread = d.pop("spread", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: SymbolPriceDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = SymbolPriceDirection(_direction)




        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        def _parse_last_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_time_type_0 = datetime.datetime.fromisoformat(data)



                return last_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_time = _parse_last_time(d.pop("lastTime", UNSET))


        mt4_symbol_info = cls(
            symbol=symbol,
            digits=digits,
            type_=type_,
            point=point,
            spread=spread,
            direction=direction,
            bid=bid,
            ask=ask,
            high=high,
            low=low,
            last_time=last_time,
        )

        return mt4_symbol_info

