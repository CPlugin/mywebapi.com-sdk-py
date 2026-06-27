from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.gtc_mode import GTCMode
from ..models.margin_calculation_mode import MarginCalculationMode
from ..models.profit_calculation_mode import ProfitCalculationMode
from ..models.swap_type import SwapType
from ..models.symbol_exec_mode import SymbolExecMode
from ..models.trade_mode import TradeMode
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4SymbolConfigUpdate")



@_attrs_define
class MT4SymbolConfigUpdate:
    """ Type 1 mutator input for `CfgUpdateSymbol`. Same field set as the read
    DTO CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4SymbolConfig minus:
      * `Symbol` (path parameter, immutable identity);
      * `Count`, `CountOriginal`, `FilterCounter` — server-side
        counters, derived;
      * Stringified enum fields are submitted as their original wrapper enum
        types here (one-way deserialisation accepts JsonStringEnumConverter
        via the existing global STJ options).

    Fields preserved by the server-side read step (NOT on this DTO):
      * `Symbol` identity.
      * `Sessions` nested array (own endpoint planned).
      * `Unused`, `ExternalUnused`, `ProfitReserved`,
        `FilterReserved` reserved arrays.
      * `Count`, `CountOriginal`, `FilterCounter`,
        `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
        — server-derived from other fields, writing them is a no-op or
        overwrite-with-stale.

        Attributes:
            description (None | str | Unset):
            source (None | str | Unset):
            currency (None | str | Unset):
            type_ (int | Unset):
            digits (int | Unset):
            trade_mode (TradeMode | Unset):
            background_color (int | Unset):
            realtime (int | Unset):
            starting (datetime.datetime | Unset):
            expiration (datetime.datetime | Unset):
            profit_calculation_mode (ProfitCalculationMode | Unset):
            filter_ (int | Unset):
            filter_limit (float | Unset):
            filter_smoothing (int | Unset):
            logging (int | Unset):
            spread (int | Unset):
            spread_balance (int | Unset):
            symbol_exec_mode (SymbolExecMode | Unset):
            swap_enable (int | Unset):
            swap_type (SwapType | Unset):
            swap_long (float | Unset):
            swap_short (float | Unset):
            swap_rollover_3_days (int | Unset):
            contract_size (float | Unset):
            tick_value (float | Unset):
            tick_size (float | Unset):
            stops_level (int | Unset):
            gtc_mode (GTCMode | Unset):
            margin_calculation_mode (MarginCalculationMode | Unset):
            margin_initial (float | Unset):
            margin_maintenance (float | Unset):
            margin_hedged (float | Unset):
            margin_divider (float | Unset):
            percentage (float | Unset):
            long_only (int | Unset):
            instant_max_volume (int | Unset):
            margin_currency (None | str | Unset):
            freeze_level (int | Unset):
            margin_hedged_strong (int | Unset):
            value_date (datetime.datetime | Unset):
            quotes_delay (int | Unset):
            swap_open_price (int | Unset):
            swap_variation_margin (int | Unset):
     """

    description: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    type_: int | Unset = UNSET
    digits: int | Unset = UNSET
    trade_mode: TradeMode | Unset = UNSET
    background_color: int | Unset = UNSET
    realtime: int | Unset = UNSET
    starting: datetime.datetime | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    profit_calculation_mode: ProfitCalculationMode | Unset = UNSET
    filter_: int | Unset = UNSET
    filter_limit: float | Unset = UNSET
    filter_smoothing: int | Unset = UNSET
    logging: int | Unset = UNSET
    spread: int | Unset = UNSET
    spread_balance: int | Unset = UNSET
    symbol_exec_mode: SymbolExecMode | Unset = UNSET
    swap_enable: int | Unset = UNSET
    swap_type: SwapType | Unset = UNSET
    swap_long: float | Unset = UNSET
    swap_short: float | Unset = UNSET
    swap_rollover_3_days: int | Unset = UNSET
    contract_size: float | Unset = UNSET
    tick_value: float | Unset = UNSET
    tick_size: float | Unset = UNSET
    stops_level: int | Unset = UNSET
    gtc_mode: GTCMode | Unset = UNSET
    margin_calculation_mode: MarginCalculationMode | Unset = UNSET
    margin_initial: float | Unset = UNSET
    margin_maintenance: float | Unset = UNSET
    margin_hedged: float | Unset = UNSET
    margin_divider: float | Unset = UNSET
    percentage: float | Unset = UNSET
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

        trade_mode: str | Unset = UNSET
        if not isinstance(self.trade_mode, Unset):
            trade_mode = self.trade_mode.value


        background_color = self.background_color

        realtime = self.realtime

        starting: str | Unset = UNSET
        if not isinstance(self.starting, Unset):
            starting = self.starting.isoformat()

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        profit_calculation_mode: str | Unset = UNSET
        if not isinstance(self.profit_calculation_mode, Unset):
            profit_calculation_mode = self.profit_calculation_mode.value


        filter_ = self.filter_

        filter_limit = self.filter_limit

        filter_smoothing = self.filter_smoothing

        logging = self.logging

        spread = self.spread

        spread_balance = self.spread_balance

        symbol_exec_mode: str | Unset = UNSET
        if not isinstance(self.symbol_exec_mode, Unset):
            symbol_exec_mode = self.symbol_exec_mode.value


        swap_enable = self.swap_enable

        swap_type: str | Unset = UNSET
        if not isinstance(self.swap_type, Unset):
            swap_type = self.swap_type.value


        swap_long = self.swap_long

        swap_short = self.swap_short

        swap_rollover_3_days = self.swap_rollover_3_days

        contract_size = self.contract_size

        tick_value = self.tick_value

        tick_size = self.tick_size

        stops_level = self.stops_level

        gtc_mode: str | Unset = UNSET
        if not isinstance(self.gtc_mode, Unset):
            gtc_mode = self.gtc_mode.value


        margin_calculation_mode: str | Unset = UNSET
        if not isinstance(self.margin_calculation_mode, Unset):
            margin_calculation_mode = self.margin_calculation_mode.value


        margin_initial = self.margin_initial

        margin_maintenance = self.margin_maintenance

        margin_hedged = self.margin_hedged

        margin_divider = self.margin_divider

        percentage = self.percentage

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

        _trade_mode = d.pop("tradeMode", UNSET)
        trade_mode: TradeMode | Unset
        if isinstance(_trade_mode,  Unset):
            trade_mode = UNSET
        else:
            trade_mode = TradeMode(_trade_mode)




        background_color = d.pop("backgroundColor", UNSET)

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




        _profit_calculation_mode = d.pop("profitCalculationMode", UNSET)
        profit_calculation_mode: ProfitCalculationMode | Unset
        if isinstance(_profit_calculation_mode,  Unset):
            profit_calculation_mode = UNSET
        else:
            profit_calculation_mode = ProfitCalculationMode(_profit_calculation_mode)




        filter_ = d.pop("filter", UNSET)

        filter_limit = d.pop("filterLimit", UNSET)

        filter_smoothing = d.pop("filterSmoothing", UNSET)

        logging = d.pop("logging", UNSET)

        spread = d.pop("spread", UNSET)

        spread_balance = d.pop("spreadBalance", UNSET)

        _symbol_exec_mode = d.pop("symbolExecMode", UNSET)
        symbol_exec_mode: SymbolExecMode | Unset
        if isinstance(_symbol_exec_mode,  Unset):
            symbol_exec_mode = UNSET
        else:
            symbol_exec_mode = SymbolExecMode(_symbol_exec_mode)




        swap_enable = d.pop("swapEnable", UNSET)

        _swap_type = d.pop("swapType", UNSET)
        swap_type: SwapType | Unset
        if isinstance(_swap_type,  Unset):
            swap_type = UNSET
        else:
            swap_type = SwapType(_swap_type)




        swap_long = d.pop("swapLong", UNSET)

        swap_short = d.pop("swapShort", UNSET)

        swap_rollover_3_days = d.pop("swapRollover3Days", UNSET)

        contract_size = d.pop("contractSize", UNSET)

        tick_value = d.pop("tickValue", UNSET)

        tick_size = d.pop("tickSize", UNSET)

        stops_level = d.pop("stopsLevel", UNSET)

        _gtc_mode = d.pop("gtcMode", UNSET)
        gtc_mode: GTCMode | Unset
        if isinstance(_gtc_mode,  Unset):
            gtc_mode = UNSET
        else:
            gtc_mode = GTCMode(_gtc_mode)




        _margin_calculation_mode = d.pop("marginCalculationMode", UNSET)
        margin_calculation_mode: MarginCalculationMode | Unset
        if isinstance(_margin_calculation_mode,  Unset):
            margin_calculation_mode = UNSET
        else:
            margin_calculation_mode = MarginCalculationMode(_margin_calculation_mode)




        margin_initial = d.pop("marginInitial", UNSET)

        margin_maintenance = d.pop("marginMaintenance", UNSET)

        margin_hedged = d.pop("marginHedged", UNSET)

        margin_divider = d.pop("marginDivider", UNSET)

        percentage = d.pop("percentage", UNSET)

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

        mt4_symbol_config_update = cls(
            description=description,
            source=source,
            currency=currency,
            type_=type_,
            digits=digits,
            trade_mode=trade_mode,
            background_color=background_color,
            realtime=realtime,
            starting=starting,
            expiration=expiration,
            profit_calculation_mode=profit_calculation_mode,
            filter_=filter_,
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

        return mt4_symbol_config_update

