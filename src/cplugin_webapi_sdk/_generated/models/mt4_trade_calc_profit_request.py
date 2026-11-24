from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4TradeCalcProfitRequest")



@_attrs_define
class MT4TradeCalcProfitRequest:
    """ Input of the profit calculation: the trade fields the calculation reads.
    Only these fields take part in the result — stops, magic number, comment
    and timestamps do not change it.
    <br>
    Nothing is written anywhere: the trade record is assembled in memory,
    priced against the symbol's current conversion rates, and only the
    resulting profit is returned.

        Attributes:
            login (int | Unset): Account login the trade would belong to
            symbol (None | str | Unset): Symbol of the trade (e.g. EURUSD)
            trade_command (None | str | Unset): Trade direction: `Buy` or `Sell`.<br/>One of: Buy, Sell, BuyLimit,
                SellLimit, BuyStop, SellStop, Balance, Credit. Case-insensitive; the numeric value is accepted too. Any other
                value is refused with error code Validation.
            volume (int | Unset): Volume in MT4 internal units. 1 lot = 100, so e.g. 250 = 2.5 lots.
            open_price (float | Unset): Open price of the trade
            close_price (float | Unset): Close price of the trade
     """

    login: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    trade_command: None | str | Unset = UNSET
    volume: int | Unset = UNSET
    open_price: float | Unset = UNSET
    close_price: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        trade_command: None | str | Unset
        if isinstance(self.trade_command, Unset):
            trade_command = UNSET
        else:
            trade_command = self.trade_command

        volume = self.volume

        open_price = self.open_price

        close_price = self.close_price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if trade_command is not UNSET:
            field_dict["tradeCommand"] = trade_command
        if volume is not UNSET:
            field_dict["volume"] = volume
        if open_price is not UNSET:
            field_dict["openPrice"] = open_price
        if close_price is not UNSET:
            field_dict["closePrice"] = close_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_trade_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_command = _parse_trade_command(d.pop("tradeCommand", UNSET))


        volume = d.pop("volume", UNSET)

        open_price = d.pop("openPrice", UNSET)

        close_price = d.pop("closePrice", UNSET)

        mt4_trade_calc_profit_request = cls(
            login=login,
            symbol=symbol,
            trade_command=trade_command,
            volume=volume,
            open_price=open_price,
            close_price=close_price,
        )

        return mt4_trade_calc_profit_request

