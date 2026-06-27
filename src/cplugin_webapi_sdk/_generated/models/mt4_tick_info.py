from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4TickInfo")



@_attrs_define
class MT4TickInfo:
    """ v2 DTO describing the last known tick for a trading symbol. Pump-cached
    snapshot of bid/ask quote — for sub-second updates, prefer the SignalR
    tick stream over polling this endpoint. The wrapper's `TickInfo`
    has no additional fields; the curated DTO is 1:1 on field semantics
    with the wrapper, only the timestamp source field is renamed for
    readability (`Ctm` → `Time`).

        Attributes:
            symbol (None | str | Unset): Symbol the tick applies to (e.g. "EURUSD")
            time (datetime.datetime | Unset): Server-side tick timestamp (UTC)
            bid (float | Unset): Bid price (best price at which the broker is buying)
            ask (float | Unset): Ask price (best price at which the broker is selling)
     """

    symbol: None | str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    bid: float | Unset = UNSET
    ask: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        bid = self.bid

        ask = self.ask


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if time is not UNSET:
            field_dict["time"] = time
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask

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


        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        mt4_tick_info = cls(
            symbol=symbol,
            time=time,
            bid=bid,
            ask=ask,
        )

        return mt4_tick_info

