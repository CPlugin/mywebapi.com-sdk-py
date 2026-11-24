from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4SymbolSummary")



@_attrs_define
class MT4SymbolSummary:
    """ Aggregated position of all client and coverage orders in one symbol —
    the platform's `SymbolSummary` record.
    <br>
    The values are calculated by the trade server over the orders it holds
    at the moment of the call, not over the trade history: a summary of a
    symbol with no open orders carries zero volumes and zero profit.

        Attributes:
            symbol (None | str | Unset): Symbol name (e.g. EURUSD)
            count (int | Unset): Symbol counter — the position of the symbol in the server's symbol list
            digits (int | Unset): Symbol precision (number of digits after the decimal point)
            type_ (int | Unset): Symbol group index the symbol belongs to
            orders (int | Unset): Number of client orders in the symbol
            buy_lots (int | Unset): Client buy volume in lots ×100 (e.g. 150 means 1.50 lots)
            sell_lots (int | Unset): Client sell volume in lots ×100
            buy_price (float | Unset): Average client buy price
            sell_price (float | Unset): Average client sell price
            profit (float | Unset): Client profit in the account currency at the moment of the call
            cov_orders (int | Unset): Number of coverage (broker-side) orders in the symbol
            cov_buy_lots (int | Unset): Coverage buy volume in lots ×100
            cov_sell_lots (int | Unset): Coverage sell volume in lots ×100
            cov_buy_price (float | Unset): Average coverage buy price
            cov_sell_price (float | Unset): Average coverage sell price
            cov_profit (float | Unset): Coverage profit at the moment of the call
     """

    symbol: None | str | Unset = UNSET
    count: int | Unset = UNSET
    digits: int | Unset = UNSET
    type_: int | Unset = UNSET
    orders: int | Unset = UNSET
    buy_lots: int | Unset = UNSET
    sell_lots: int | Unset = UNSET
    buy_price: float | Unset = UNSET
    sell_price: float | Unset = UNSET
    profit: float | Unset = UNSET
    cov_orders: int | Unset = UNSET
    cov_buy_lots: int | Unset = UNSET
    cov_sell_lots: int | Unset = UNSET
    cov_buy_price: float | Unset = UNSET
    cov_sell_price: float | Unset = UNSET
    cov_profit: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        count = self.count

        digits = self.digits

        type_ = self.type_

        orders = self.orders

        buy_lots = self.buy_lots

        sell_lots = self.sell_lots

        buy_price = self.buy_price

        sell_price = self.sell_price

        profit = self.profit

        cov_orders = self.cov_orders

        cov_buy_lots = self.cov_buy_lots

        cov_sell_lots = self.cov_sell_lots

        cov_buy_price = self.cov_buy_price

        cov_sell_price = self.cov_sell_price

        cov_profit = self.cov_profit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if count is not UNSET:
            field_dict["count"] = count
        if digits is not UNSET:
            field_dict["digits"] = digits
        if type_ is not UNSET:
            field_dict["type"] = type_
        if orders is not UNSET:
            field_dict["orders"] = orders
        if buy_lots is not UNSET:
            field_dict["buyLots"] = buy_lots
        if sell_lots is not UNSET:
            field_dict["sellLots"] = sell_lots
        if buy_price is not UNSET:
            field_dict["buyPrice"] = buy_price
        if sell_price is not UNSET:
            field_dict["sellPrice"] = sell_price
        if profit is not UNSET:
            field_dict["profit"] = profit
        if cov_orders is not UNSET:
            field_dict["covOrders"] = cov_orders
        if cov_buy_lots is not UNSET:
            field_dict["covBuyLots"] = cov_buy_lots
        if cov_sell_lots is not UNSET:
            field_dict["covSellLots"] = cov_sell_lots
        if cov_buy_price is not UNSET:
            field_dict["covBuyPrice"] = cov_buy_price
        if cov_sell_price is not UNSET:
            field_dict["covSellPrice"] = cov_sell_price
        if cov_profit is not UNSET:
            field_dict["covProfit"] = cov_profit

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


        count = d.pop("count", UNSET)

        digits = d.pop("digits", UNSET)

        type_ = d.pop("type", UNSET)

        orders = d.pop("orders", UNSET)

        buy_lots = d.pop("buyLots", UNSET)

        sell_lots = d.pop("sellLots", UNSET)

        buy_price = d.pop("buyPrice", UNSET)

        sell_price = d.pop("sellPrice", UNSET)

        profit = d.pop("profit", UNSET)

        cov_orders = d.pop("covOrders", UNSET)

        cov_buy_lots = d.pop("covBuyLots", UNSET)

        cov_sell_lots = d.pop("covSellLots", UNSET)

        cov_buy_price = d.pop("covBuyPrice", UNSET)

        cov_sell_price = d.pop("covSellPrice", UNSET)

        cov_profit = d.pop("covProfit", UNSET)

        mt4_symbol_summary = cls(
            symbol=symbol,
            count=count,
            digits=digits,
            type_=type_,
            orders=orders,
            buy_lots=buy_lots,
            sell_lots=sell_lots,
            buy_price=buy_price,
            sell_price=sell_price,
            profit=profit,
            cov_orders=cov_orders,
            cov_buy_lots=cov_buy_lots,
            cov_sell_lots=cov_sell_lots,
            cov_buy_price=cov_buy_price,
            cov_sell_price=cov_sell_price,
            cov_profit=cov_profit,
        )

        return mt4_symbol_summary

