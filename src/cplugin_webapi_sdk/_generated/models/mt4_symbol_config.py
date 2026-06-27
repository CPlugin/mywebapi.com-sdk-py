from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4SymbolConfig")



@_attrs_define
class MT4SymbolConfig:
    """ v2 DTO for a symbol's full server-side configuration. Curated from
    `ConSymbol`; drops reserved / unused arrays and the nested
    `Sessions` table (planned as its own endpoint).

    Seven wrapper enum fields (`TradeMode`, `ProfitCalculationMode`,
    `SymbolExecMode`, `SwapType`, `GTCMode`,
    `MarginCalculationMode`) are exposed as strings; see
    feedback-stj-enum-leaf-nested for why the conversion happens at the mapper.

        Attributes:
            symbol (None | str | Unset): Symbol name (max 12 chars)
            description (None | str | Unset): Human-readable description
            source (None | str | Unset): Data feed source identifier
            currency (None | str | Unset): Quote currency code
            type_ (int | Unset): Symbol type identifier
            digits (int | Unset): Number of decimal digits in the quote
            trade_mode (None | str | Unset): Trading mode (Disabled / CloseOnly / Full)
            background_color (int | Unset): Background colour for terminal client (BGR int)
            count (int | Unset): Tick counter for the symbol (computed)
            count_original (int | Unset): Original tick counter (computed)
            realtime (int | Unset): 0 = synthetic, non-zero = real-time feed
            starting (datetime.datetime | Unset): Symbol activation date (UTC)
            expiration (datetime.datetime | Unset): Symbol expiration date (UTC)
            profit_calculation_mode (None | str | Unset): Profit calculation mode (Forex / CFD / Futures)
            filter_ (int | Unset): Tick filter type
            filter_counter (int | Unset): Tick filter counter (computed)
            filter_limit (float | Unset): Tick filter price-change limit
            filter_smoothing (int | Unset): Tick filter smoothing factor
            logging (int | Unset): 0 = no logging, non-zero = log price changes
            spread (int | Unset): Spread in points (0 = floating)
            spread_balance (int | Unset): Spread balance correction
            symbol_exec_mode (None | str | Unset): Symbol execution mode
            swap_enable (int | Unset): 0 = swaps disabled, non-zero = enabled
            swap_type (None | str | Unset): Swap type (Points / SymbolBase / SymbolMargin / CurrencyMargin)
            swap_long (float | Unset): Swap value for long positions
            swap_short (float | Unset): Swap value for short positions
            swap_rollover_3_days (int | Unset): Day of week (1-7) when 3-day rollover applies
            contract_size (float | Unset): Contract size
            tick_value (float | Unset): Tick value in deposit currency
            tick_size (float | Unset): Tick size
            stops_level (int | Unset): Minimum distance to current price for SL/TP (points)
            gtc_mode (None | str | Unset): Pending order GTC mode
            margin_calculation_mode (None | str | Unset): Margin calculation mode (Forex / CFD / Futures / CFDIndex /
                CFDLeverage)
            margin_initial (float | Unset): Initial margin per lot
            margin_maintenance (float | Unset): Maintenance margin per lot
            margin_hedged (float | Unset): Hedged margin per lot
            margin_divider (float | Unset): Margin divider
            percentage (float | Unset): Percentage
            point (float | Unset): Point size
            multiply (float | Unset): Multiplier
            bid_tick_value (float | Unset): Bid tick value
            ask_tick_value (float | Unset): Ask tick value
            long_only (int | Unset): 0 = long+short, non-zero = long-only
            instant_max_volume (int | Unset): Max instant-execution volume (lots, 0 = unlimited)
            margin_currency (None | str | Unset): Margin currency for non-deposit-currency symbols
            freeze_level (int | Unset): Freeze level (points before expiration to freeze trading)
            margin_hedged_strong (int | Unset): Strong hedge margin per lot
            value_date (datetime.datetime | Unset): Value date (UTC)
            quotes_delay (int | Unset): Quotes delay in seconds (0 = real time)
            swap_open_price (int | Unset): 0 = standard, non-zero = use open price for swaps
            swap_variation_margin (int | Unset): 0 = swap, non-zero = variation margin
     """

    symbol: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    type_: int | Unset = UNSET
    digits: int | Unset = UNSET
    trade_mode: None | str | Unset = UNSET
    background_color: int | Unset = UNSET
    count: int | Unset = UNSET
    count_original: int | Unset = UNSET
    realtime: int | Unset = UNSET
    starting: datetime.datetime | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    profit_calculation_mode: None | str | Unset = UNSET
    filter_: int | Unset = UNSET
    filter_counter: int | Unset = UNSET
    filter_limit: float | Unset = UNSET
    filter_smoothing: int | Unset = UNSET
    logging: int | Unset = UNSET
    spread: int | Unset = UNSET
    spread_balance: int | Unset = UNSET
    symbol_exec_mode: None | str | Unset = UNSET
    swap_enable: int | Unset = UNSET
    swap_type: None | str | Unset = UNSET
    swap_long: float | Unset = UNSET
    swap_short: float | Unset = UNSET
    swap_rollover_3_days: int | Unset = UNSET
    contract_size: float | Unset = UNSET
    tick_value: float | Unset = UNSET
    tick_size: float | Unset = UNSET
    stops_level: int | Unset = UNSET
    gtc_mode: None | str | Unset = UNSET
    margin_calculation_mode: None | str | Unset = UNSET
    margin_initial: float | Unset = UNSET
    margin_maintenance: float | Unset = UNSET
    margin_hedged: float | Unset = UNSET
    margin_divider: float | Unset = UNSET
    percentage: float | Unset = UNSET
    point: float | Unset = UNSET
    multiply: float | Unset = UNSET
    bid_tick_value: float | Unset = UNSET
    ask_tick_value: float | Unset = UNSET
    long_only: int | Unset = UNSET
    instant_max_volume: int | Unset = UNSET
    margin_currency: None | str | Unset = UNSET
    freeze_level: int | Unset = UNSET
    margin_hedged_strong: int | Unset = UNSET
    value_date: datetime.datetime | Unset = UNSET
    quotes_delay: int | Unset = UNSET
    swap_open_price: int | Unset = UNSET
    swap_variation_margin: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        type_ = self.type_

        digits = self.digits

        trade_mode: None | str | Unset
        if isinstance(self.trade_mode, Unset):
            trade_mode = UNSET
        else:
            trade_mode = self.trade_mode

        background_color = self.background_color

        count = self.count

        count_original = self.count_original

        realtime = self.realtime

        starting: str | Unset = UNSET
        if not isinstance(self.starting, Unset):
            starting = self.starting.isoformat()

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        profit_calculation_mode: None | str | Unset
        if isinstance(self.profit_calculation_mode, Unset):
            profit_calculation_mode = UNSET
        else:
            profit_calculation_mode = self.profit_calculation_mode

        filter_ = self.filter_

        filter_counter = self.filter_counter

        filter_limit = self.filter_limit

        filter_smoothing = self.filter_smoothing

        logging = self.logging

        spread = self.spread

        spread_balance = self.spread_balance

        symbol_exec_mode: None | str | Unset
        if isinstance(self.symbol_exec_mode, Unset):
            symbol_exec_mode = UNSET
        else:
            symbol_exec_mode = self.symbol_exec_mode

        swap_enable = self.swap_enable

        swap_type: None | str | Unset
        if isinstance(self.swap_type, Unset):
            swap_type = UNSET
        else:
            swap_type = self.swap_type

        swap_long = self.swap_long

        swap_short = self.swap_short

        swap_rollover_3_days = self.swap_rollover_3_days

        contract_size = self.contract_size

        tick_value = self.tick_value

        tick_size = self.tick_size

        stops_level = self.stops_level

        gtc_mode: None | str | Unset
        if isinstance(self.gtc_mode, Unset):
            gtc_mode = UNSET
        else:
            gtc_mode = self.gtc_mode

        margin_calculation_mode: None | str | Unset
        if isinstance(self.margin_calculation_mode, Unset):
            margin_calculation_mode = UNSET
        else:
            margin_calculation_mode = self.margin_calculation_mode

        margin_initial = self.margin_initial

        margin_maintenance = self.margin_maintenance

        margin_hedged = self.margin_hedged

        margin_divider = self.margin_divider

        percentage = self.percentage

        point = self.point

        multiply = self.multiply

        bid_tick_value = self.bid_tick_value

        ask_tick_value = self.ask_tick_value

        long_only = self.long_only

        instant_max_volume = self.instant_max_volume

        margin_currency: None | str | Unset
        if isinstance(self.margin_currency, Unset):
            margin_currency = UNSET
        else:
            margin_currency = self.margin_currency

        freeze_level = self.freeze_level

        margin_hedged_strong = self.margin_hedged_strong

        value_date: str | Unset = UNSET
        if not isinstance(self.value_date, Unset):
            value_date = self.value_date.isoformat()

        quotes_delay = self.quotes_delay

        swap_open_price = self.swap_open_price

        swap_variation_margin = self.swap_variation_margin


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type_ is not UNSET:
            field_dict["type"] = type_
        if digits is not UNSET:
            field_dict["digits"] = digits
        if trade_mode is not UNSET:
            field_dict["tradeMode"] = trade_mode
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if count is not UNSET:
            field_dict["count"] = count
        if count_original is not UNSET:
            field_dict["countOriginal"] = count_original
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if starting is not UNSET:
            field_dict["starting"] = starting
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if profit_calculation_mode is not UNSET:
            field_dict["profitCalculationMode"] = profit_calculation_mode
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_counter is not UNSET:
            field_dict["filterCounter"] = filter_counter
        if filter_limit is not UNSET:
            field_dict["filterLimit"] = filter_limit
        if filter_smoothing is not UNSET:
            field_dict["filterSmoothing"] = filter_smoothing
        if logging is not UNSET:
            field_dict["logging"] = logging
        if spread is not UNSET:
            field_dict["spread"] = spread
        if spread_balance is not UNSET:
            field_dict["spreadBalance"] = spread_balance
        if symbol_exec_mode is not UNSET:
            field_dict["symbolExecMode"] = symbol_exec_mode
        if swap_enable is not UNSET:
            field_dict["swapEnable"] = swap_enable
        if swap_type is not UNSET:
            field_dict["swapType"] = swap_type
        if swap_long is not UNSET:
            field_dict["swapLong"] = swap_long
        if swap_short is not UNSET:
            field_dict["swapShort"] = swap_short
        if swap_rollover_3_days is not UNSET:
            field_dict["swapRollover3Days"] = swap_rollover_3_days
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if tick_value is not UNSET:
            field_dict["tickValue"] = tick_value
        if tick_size is not UNSET:
            field_dict["tickSize"] = tick_size
        if stops_level is not UNSET:
            field_dict["stopsLevel"] = stops_level
        if gtc_mode is not UNSET:
            field_dict["gtcMode"] = gtc_mode
        if margin_calculation_mode is not UNSET:
            field_dict["marginCalculationMode"] = margin_calculation_mode
        if margin_initial is not UNSET:
            field_dict["marginInitial"] = margin_initial
        if margin_maintenance is not UNSET:
            field_dict["marginMaintenance"] = margin_maintenance
        if margin_hedged is not UNSET:
            field_dict["marginHedged"] = margin_hedged
        if margin_divider is not UNSET:
            field_dict["marginDivider"] = margin_divider
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if point is not UNSET:
            field_dict["point"] = point
        if multiply is not UNSET:
            field_dict["multiply"] = multiply
        if bid_tick_value is not UNSET:
            field_dict["bidTickValue"] = bid_tick_value
        if ask_tick_value is not UNSET:
            field_dict["askTickValue"] = ask_tick_value
        if long_only is not UNSET:
            field_dict["longOnly"] = long_only
        if instant_max_volume is not UNSET:
            field_dict["instantMaxVolume"] = instant_max_volume
        if margin_currency is not UNSET:
            field_dict["marginCurrency"] = margin_currency
        if freeze_level is not UNSET:
            field_dict["freezeLevel"] = freeze_level
        if margin_hedged_strong is not UNSET:
            field_dict["marginHedgedStrong"] = margin_hedged_strong
        if value_date is not UNSET:
            field_dict["valueDate"] = value_date
        if quotes_delay is not UNSET:
            field_dict["quotesDelay"] = quotes_delay
        if swap_open_price is not UNSET:
            field_dict["swapOpenPrice"] = swap_open_price
        if swap_variation_margin is not UNSET:
            field_dict["swapVariationMargin"] = swap_variation_margin

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


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        type_ = d.pop("type", UNSET)

        digits = d.pop("digits", UNSET)

        def _parse_trade_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_mode = _parse_trade_mode(d.pop("tradeMode", UNSET))


        background_color = d.pop("backgroundColor", UNSET)

        count = d.pop("count", UNSET)

        count_original = d.pop("countOriginal", UNSET)

        realtime = d.pop("realtime", UNSET)

        _starting = d.pop("starting", UNSET)
        starting: datetime.datetime | Unset
        if isinstance(_starting,  Unset):
            starting = UNSET
        else:
            starting = datetime.datetime.fromisoformat(_starting)




        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration,  Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)




        def _parse_profit_calculation_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profit_calculation_mode = _parse_profit_calculation_mode(d.pop("profitCalculationMode", UNSET))


        filter_ = d.pop("filter", UNSET)

        filter_counter = d.pop("filterCounter", UNSET)

        filter_limit = d.pop("filterLimit", UNSET)

        filter_smoothing = d.pop("filterSmoothing", UNSET)

        logging = d.pop("logging", UNSET)

        spread = d.pop("spread", UNSET)

        spread_balance = d.pop("spreadBalance", UNSET)

        def _parse_symbol_exec_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_exec_mode = _parse_symbol_exec_mode(d.pop("symbolExecMode", UNSET))


        swap_enable = d.pop("swapEnable", UNSET)

        def _parse_swap_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        swap_type = _parse_swap_type(d.pop("swapType", UNSET))


        swap_long = d.pop("swapLong", UNSET)

        swap_short = d.pop("swapShort", UNSET)

        swap_rollover_3_days = d.pop("swapRollover3Days", UNSET)

        contract_size = d.pop("contractSize", UNSET)

        tick_value = d.pop("tickValue", UNSET)

        tick_size = d.pop("tickSize", UNSET)

        stops_level = d.pop("stopsLevel", UNSET)

        def _parse_gtc_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gtc_mode = _parse_gtc_mode(d.pop("gtcMode", UNSET))


        def _parse_margin_calculation_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        margin_calculation_mode = _parse_margin_calculation_mode(d.pop("marginCalculationMode", UNSET))


        margin_initial = d.pop("marginInitial", UNSET)

        margin_maintenance = d.pop("marginMaintenance", UNSET)

        margin_hedged = d.pop("marginHedged", UNSET)

        margin_divider = d.pop("marginDivider", UNSET)

        percentage = d.pop("percentage", UNSET)

        point = d.pop("point", UNSET)

        multiply = d.pop("multiply", UNSET)

        bid_tick_value = d.pop("bidTickValue", UNSET)

        ask_tick_value = d.pop("askTickValue", UNSET)

        long_only = d.pop("longOnly", UNSET)

        instant_max_volume = d.pop("instantMaxVolume", UNSET)

        def _parse_margin_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        margin_currency = _parse_margin_currency(d.pop("marginCurrency", UNSET))


        freeze_level = d.pop("freezeLevel", UNSET)

        margin_hedged_strong = d.pop("marginHedgedStrong", UNSET)

        _value_date = d.pop("valueDate", UNSET)
        value_date: datetime.datetime | Unset
        if isinstance(_value_date,  Unset):
            value_date = UNSET
        else:
            value_date = datetime.datetime.fromisoformat(_value_date)




        quotes_delay = d.pop("quotesDelay", UNSET)

        swap_open_price = d.pop("swapOpenPrice", UNSET)

        swap_variation_margin = d.pop("swapVariationMargin", UNSET)

        mt4_symbol_config = cls(
            symbol=symbol,
            description=description,
            source=source,
            currency=currency,
            type_=type_,
            digits=digits,
            trade_mode=trade_mode,
            background_color=background_color,
            count=count,
            count_original=count_original,
            realtime=realtime,
            starting=starting,
            expiration=expiration,
            profit_calculation_mode=profit_calculation_mode,
            filter_=filter_,
            filter_counter=filter_counter,
            filter_limit=filter_limit,
            filter_smoothing=filter_smoothing,
            logging=logging,
            spread=spread,
            spread_balance=spread_balance,
            symbol_exec_mode=symbol_exec_mode,
            swap_enable=swap_enable,
            swap_type=swap_type,
            swap_long=swap_long,
            swap_short=swap_short,
            swap_rollover_3_days=swap_rollover_3_days,
            contract_size=contract_size,
            tick_value=tick_value,
            tick_size=tick_size,
            stops_level=stops_level,
            gtc_mode=gtc_mode,
            margin_calculation_mode=margin_calculation_mode,
            margin_initial=margin_initial,
            margin_maintenance=margin_maintenance,
            margin_hedged=margin_hedged,
            margin_divider=margin_divider,
            percentage=percentage,
            point=point,
            multiply=multiply,
            bid_tick_value=bid_tick_value,
            ask_tick_value=ask_tick_value,
            long_only=long_only,
            instant_max_volume=instant_max_volume,
            margin_currency=margin_currency,
            freeze_level=freeze_level,
            margin_hedged_strong=margin_hedged_strong,
            value_date=value_date,
            quotes_delay=quotes_delay,
            swap_open_price=swap_open_price,
            swap_variation_margin=swap_variation_margin,
        )

        return mt4_symbol_config

