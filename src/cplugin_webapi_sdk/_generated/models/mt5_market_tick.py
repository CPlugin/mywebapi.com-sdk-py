from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5MarketTick")



@_attrs_define
class MT5MarketTick:
    """ A full quote record of a symbol.

        Attributes:
            symbol (None | str | Unset): Name of the trading instrument the quote belongs to. Mandatory.
            bank (None | str | Unset): Name of the price source (liquidity provider) as the sender reports it.
            time (int | None | Unset): Quote time — seconds since 01.01.1970 in the trading time of the trade server.
            time_msc (int | None | Unset): Quote time — milliseconds since 01.01.1970 in the trading time of the trade
                server.
            bid (float | None | Unset): Bid price.
            ask (float | None | Unset): Ask price.
            last (float | None | Unset): Price of the last committed deal.
            volume (int | None | Unset): Volume of the last deal, as the data provider passed it.
            volume_ext (int | None | Unset): Volume of the last deal with extended accuracy; wins over `volume` when both
                are given.
            flags (None | str | Unset): Direction of the last deal: `None`, `Buy` or `Sell`.
     """

    symbol: None | str | Unset = UNSET
    bank: None | str | Unset = UNSET
    time: int | None | Unset = UNSET
    time_msc: int | None | Unset = UNSET
    bid: float | None | Unset = UNSET
    ask: float | None | Unset = UNSET
    last: float | None | Unset = UNSET
    volume: int | None | Unset = UNSET
    volume_ext: int | None | Unset = UNSET
    flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        bank: None | str | Unset
        if isinstance(self.bank, Unset):
            bank = UNSET
        else:
            bank = self.bank

        time: int | None | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        time_msc: int | None | Unset
        if isinstance(self.time_msc, Unset):
            time_msc = UNSET
        else:
            time_msc = self.time_msc

        bid: float | None | Unset
        if isinstance(self.bid, Unset):
            bid = UNSET
        else:
            bid = self.bid

        ask: float | None | Unset
        if isinstance(self.ask, Unset):
            ask = UNSET
        else:
            ask = self.ask

        last: float | None | Unset
        if isinstance(self.last, Unset):
            last = UNSET
        else:
            last = self.last

        volume: int | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        volume_ext: int | None | Unset
        if isinstance(self.volume_ext, Unset):
            volume_ext = UNSET
        else:
            volume_ext = self.volume_ext

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if bank is not UNSET:
            field_dict["bank"] = bank
        if time is not UNSET:
            field_dict["time"] = time
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask
        if last is not UNSET:
            field_dict["last"] = last
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext
        if flags is not UNSET:
            field_dict["flags"] = flags

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


        def _parse_bank(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank = _parse_bank(d.pop("bank", UNSET))


        def _parse_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        def _parse_time_msc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_msc = _parse_time_msc(d.pop("timeMsc", UNSET))


        def _parse_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bid = _parse_bid(d.pop("bid", UNSET))


        def _parse_ask(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ask = _parse_ask(d.pop("ask", UNSET))


        def _parse_last(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last = _parse_last(d.pop("last", UNSET))


        def _parse_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))


        def _parse_volume_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_ext = _parse_volume_ext(d.pop("volumeExt", UNSET))


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        mt5_market_tick = cls(
            symbol=symbol,
            bank=bank,
            time=time,
            time_msc=time_msc,
            bid=bid,
            ask=ask,
            last=last,
            volume=volume,
            volume_ext=volume_ext,
            flags=flags,
        )

        return mt5_market_tick

