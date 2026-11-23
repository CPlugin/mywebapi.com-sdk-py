from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5MarketTickStat")



@_attrs_define
class MT5MarketTickStat:
    """ Statistical information about the quotes of a symbol.

        Attributes:
            symbol (None | str | Unset): Name of the trading instrument the statistics belong to.
            time (int | Unset): Time the statistics refer to — seconds since 01.01.1970 in the trading time of the trade
                server.
            time_msc (int | Unset): The same time in milliseconds since 01.01.1970.
            date_time (datetime.datetime | Unset): The same time as a date-time without offset, for direct reading.
            bid_high (float | Unset): Highest bid of the session.
            bid_low (float | Unset): Lowest bid of the session.
            ask_high (float | Unset): Highest ask of the session.
            ask_low (float | Unset): Lowest ask of the session.
            last_high (float | Unset): Highest last deal price of the session.
            last_low (float | Unset): Lowest last deal price of the session.
            volume_high (int | Unset): Highest deal volume of the session.
            volume_low (int | Unset): Lowest deal volume of the session.
            volume_high_ext (int | Unset): Highest deal volume of the session with extended accuracy.
            volume_low_ext (int | Unset): Lowest deal volume of the session with extended accuracy.
            trade_deals (int | Unset): Number of deals of the session.
            trade_volume (int | Unset): Volume of the deals of the session.
            trade_turnover (int | Unset): Turnover of the session.
            trade_interest (int | Unset): Volume of the effective contracts of the session.
            trade_buy_orders (int | Unset): Number of buy orders received during the session.
            trade_buy_volume (int | Unset): Volume of buy orders received during the session.
            trade_sell_orders (int | Unset): Number of sell orders received during the session.
            trade_sell_volume (int | Unset): Volume of sell orders received during the session.
            trade_volume_ext (int | Unset): Volume of the deals of the session with extended accuracy.
            trade_buy_volume_ext (int | Unset): Volume of buy orders of the session with extended accuracy.
            trade_sell_volume_ext (int | Unset): Volume of sell orders of the session with extended accuracy.
            price_open (float | Unset): Opening price of the session.
            price_close (float | Unset): Closing price of the session.
            price_aw (float | Unset): Average weighted price of the session.
            price_volatility (float | Unset): Price volatility of the session.
            price_theoretical (float | Unset): Theoretical option price.
     """

    symbol: None | str | Unset = UNSET
    time: int | Unset = UNSET
    time_msc: int | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    bid_high: float | Unset = UNSET
    bid_low: float | Unset = UNSET
    ask_high: float | Unset = UNSET
    ask_low: float | Unset = UNSET
    last_high: float | Unset = UNSET
    last_low: float | Unset = UNSET
    volume_high: int | Unset = UNSET
    volume_low: int | Unset = UNSET
    volume_high_ext: int | Unset = UNSET
    volume_low_ext: int | Unset = UNSET
    trade_deals: int | Unset = UNSET
    trade_volume: int | Unset = UNSET
    trade_turnover: int | Unset = UNSET
    trade_interest: int | Unset = UNSET
    trade_buy_orders: int | Unset = UNSET
    trade_buy_volume: int | Unset = UNSET
    trade_sell_orders: int | Unset = UNSET
    trade_sell_volume: int | Unset = UNSET
    trade_volume_ext: int | Unset = UNSET
    trade_buy_volume_ext: int | Unset = UNSET
    trade_sell_volume_ext: int | Unset = UNSET
    price_open: float | Unset = UNSET
    price_close: float | Unset = UNSET
    price_aw: float | Unset = UNSET
    price_volatility: float | Unset = UNSET
    price_theoretical: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        time = self.time

        time_msc = self.time_msc

        date_time: str | Unset = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        bid_high = self.bid_high

        bid_low = self.bid_low

        ask_high = self.ask_high

        ask_low = self.ask_low

        last_high = self.last_high

        last_low = self.last_low

        volume_high = self.volume_high

        volume_low = self.volume_low

        volume_high_ext = self.volume_high_ext

        volume_low_ext = self.volume_low_ext

        trade_deals = self.trade_deals

        trade_volume = self.trade_volume

        trade_turnover = self.trade_turnover

        trade_interest = self.trade_interest

        trade_buy_orders = self.trade_buy_orders

        trade_buy_volume = self.trade_buy_volume

        trade_sell_orders = self.trade_sell_orders

        trade_sell_volume = self.trade_sell_volume

        trade_volume_ext = self.trade_volume_ext

        trade_buy_volume_ext = self.trade_buy_volume_ext

        trade_sell_volume_ext = self.trade_sell_volume_ext

        price_open = self.price_open

        price_close = self.price_close

        price_aw = self.price_aw

        price_volatility = self.price_volatility

        price_theoretical = self.price_theoretical


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if time is not UNSET:
            field_dict["time"] = time
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if bid_high is not UNSET:
            field_dict["bidHigh"] = bid_high
        if bid_low is not UNSET:
            field_dict["bidLow"] = bid_low
        if ask_high is not UNSET:
            field_dict["askHigh"] = ask_high
        if ask_low is not UNSET:
            field_dict["askLow"] = ask_low
        if last_high is not UNSET:
            field_dict["lastHigh"] = last_high
        if last_low is not UNSET:
            field_dict["lastLow"] = last_low
        if volume_high is not UNSET:
            field_dict["volumeHigh"] = volume_high
        if volume_low is not UNSET:
            field_dict["volumeLow"] = volume_low
        if volume_high_ext is not UNSET:
            field_dict["volumeHighExt"] = volume_high_ext
        if volume_low_ext is not UNSET:
            field_dict["volumeLowExt"] = volume_low_ext
        if trade_deals is not UNSET:
            field_dict["tradeDeals"] = trade_deals
        if trade_volume is not UNSET:
            field_dict["tradeVolume"] = trade_volume
        if trade_turnover is not UNSET:
            field_dict["tradeTurnover"] = trade_turnover
        if trade_interest is not UNSET:
            field_dict["tradeInterest"] = trade_interest
        if trade_buy_orders is not UNSET:
            field_dict["tradeBuyOrders"] = trade_buy_orders
        if trade_buy_volume is not UNSET:
            field_dict["tradeBuyVolume"] = trade_buy_volume
        if trade_sell_orders is not UNSET:
            field_dict["tradeSellOrders"] = trade_sell_orders
        if trade_sell_volume is not UNSET:
            field_dict["tradeSellVolume"] = trade_sell_volume
        if trade_volume_ext is not UNSET:
            field_dict["tradeVolumeExt"] = trade_volume_ext
        if trade_buy_volume_ext is not UNSET:
            field_dict["tradeBuyVolumeExt"] = trade_buy_volume_ext
        if trade_sell_volume_ext is not UNSET:
            field_dict["tradeSellVolumeExt"] = trade_sell_volume_ext
        if price_open is not UNSET:
            field_dict["priceOpen"] = price_open
        if price_close is not UNSET:
            field_dict["priceClose"] = price_close
        if price_aw is not UNSET:
            field_dict["priceAw"] = price_aw
        if price_volatility is not UNSET:
            field_dict["priceVolatility"] = price_volatility
        if price_theoretical is not UNSET:
            field_dict["priceTheoretical"] = price_theoretical

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


        time = d.pop("time", UNSET)

        time_msc = d.pop("timeMsc", UNSET)

        _date_time = d.pop("dateTime", UNSET)
        date_time: datetime.datetime | Unset
        if isinstance(_date_time,  Unset):
            date_time = UNSET
        else:
            date_time = datetime.datetime.fromisoformat(_date_time)




        bid_high = d.pop("bidHigh", UNSET)

        bid_low = d.pop("bidLow", UNSET)

        ask_high = d.pop("askHigh", UNSET)

        ask_low = d.pop("askLow", UNSET)

        last_high = d.pop("lastHigh", UNSET)

        last_low = d.pop("lastLow", UNSET)

        volume_high = d.pop("volumeHigh", UNSET)

        volume_low = d.pop("volumeLow", UNSET)

        volume_high_ext = d.pop("volumeHighExt", UNSET)

        volume_low_ext = d.pop("volumeLowExt", UNSET)

        trade_deals = d.pop("tradeDeals", UNSET)

        trade_volume = d.pop("tradeVolume", UNSET)

        trade_turnover = d.pop("tradeTurnover", UNSET)

        trade_interest = d.pop("tradeInterest", UNSET)

        trade_buy_orders = d.pop("tradeBuyOrders", UNSET)

        trade_buy_volume = d.pop("tradeBuyVolume", UNSET)

        trade_sell_orders = d.pop("tradeSellOrders", UNSET)

        trade_sell_volume = d.pop("tradeSellVolume", UNSET)

        trade_volume_ext = d.pop("tradeVolumeExt", UNSET)

        trade_buy_volume_ext = d.pop("tradeBuyVolumeExt", UNSET)

        trade_sell_volume_ext = d.pop("tradeSellVolumeExt", UNSET)

        price_open = d.pop("priceOpen", UNSET)

        price_close = d.pop("priceClose", UNSET)

        price_aw = d.pop("priceAw", UNSET)

        price_volatility = d.pop("priceVolatility", UNSET)

        price_theoretical = d.pop("priceTheoretical", UNSET)

        mt5_market_tick_stat = cls(
            symbol=symbol,
            time=time,
            time_msc=time_msc,
            date_time=date_time,
            bid_high=bid_high,
            bid_low=bid_low,
            ask_high=ask_high,
            ask_low=ask_low,
            last_high=last_high,
            last_low=last_low,
            volume_high=volume_high,
            volume_low=volume_low,
            volume_high_ext=volume_high_ext,
            volume_low_ext=volume_low_ext,
            trade_deals=trade_deals,
            trade_volume=trade_volume,
            trade_turnover=trade_turnover,
            trade_interest=trade_interest,
            trade_buy_orders=trade_buy_orders,
            trade_buy_volume=trade_buy_volume,
            trade_sell_orders=trade_sell_orders,
            trade_sell_volume=trade_sell_volume,
            trade_volume_ext=trade_volume_ext,
            trade_buy_volume_ext=trade_buy_volume_ext,
            trade_sell_volume_ext=trade_sell_volume_ext,
            price_open=price_open,
            price_close=price_close,
            price_aw=price_aw,
            price_volatility=price_volatility,
            price_theoretical=price_theoretical,
        )

        return mt5_market_tick_stat

