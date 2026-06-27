from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_calc_mode import EnCalcMode
from ..models.en_chart_mode import EnChartMode
from ..models.en_execution_mode import EnExecutionMode
from ..models.en_expiration_flags import EnExpirationFlags
from ..models.en_filling_flags import EnFillingFlags
from ..models.en_gtc_mode import EnGtcMode
from ..models.en_industries import EnIndustries
from ..models.en_instant_flags import EnInstantFlags
from ..models.en_instant_mode import EnInstantMode
from ..models.en_margin_flags import EnMarginFlags
from ..models.en_option_mode import EnOptionMode
from ..models.en_order_flags import EnOrderFlags
from ..models.en_request_flags import EnRequestFlags
from ..models.en_sectors import EnSectors
from ..models.en_splice_time_type import EnSpliceTimeType
from ..models.en_splice_type import EnSpliceType
from ..models.en_swap_days import EnSwapDays
from ..models.en_swap_flags import EnSwapFlags
from ..models.en_swap_mode import EnSwapMode
from ..models.en_tick_flags import EnTickFlags
from ..models.en_trade_flags import EnTradeFlags
from ..models.en_trade_mode import EnTradeMode
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.mt5_symbol_margin_rate_initial_type_0 import MT5SymbolMarginRateInitialType0
  from ..models.mt5_symbol_margin_rate_maintenance_type_0 import MT5SymbolMarginRateMaintenanceType0
  from ..models.mt5_symbol_session import MT5SymbolSession





T = TypeVar("T", bound="MT5Symbol")



@_attrs_define
class MT5Symbol:
    """ 
        Attributes:
            symbol (None | str | Unset): name
            path (None | str | Unset): hierarchical symbol path (including symbol name)
            isin (None | str | Unset): ISIN
            description (None | str | Unset): local description
            international (None | str | Unset): internation description
            basis (None | str | Unset): basic symbol name
            source (None | str | Unset): source symbol name
            page (None | str | Unset): symbol specification page URL
            currency_base (None | str | Unset): symbol base currency
            currency_base_digits (int | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
            currency_profit (None | str | Unset): symbol profit currency
            currency_profit_digits (int | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
            currency_margin (None | str | Unset): symbol margin currency
            currency_margin_digits (int | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
            color (int | None | Unset): symbol color
            color_background (int | None | Unset): symbol background color
            digits (int | None | Unset): symbol digits
            point (float | None | Unset):
            multiply (float | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
            tick_flags (EnTickFlags | None | Unset): EnTickFlags
            tick_book_depth (int | None | Unset): Depth of Market depth (both legs)
            filter_soft (int | None | Unset): filtration soft level
            filter_soft_ticks (int | None | Unset): filtration soft level counter
            filter_hard (int | None | Unset): filtration hard level
            filter_hard_ticks (int | None | Unset): filtration hard level counter
            filter_discard (int | None | Unset): filtration discard level
            filter_spread_max (int | None | Unset): spread max value
            filter_spread_min (int | None | Unset): spread min value
            trade_mode (EnTradeMode | None | Unset): EnTradeMode
            calc_mode (EnCalcMode | None | Unset): EnCalcMode
            exec_mode (EnExecutionMode | None | Unset): EnExecutionMode
            gtc_mode (EnGtcMode | None | Unset): EnGTCMode
            fill_flags (EnFillingFlags | None | Unset): EnFillingFlags
            expir_flags (EnExpirationFlags | None | Unset): EnExpirationFlags
            spread (int | None | Unset): symbol spread (0-floating)
            spread_balance (int | None | Unset): spread balance
            spread_diff (int | None | Unset): spread difference
            spread_diff_balance (int | None | Unset): spread difference balance
            tick_value (float | None | Unset): tick value
            tick_size (float | None | Unset): tick size
            contract_size (float | None | Unset): contract size
            stops_level (int | None | Unset): stops level
            freeze_level (int | None | Unset): freeze level
            quotes_timeout (int | None | Unset): The time to wait for quotes in seconds, after which trading is
                automatically disabled for the symbol.
            volume_min (int | None | Unset): minimal volume
            volume_max (int | None | Unset): maximal volume
            volume_step (int | None | Unset): volume step
            volume_limit (int | None | Unset): cumulative positions and orders limit
            margin_flags (EnMarginFlags | None | Unset): EnMarginFlags
            margin_initial (float | None | Unset): initial margin
            margin_maintenance (float | None | Unset): maintenance margin
            margin_long (float | None | Unset): long orders and positions margin rate
            margin_short (float | None | Unset): short orders and positions margin rate
            margin_limit (float | None | Unset): limit orders and positions margin rate
            margin_stop (float | None | Unset): stop orders and positions margin rate
            margin_stop_limit (float | None | Unset): stop-limit orders and positions margin rate
            swap_mode (EnSwapMode | None | Unset): EnSwapMode
            swap_long (float | None | Unset): long positions swaps rate
            swap_short (float | None | Unset): short positions swaps rate
            swap_3_day (EnSwapDays | None | Unset): 3 time swaps day, EnSwapDay
            time_start (datetime.datetime | None | Unset): trade start date
            time_expiration (datetime.datetime | None | Unset): The date of trading expiration for a symbol.<br />
                It is considered that there is no time limitation for trading by a symbol if both IMTConSymbol::TimeStart and
                IMTConSymbol::TimeExpiration are equal to 0.
            session_quote (list[list[MT5SymbolSession]] | None | Unset): <strong>Not yet implemented. Contact us for further
                information</strong>
                <br />
                <br />
                            Update a quoting session of a symbol by the day and index. The day is specified by a value 0
                (Sunday) to 6 (Saturday).
            session_trade (list[list[MT5SymbolSession]] | None | Unset): <strong>Not yet implemented. Contact us for further
                information</strong>
                <br />
                <br />
            re_flags (EnRequestFlags | None | Unset): request execution flags
            re_timeout (int | None | Unset): Time in seconds during which the price issued by a dealer in the request
                execution mode is valid.
            ie_check_mode (EnInstantMode | None | Unset): instant execution check mode
            ie_timeout (int | None | Unset): Get and set the maximum allowed difference between the time of arrival of the
                price, at which the client places an order, and the time of the last price.
            ie_slip_profit (int | None | Unset): instant execution profit slippage
            ie_slip_losing (int | None | Unset): instant execution losing slippage
            ie_volume_max (int | None | Unset): instant execution max volume
            price_settle (float | None | Unset): settle price (for futures)
            price_limit_max (float | None | Unset): price limit max (for futures)
            price_limit_min (float | None | Unset): price limit min (for futures)
            trade_flags (EnTradeFlags | None | Unset): EnTradeFlags
            order_flags (EnOrderFlags | None | Unset): EnOrderFlags
            margin_rate_initial (MT5SymbolMarginRateInitialType0 | None | Unset): orders and positions margin rates
            margin_rate_maintenance (MT5SymbolMarginRateMaintenanceType0 | None | Unset): orders and positions margin rates
            options_mode (EnOptionMode | None | Unset): options mode EnOptionMode
            price_strike (float | None | Unset): option strike price value
            margin_rate_liquidity (float | None | Unset): liquidity rate
            face_value (float | None | Unset): bond face value
            accrued_interest (float | None | Unset): bond accrued interest
            splice_type (EnSpliceType | None | Unset): futures splice type EnSpliceType
            splice_time_type (EnSpliceTimeType | None | Unset): futures splice time type EnSpliceType
            splice_time_days (int | None | Unset): The splicing shift as a number of days to the past from the symbol's
                expiration date IMTConSymbol::TimeExpiration
            margin_hedged (float | None | Unset): hedged positions margin rate
            margin_rate_currency (float | None | Unset): currency rate
            filter_gap (int | None | Unset): gap level
            filter_gap_ticks (int | None | Unset): gap level ticks
            chart_mode (EnChartMode | None | Unset): chart mode
            ie_flags (EnInstantFlags | None | Unset): instant execution flags with extended accuracy
            volume_min_ext (int | None | Unset): minimal volume with extended accuracy
            volume_max_ext (int | None | Unset): maximal volume with extended accuracy
            volume_step_ext (int | None | Unset): volume step with extended accuracy
            volume_limit_ext (int | None | Unset): cumulative positions and orders limit with extended accuracy
            ie_volume_max_ext (int | None | Unset): instant execution max volume with extended accuracy
            category (None | str | Unset): category
            exchange (None | str | Unset): exchange
            cfi (None | str | Unset): CFI
            sector (EnSectors | None | Unset): Sector
            industry (EnIndustries | None | Unset): Industry
            country (None | str | Unset): Country - ISO 3166-1 alpha-3 code
            subscriptions_delay (int | None | Unset): Delay for subscriptions
            swap_year_days (int | None | Unset): Days in year
            swap_flags (EnSwapFlags | None | Unset): swap flags
            swap_rate_sunday (float | None | Unset): swap rate for Sunday
            swap_rate_monday (float | None | Unset): swap rate for Monday
            swap_rate_tuesday (float | None | Unset): swap rate for Tuesday
            swap_rate_wednesday (float | None | Unset): swap rate for Wednesday
            swap_rate_thursday (float | None | Unset): swap rate for Thursday
            swap_rate_friday (float | None | Unset): swap rate for Friday
            swap_rate_saturday (float | None | Unset): swap rate for Saturday
     """

    symbol: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    isin: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    international: None | str | Unset = UNSET
    basis: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    page: None | str | Unset = UNSET
    currency_base: None | str | Unset = UNSET
    currency_base_digits: int | None | Unset = UNSET
    currency_profit: None | str | Unset = UNSET
    currency_profit_digits: int | None | Unset = UNSET
    currency_margin: None | str | Unset = UNSET
    currency_margin_digits: int | None | Unset = UNSET
    color: int | None | Unset = UNSET
    color_background: int | None | Unset = UNSET
    digits: int | None | Unset = UNSET
    point: float | None | Unset = UNSET
    multiply: float | None | Unset = UNSET
    tick_flags: EnTickFlags | None | Unset = UNSET
    tick_book_depth: int | None | Unset = UNSET
    filter_soft: int | None | Unset = UNSET
    filter_soft_ticks: int | None | Unset = UNSET
    filter_hard: int | None | Unset = UNSET
    filter_hard_ticks: int | None | Unset = UNSET
    filter_discard: int | None | Unset = UNSET
    filter_spread_max: int | None | Unset = UNSET
    filter_spread_min: int | None | Unset = UNSET
    trade_mode: EnTradeMode | None | Unset = UNSET
    calc_mode: EnCalcMode | None | Unset = UNSET
    exec_mode: EnExecutionMode | None | Unset = UNSET
    gtc_mode: EnGtcMode | None | Unset = UNSET
    fill_flags: EnFillingFlags | None | Unset = UNSET
    expir_flags: EnExpirationFlags | None | Unset = UNSET
    spread: int | None | Unset = UNSET
    spread_balance: int | None | Unset = UNSET
    spread_diff: int | None | Unset = UNSET
    spread_diff_balance: int | None | Unset = UNSET
    tick_value: float | None | Unset = UNSET
    tick_size: float | None | Unset = UNSET
    contract_size: float | None | Unset = UNSET
    stops_level: int | None | Unset = UNSET
    freeze_level: int | None | Unset = UNSET
    quotes_timeout: int | None | Unset = UNSET
    volume_min: int | None | Unset = UNSET
    volume_max: int | None | Unset = UNSET
    volume_step: int | None | Unset = UNSET
    volume_limit: int | None | Unset = UNSET
    margin_flags: EnMarginFlags | None | Unset = UNSET
    margin_initial: float | None | Unset = UNSET
    margin_maintenance: float | None | Unset = UNSET
    margin_long: float | None | Unset = UNSET
    margin_short: float | None | Unset = UNSET
    margin_limit: float | None | Unset = UNSET
    margin_stop: float | None | Unset = UNSET
    margin_stop_limit: float | None | Unset = UNSET
    swap_mode: EnSwapMode | None | Unset = UNSET
    swap_long: float | None | Unset = UNSET
    swap_short: float | None | Unset = UNSET
    swap_3_day: EnSwapDays | None | Unset = UNSET
    time_start: datetime.datetime | None | Unset = UNSET
    time_expiration: datetime.datetime | None | Unset = UNSET
    session_quote: list[list[MT5SymbolSession]] | None | Unset = UNSET
    session_trade: list[list[MT5SymbolSession]] | None | Unset = UNSET
    re_flags: EnRequestFlags | None | Unset = UNSET
    re_timeout: int | None | Unset = UNSET
    ie_check_mode: EnInstantMode | None | Unset = UNSET
    ie_timeout: int | None | Unset = UNSET
    ie_slip_profit: int | None | Unset = UNSET
    ie_slip_losing: int | None | Unset = UNSET
    ie_volume_max: int | None | Unset = UNSET
    price_settle: float | None | Unset = UNSET
    price_limit_max: float | None | Unset = UNSET
    price_limit_min: float | None | Unset = UNSET
    trade_flags: EnTradeFlags | None | Unset = UNSET
    order_flags: EnOrderFlags | None | Unset = UNSET
    margin_rate_initial: MT5SymbolMarginRateInitialType0 | None | Unset = UNSET
    margin_rate_maintenance: MT5SymbolMarginRateMaintenanceType0 | None | Unset = UNSET
    options_mode: EnOptionMode | None | Unset = UNSET
    price_strike: float | None | Unset = UNSET
    margin_rate_liquidity: float | None | Unset = UNSET
    face_value: float | None | Unset = UNSET
    accrued_interest: float | None | Unset = UNSET
    splice_type: EnSpliceType | None | Unset = UNSET
    splice_time_type: EnSpliceTimeType | None | Unset = UNSET
    splice_time_days: int | None | Unset = UNSET
    margin_hedged: float | None | Unset = UNSET
    margin_rate_currency: float | None | Unset = UNSET
    filter_gap: int | None | Unset = UNSET
    filter_gap_ticks: int | None | Unset = UNSET
    chart_mode: EnChartMode | None | Unset = UNSET
    ie_flags: EnInstantFlags | None | Unset = UNSET
    volume_min_ext: int | None | Unset = UNSET
    volume_max_ext: int | None | Unset = UNSET
    volume_step_ext: int | None | Unset = UNSET
    volume_limit_ext: int | None | Unset = UNSET
    ie_volume_max_ext: int | None | Unset = UNSET
    category: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    cfi: None | str | Unset = UNSET
    sector: EnSectors | None | Unset = UNSET
    industry: EnIndustries | None | Unset = UNSET
    country: None | str | Unset = UNSET
    subscriptions_delay: int | None | Unset = UNSET
    swap_year_days: int | None | Unset = UNSET
    swap_flags: EnSwapFlags | None | Unset = UNSET
    swap_rate_sunday: float | None | Unset = UNSET
    swap_rate_monday: float | None | Unset = UNSET
    swap_rate_tuesday: float | None | Unset = UNSET
    swap_rate_wednesday: float | None | Unset = UNSET
    swap_rate_thursday: float | None | Unset = UNSET
    swap_rate_friday: float | None | Unset = UNSET
    swap_rate_saturday: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_symbol_margin_rate_initial_type_0 import MT5SymbolMarginRateInitialType0
        from ..models.mt5_symbol_margin_rate_maintenance_type_0 import MT5SymbolMarginRateMaintenanceType0
        from ..models.mt5_symbol_session import MT5SymbolSession
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        isin: None | str | Unset
        if isinstance(self.isin, Unset):
            isin = UNSET
        else:
            isin = self.isin

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        international: None | str | Unset
        if isinstance(self.international, Unset):
            international = UNSET
        else:
            international = self.international

        basis: None | str | Unset
        if isinstance(self.basis, Unset):
            basis = UNSET
        else:
            basis = self.basis

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        page: None | str | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        currency_base: None | str | Unset
        if isinstance(self.currency_base, Unset):
            currency_base = UNSET
        else:
            currency_base = self.currency_base

        currency_base_digits: int | None | Unset
        if isinstance(self.currency_base_digits, Unset):
            currency_base_digits = UNSET
        else:
            currency_base_digits = self.currency_base_digits

        currency_profit: None | str | Unset
        if isinstance(self.currency_profit, Unset):
            currency_profit = UNSET
        else:
            currency_profit = self.currency_profit

        currency_profit_digits: int | None | Unset
        if isinstance(self.currency_profit_digits, Unset):
            currency_profit_digits = UNSET
        else:
            currency_profit_digits = self.currency_profit_digits

        currency_margin: None | str | Unset
        if isinstance(self.currency_margin, Unset):
            currency_margin = UNSET
        else:
            currency_margin = self.currency_margin

        currency_margin_digits: int | None | Unset
        if isinstance(self.currency_margin_digits, Unset):
            currency_margin_digits = UNSET
        else:
            currency_margin_digits = self.currency_margin_digits

        color: int | None | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        color_background: int | None | Unset
        if isinstance(self.color_background, Unset):
            color_background = UNSET
        else:
            color_background = self.color_background

        digits: int | None | Unset
        if isinstance(self.digits, Unset):
            digits = UNSET
        else:
            digits = self.digits

        point: float | None | Unset
        if isinstance(self.point, Unset):
            point = UNSET
        else:
            point = self.point

        multiply: float | None | Unset
        if isinstance(self.multiply, Unset):
            multiply = UNSET
        else:
            multiply = self.multiply

        tick_flags: None | str | Unset
        if isinstance(self.tick_flags, Unset):
            tick_flags = UNSET
        elif isinstance(self.tick_flags, EnTickFlags):
            tick_flags = self.tick_flags.value
        else:
            tick_flags = self.tick_flags

        tick_book_depth: int | None | Unset
        if isinstance(self.tick_book_depth, Unset):
            tick_book_depth = UNSET
        else:
            tick_book_depth = self.tick_book_depth

        filter_soft: int | None | Unset
        if isinstance(self.filter_soft, Unset):
            filter_soft = UNSET
        else:
            filter_soft = self.filter_soft

        filter_soft_ticks: int | None | Unset
        if isinstance(self.filter_soft_ticks, Unset):
            filter_soft_ticks = UNSET
        else:
            filter_soft_ticks = self.filter_soft_ticks

        filter_hard: int | None | Unset
        if isinstance(self.filter_hard, Unset):
            filter_hard = UNSET
        else:
            filter_hard = self.filter_hard

        filter_hard_ticks: int | None | Unset
        if isinstance(self.filter_hard_ticks, Unset):
            filter_hard_ticks = UNSET
        else:
            filter_hard_ticks = self.filter_hard_ticks

        filter_discard: int | None | Unset
        if isinstance(self.filter_discard, Unset):
            filter_discard = UNSET
        else:
            filter_discard = self.filter_discard

        filter_spread_max: int | None | Unset
        if isinstance(self.filter_spread_max, Unset):
            filter_spread_max = UNSET
        else:
            filter_spread_max = self.filter_spread_max

        filter_spread_min: int | None | Unset
        if isinstance(self.filter_spread_min, Unset):
            filter_spread_min = UNSET
        else:
            filter_spread_min = self.filter_spread_min

        trade_mode: None | str | Unset
        if isinstance(self.trade_mode, Unset):
            trade_mode = UNSET
        elif isinstance(self.trade_mode, EnTradeMode):
            trade_mode = self.trade_mode.value
        else:
            trade_mode = self.trade_mode

        calc_mode: None | str | Unset
        if isinstance(self.calc_mode, Unset):
            calc_mode = UNSET
        elif isinstance(self.calc_mode, EnCalcMode):
            calc_mode = self.calc_mode.value
        else:
            calc_mode = self.calc_mode

        exec_mode: None | str | Unset
        if isinstance(self.exec_mode, Unset):
            exec_mode = UNSET
        elif isinstance(self.exec_mode, EnExecutionMode):
            exec_mode = self.exec_mode.value
        else:
            exec_mode = self.exec_mode

        gtc_mode: None | str | Unset
        if isinstance(self.gtc_mode, Unset):
            gtc_mode = UNSET
        elif isinstance(self.gtc_mode, EnGtcMode):
            gtc_mode = self.gtc_mode.value
        else:
            gtc_mode = self.gtc_mode

        fill_flags: None | str | Unset
        if isinstance(self.fill_flags, Unset):
            fill_flags = UNSET
        elif isinstance(self.fill_flags, EnFillingFlags):
            fill_flags = self.fill_flags.value
        else:
            fill_flags = self.fill_flags

        expir_flags: None | str | Unset
        if isinstance(self.expir_flags, Unset):
            expir_flags = UNSET
        elif isinstance(self.expir_flags, EnExpirationFlags):
            expir_flags = self.expir_flags.value
        else:
            expir_flags = self.expir_flags

        spread: int | None | Unset
        if isinstance(self.spread, Unset):
            spread = UNSET
        else:
            spread = self.spread

        spread_balance: int | None | Unset
        if isinstance(self.spread_balance, Unset):
            spread_balance = UNSET
        else:
            spread_balance = self.spread_balance

        spread_diff: int | None | Unset
        if isinstance(self.spread_diff, Unset):
            spread_diff = UNSET
        else:
            spread_diff = self.spread_diff

        spread_diff_balance: int | None | Unset
        if isinstance(self.spread_diff_balance, Unset):
            spread_diff_balance = UNSET
        else:
            spread_diff_balance = self.spread_diff_balance

        tick_value: float | None | Unset
        if isinstance(self.tick_value, Unset):
            tick_value = UNSET
        else:
            tick_value = self.tick_value

        tick_size: float | None | Unset
        if isinstance(self.tick_size, Unset):
            tick_size = UNSET
        else:
            tick_size = self.tick_size

        contract_size: float | None | Unset
        if isinstance(self.contract_size, Unset):
            contract_size = UNSET
        else:
            contract_size = self.contract_size

        stops_level: int | None | Unset
        if isinstance(self.stops_level, Unset):
            stops_level = UNSET
        else:
            stops_level = self.stops_level

        freeze_level: int | None | Unset
        if isinstance(self.freeze_level, Unset):
            freeze_level = UNSET
        else:
            freeze_level = self.freeze_level

        quotes_timeout: int | None | Unset
        if isinstance(self.quotes_timeout, Unset):
            quotes_timeout = UNSET
        else:
            quotes_timeout = self.quotes_timeout

        volume_min: int | None | Unset
        if isinstance(self.volume_min, Unset):
            volume_min = UNSET
        else:
            volume_min = self.volume_min

        volume_max: int | None | Unset
        if isinstance(self.volume_max, Unset):
            volume_max = UNSET
        else:
            volume_max = self.volume_max

        volume_step: int | None | Unset
        if isinstance(self.volume_step, Unset):
            volume_step = UNSET
        else:
            volume_step = self.volume_step

        volume_limit: int | None | Unset
        if isinstance(self.volume_limit, Unset):
            volume_limit = UNSET
        else:
            volume_limit = self.volume_limit

        margin_flags: None | str | Unset
        if isinstance(self.margin_flags, Unset):
            margin_flags = UNSET
        elif isinstance(self.margin_flags, EnMarginFlags):
            margin_flags = self.margin_flags.value
        else:
            margin_flags = self.margin_flags

        margin_initial: float | None | Unset
        if isinstance(self.margin_initial, Unset):
            margin_initial = UNSET
        else:
            margin_initial = self.margin_initial

        margin_maintenance: float | None | Unset
        if isinstance(self.margin_maintenance, Unset):
            margin_maintenance = UNSET
        else:
            margin_maintenance = self.margin_maintenance

        margin_long: float | None | Unset
        if isinstance(self.margin_long, Unset):
            margin_long = UNSET
        else:
            margin_long = self.margin_long

        margin_short: float | None | Unset
        if isinstance(self.margin_short, Unset):
            margin_short = UNSET
        else:
            margin_short = self.margin_short

        margin_limit: float | None | Unset
        if isinstance(self.margin_limit, Unset):
            margin_limit = UNSET
        else:
            margin_limit = self.margin_limit

        margin_stop: float | None | Unset
        if isinstance(self.margin_stop, Unset):
            margin_stop = UNSET
        else:
            margin_stop = self.margin_stop

        margin_stop_limit: float | None | Unset
        if isinstance(self.margin_stop_limit, Unset):
            margin_stop_limit = UNSET
        else:
            margin_stop_limit = self.margin_stop_limit

        swap_mode: None | str | Unset
        if isinstance(self.swap_mode, Unset):
            swap_mode = UNSET
        elif isinstance(self.swap_mode, EnSwapMode):
            swap_mode = self.swap_mode.value
        else:
            swap_mode = self.swap_mode

        swap_long: float | None | Unset
        if isinstance(self.swap_long, Unset):
            swap_long = UNSET
        else:
            swap_long = self.swap_long

        swap_short: float | None | Unset
        if isinstance(self.swap_short, Unset):
            swap_short = UNSET
        else:
            swap_short = self.swap_short

        swap_3_day: None | str | Unset
        if isinstance(self.swap_3_day, Unset):
            swap_3_day = UNSET
        elif isinstance(self.swap_3_day, EnSwapDays):
            swap_3_day = self.swap_3_day.value
        else:
            swap_3_day = self.swap_3_day

        time_start: None | str | Unset
        if isinstance(self.time_start, Unset):
            time_start = UNSET
        elif isinstance(self.time_start, datetime.datetime):
            time_start = self.time_start.isoformat()
        else:
            time_start = self.time_start

        time_expiration: None | str | Unset
        if isinstance(self.time_expiration, Unset):
            time_expiration = UNSET
        elif isinstance(self.time_expiration, datetime.datetime):
            time_expiration = self.time_expiration.isoformat()
        else:
            time_expiration = self.time_expiration

        session_quote: list[list[dict[str, Any]]] | None | Unset
        if isinstance(self.session_quote, Unset):
            session_quote = UNSET
        elif isinstance(self.session_quote, list):
            session_quote = []
            for session_quote_type_0_item_data in self.session_quote:
                session_quote_type_0_item = []
                for session_quote_type_0_item_item_data in session_quote_type_0_item_data:
                    session_quote_type_0_item_item = session_quote_type_0_item_item_data.to_dict()
                    session_quote_type_0_item.append(session_quote_type_0_item_item)


                session_quote.append(session_quote_type_0_item)


        else:
            session_quote = self.session_quote

        session_trade: list[list[dict[str, Any]]] | None | Unset
        if isinstance(self.session_trade, Unset):
            session_trade = UNSET
        elif isinstance(self.session_trade, list):
            session_trade = []
            for session_trade_type_0_item_data in self.session_trade:
                session_trade_type_0_item = []
                for session_trade_type_0_item_item_data in session_trade_type_0_item_data:
                    session_trade_type_0_item_item = session_trade_type_0_item_item_data.to_dict()
                    session_trade_type_0_item.append(session_trade_type_0_item_item)


                session_trade.append(session_trade_type_0_item)


        else:
            session_trade = self.session_trade

        re_flags: None | str | Unset
        if isinstance(self.re_flags, Unset):
            re_flags = UNSET
        elif isinstance(self.re_flags, EnRequestFlags):
            re_flags = self.re_flags.value
        else:
            re_flags = self.re_flags

        re_timeout: int | None | Unset
        if isinstance(self.re_timeout, Unset):
            re_timeout = UNSET
        else:
            re_timeout = self.re_timeout

        ie_check_mode: None | str | Unset
        if isinstance(self.ie_check_mode, Unset):
            ie_check_mode = UNSET
        elif isinstance(self.ie_check_mode, EnInstantMode):
            ie_check_mode = self.ie_check_mode.value
        else:
            ie_check_mode = self.ie_check_mode

        ie_timeout: int | None | Unset
        if isinstance(self.ie_timeout, Unset):
            ie_timeout = UNSET
        else:
            ie_timeout = self.ie_timeout

        ie_slip_profit: int | None | Unset
        if isinstance(self.ie_slip_profit, Unset):
            ie_slip_profit = UNSET
        else:
            ie_slip_profit = self.ie_slip_profit

        ie_slip_losing: int | None | Unset
        if isinstance(self.ie_slip_losing, Unset):
            ie_slip_losing = UNSET
        else:
            ie_slip_losing = self.ie_slip_losing

        ie_volume_max: int | None | Unset
        if isinstance(self.ie_volume_max, Unset):
            ie_volume_max = UNSET
        else:
            ie_volume_max = self.ie_volume_max

        price_settle: float | None | Unset
        if isinstance(self.price_settle, Unset):
            price_settle = UNSET
        else:
            price_settle = self.price_settle

        price_limit_max: float | None | Unset
        if isinstance(self.price_limit_max, Unset):
            price_limit_max = UNSET
        else:
            price_limit_max = self.price_limit_max

        price_limit_min: float | None | Unset
        if isinstance(self.price_limit_min, Unset):
            price_limit_min = UNSET
        else:
            price_limit_min = self.price_limit_min

        trade_flags: None | str | Unset
        if isinstance(self.trade_flags, Unset):
            trade_flags = UNSET
        elif isinstance(self.trade_flags, EnTradeFlags):
            trade_flags = self.trade_flags.value
        else:
            trade_flags = self.trade_flags

        order_flags: None | str | Unset
        if isinstance(self.order_flags, Unset):
            order_flags = UNSET
        elif isinstance(self.order_flags, EnOrderFlags):
            order_flags = self.order_flags.value
        else:
            order_flags = self.order_flags

        margin_rate_initial: dict[str, Any] | None | Unset
        if isinstance(self.margin_rate_initial, Unset):
            margin_rate_initial = UNSET
        elif isinstance(self.margin_rate_initial, MT5SymbolMarginRateInitialType0):
            margin_rate_initial = self.margin_rate_initial.to_dict()
        else:
            margin_rate_initial = self.margin_rate_initial

        margin_rate_maintenance: dict[str, Any] | None | Unset
        if isinstance(self.margin_rate_maintenance, Unset):
            margin_rate_maintenance = UNSET
        elif isinstance(self.margin_rate_maintenance, MT5SymbolMarginRateMaintenanceType0):
            margin_rate_maintenance = self.margin_rate_maintenance.to_dict()
        else:
            margin_rate_maintenance = self.margin_rate_maintenance

        options_mode: None | str | Unset
        if isinstance(self.options_mode, Unset):
            options_mode = UNSET
        elif isinstance(self.options_mode, EnOptionMode):
            options_mode = self.options_mode.value
        else:
            options_mode = self.options_mode

        price_strike: float | None | Unset
        if isinstance(self.price_strike, Unset):
            price_strike = UNSET
        else:
            price_strike = self.price_strike

        margin_rate_liquidity: float | None | Unset
        if isinstance(self.margin_rate_liquidity, Unset):
            margin_rate_liquidity = UNSET
        else:
            margin_rate_liquidity = self.margin_rate_liquidity

        face_value: float | None | Unset
        if isinstance(self.face_value, Unset):
            face_value = UNSET
        else:
            face_value = self.face_value

        accrued_interest: float | None | Unset
        if isinstance(self.accrued_interest, Unset):
            accrued_interest = UNSET
        else:
            accrued_interest = self.accrued_interest

        splice_type: None | str | Unset
        if isinstance(self.splice_type, Unset):
            splice_type = UNSET
        elif isinstance(self.splice_type, EnSpliceType):
            splice_type = self.splice_type.value
        else:
            splice_type = self.splice_type

        splice_time_type: None | str | Unset
        if isinstance(self.splice_time_type, Unset):
            splice_time_type = UNSET
        elif isinstance(self.splice_time_type, EnSpliceTimeType):
            splice_time_type = self.splice_time_type.value
        else:
            splice_time_type = self.splice_time_type

        splice_time_days: int | None | Unset
        if isinstance(self.splice_time_days, Unset):
            splice_time_days = UNSET
        else:
            splice_time_days = self.splice_time_days

        margin_hedged: float | None | Unset
        if isinstance(self.margin_hedged, Unset):
            margin_hedged = UNSET
        else:
            margin_hedged = self.margin_hedged

        margin_rate_currency: float | None | Unset
        if isinstance(self.margin_rate_currency, Unset):
            margin_rate_currency = UNSET
        else:
            margin_rate_currency = self.margin_rate_currency

        filter_gap: int | None | Unset
        if isinstance(self.filter_gap, Unset):
            filter_gap = UNSET
        else:
            filter_gap = self.filter_gap

        filter_gap_ticks: int | None | Unset
        if isinstance(self.filter_gap_ticks, Unset):
            filter_gap_ticks = UNSET
        else:
            filter_gap_ticks = self.filter_gap_ticks

        chart_mode: None | str | Unset
        if isinstance(self.chart_mode, Unset):
            chart_mode = UNSET
        elif isinstance(self.chart_mode, EnChartMode):
            chart_mode = self.chart_mode.value
        else:
            chart_mode = self.chart_mode

        ie_flags: None | str | Unset
        if isinstance(self.ie_flags, Unset):
            ie_flags = UNSET
        elif isinstance(self.ie_flags, EnInstantFlags):
            ie_flags = self.ie_flags.value
        else:
            ie_flags = self.ie_flags

        volume_min_ext: int | None | Unset
        if isinstance(self.volume_min_ext, Unset):
            volume_min_ext = UNSET
        else:
            volume_min_ext = self.volume_min_ext

        volume_max_ext: int | None | Unset
        if isinstance(self.volume_max_ext, Unset):
            volume_max_ext = UNSET
        else:
            volume_max_ext = self.volume_max_ext

        volume_step_ext: int | None | Unset
        if isinstance(self.volume_step_ext, Unset):
            volume_step_ext = UNSET
        else:
            volume_step_ext = self.volume_step_ext

        volume_limit_ext: int | None | Unset
        if isinstance(self.volume_limit_ext, Unset):
            volume_limit_ext = UNSET
        else:
            volume_limit_ext = self.volume_limit_ext

        ie_volume_max_ext: int | None | Unset
        if isinstance(self.ie_volume_max_ext, Unset):
            ie_volume_max_ext = UNSET
        else:
            ie_volume_max_ext = self.ie_volume_max_ext

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        exchange: None | str | Unset
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange

        cfi: None | str | Unset
        if isinstance(self.cfi, Unset):
            cfi = UNSET
        else:
            cfi = self.cfi

        sector: None | str | Unset
        if isinstance(self.sector, Unset):
            sector = UNSET
        elif isinstance(self.sector, EnSectors):
            sector = self.sector.value
        else:
            sector = self.sector

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        elif isinstance(self.industry, EnIndustries):
            industry = self.industry.value
        else:
            industry = self.industry

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        subscriptions_delay: int | None | Unset
        if isinstance(self.subscriptions_delay, Unset):
            subscriptions_delay = UNSET
        else:
            subscriptions_delay = self.subscriptions_delay

        swap_year_days: int | None | Unset
        if isinstance(self.swap_year_days, Unset):
            swap_year_days = UNSET
        else:
            swap_year_days = self.swap_year_days

        swap_flags: None | str | Unset
        if isinstance(self.swap_flags, Unset):
            swap_flags = UNSET
        elif isinstance(self.swap_flags, EnSwapFlags):
            swap_flags = self.swap_flags.value
        else:
            swap_flags = self.swap_flags

        swap_rate_sunday: float | None | Unset
        if isinstance(self.swap_rate_sunday, Unset):
            swap_rate_sunday = UNSET
        else:
            swap_rate_sunday = self.swap_rate_sunday

        swap_rate_monday: float | None | Unset
        if isinstance(self.swap_rate_monday, Unset):
            swap_rate_monday = UNSET
        else:
            swap_rate_monday = self.swap_rate_monday

        swap_rate_tuesday: float | None | Unset
        if isinstance(self.swap_rate_tuesday, Unset):
            swap_rate_tuesday = UNSET
        else:
            swap_rate_tuesday = self.swap_rate_tuesday

        swap_rate_wednesday: float | None | Unset
        if isinstance(self.swap_rate_wednesday, Unset):
            swap_rate_wednesday = UNSET
        else:
            swap_rate_wednesday = self.swap_rate_wednesday

        swap_rate_thursday: float | None | Unset
        if isinstance(self.swap_rate_thursday, Unset):
            swap_rate_thursday = UNSET
        else:
            swap_rate_thursday = self.swap_rate_thursday

        swap_rate_friday: float | None | Unset
        if isinstance(self.swap_rate_friday, Unset):
            swap_rate_friday = UNSET
        else:
            swap_rate_friday = self.swap_rate_friday

        swap_rate_saturday: float | None | Unset
        if isinstance(self.swap_rate_saturday, Unset):
            swap_rate_saturday = UNSET
        else:
            swap_rate_saturday = self.swap_rate_saturday


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if path is not UNSET:
            field_dict["path"] = path
        if isin is not UNSET:
            field_dict["isin"] = isin
        if description is not UNSET:
            field_dict["description"] = description
        if international is not UNSET:
            field_dict["international"] = international
        if basis is not UNSET:
            field_dict["basis"] = basis
        if source is not UNSET:
            field_dict["source"] = source
        if page is not UNSET:
            field_dict["page"] = page
        if currency_base is not UNSET:
            field_dict["currencyBase"] = currency_base
        if currency_base_digits is not UNSET:
            field_dict["currencyBaseDigits"] = currency_base_digits
        if currency_profit is not UNSET:
            field_dict["currencyProfit"] = currency_profit
        if currency_profit_digits is not UNSET:
            field_dict["currencyProfitDigits"] = currency_profit_digits
        if currency_margin is not UNSET:
            field_dict["currencyMargin"] = currency_margin
        if currency_margin_digits is not UNSET:
            field_dict["currencyMarginDigits"] = currency_margin_digits
        if color is not UNSET:
            field_dict["color"] = color
        if color_background is not UNSET:
            field_dict["colorBackground"] = color_background
        if digits is not UNSET:
            field_dict["digits"] = digits
        if point is not UNSET:
            field_dict["point"] = point
        if multiply is not UNSET:
            field_dict["multiply"] = multiply
        if tick_flags is not UNSET:
            field_dict["tickFlags"] = tick_flags
        if tick_book_depth is not UNSET:
            field_dict["tickBookDepth"] = tick_book_depth
        if filter_soft is not UNSET:
            field_dict["filterSoft"] = filter_soft
        if filter_soft_ticks is not UNSET:
            field_dict["filterSoftTicks"] = filter_soft_ticks
        if filter_hard is not UNSET:
            field_dict["filterHard"] = filter_hard
        if filter_hard_ticks is not UNSET:
            field_dict["filterHardTicks"] = filter_hard_ticks
        if filter_discard is not UNSET:
            field_dict["filterDiscard"] = filter_discard
        if filter_spread_max is not UNSET:
            field_dict["filterSpreadMax"] = filter_spread_max
        if filter_spread_min is not UNSET:
            field_dict["filterSpreadMin"] = filter_spread_min
        if trade_mode is not UNSET:
            field_dict["tradeMode"] = trade_mode
        if calc_mode is not UNSET:
            field_dict["calcMode"] = calc_mode
        if exec_mode is not UNSET:
            field_dict["execMode"] = exec_mode
        if gtc_mode is not UNSET:
            field_dict["gtcMode"] = gtc_mode
        if fill_flags is not UNSET:
            field_dict["fillFlags"] = fill_flags
        if expir_flags is not UNSET:
            field_dict["expirFlags"] = expir_flags
        if spread is not UNSET:
            field_dict["spread"] = spread
        if spread_balance is not UNSET:
            field_dict["spreadBalance"] = spread_balance
        if spread_diff is not UNSET:
            field_dict["spreadDiff"] = spread_diff
        if spread_diff_balance is not UNSET:
            field_dict["spreadDiffBalance"] = spread_diff_balance
        if tick_value is not UNSET:
            field_dict["tickValue"] = tick_value
        if tick_size is not UNSET:
            field_dict["tickSize"] = tick_size
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if stops_level is not UNSET:
            field_dict["stopsLevel"] = stops_level
        if freeze_level is not UNSET:
            field_dict["freezeLevel"] = freeze_level
        if quotes_timeout is not UNSET:
            field_dict["quotesTimeout"] = quotes_timeout
        if volume_min is not UNSET:
            field_dict["volumeMin"] = volume_min
        if volume_max is not UNSET:
            field_dict["volumeMax"] = volume_max
        if volume_step is not UNSET:
            field_dict["volumeStep"] = volume_step
        if volume_limit is not UNSET:
            field_dict["volumeLimit"] = volume_limit
        if margin_flags is not UNSET:
            field_dict["marginFlags"] = margin_flags
        if margin_initial is not UNSET:
            field_dict["marginInitial"] = margin_initial
        if margin_maintenance is not UNSET:
            field_dict["marginMaintenance"] = margin_maintenance
        if margin_long is not UNSET:
            field_dict["marginLong"] = margin_long
        if margin_short is not UNSET:
            field_dict["marginShort"] = margin_short
        if margin_limit is not UNSET:
            field_dict["marginLimit"] = margin_limit
        if margin_stop is not UNSET:
            field_dict["marginStop"] = margin_stop
        if margin_stop_limit is not UNSET:
            field_dict["marginStopLimit"] = margin_stop_limit
        if swap_mode is not UNSET:
            field_dict["swapMode"] = swap_mode
        if swap_long is not UNSET:
            field_dict["swapLong"] = swap_long
        if swap_short is not UNSET:
            field_dict["swapShort"] = swap_short
        if swap_3_day is not UNSET:
            field_dict["swap3Day"] = swap_3_day
        if time_start is not UNSET:
            field_dict["timeStart"] = time_start
        if time_expiration is not UNSET:
            field_dict["timeExpiration"] = time_expiration
        if session_quote is not UNSET:
            field_dict["sessionQuote"] = session_quote
        if session_trade is not UNSET:
            field_dict["sessionTrade"] = session_trade
        if re_flags is not UNSET:
            field_dict["reFlags"] = re_flags
        if re_timeout is not UNSET:
            field_dict["reTimeout"] = re_timeout
        if ie_check_mode is not UNSET:
            field_dict["ieCheckMode"] = ie_check_mode
        if ie_timeout is not UNSET:
            field_dict["ieTimeout"] = ie_timeout
        if ie_slip_profit is not UNSET:
            field_dict["ieSlipProfit"] = ie_slip_profit
        if ie_slip_losing is not UNSET:
            field_dict["ieSlipLosing"] = ie_slip_losing
        if ie_volume_max is not UNSET:
            field_dict["ieVolumeMax"] = ie_volume_max
        if price_settle is not UNSET:
            field_dict["priceSettle"] = price_settle
        if price_limit_max is not UNSET:
            field_dict["priceLimitMax"] = price_limit_max
        if price_limit_min is not UNSET:
            field_dict["priceLimitMin"] = price_limit_min
        if trade_flags is not UNSET:
            field_dict["tradeFlags"] = trade_flags
        if order_flags is not UNSET:
            field_dict["orderFlags"] = order_flags
        if margin_rate_initial is not UNSET:
            field_dict["marginRateInitial"] = margin_rate_initial
        if margin_rate_maintenance is not UNSET:
            field_dict["marginRateMaintenance"] = margin_rate_maintenance
        if options_mode is not UNSET:
            field_dict["optionsMode"] = options_mode
        if price_strike is not UNSET:
            field_dict["priceStrike"] = price_strike
        if margin_rate_liquidity is not UNSET:
            field_dict["marginRateLiquidity"] = margin_rate_liquidity
        if face_value is not UNSET:
            field_dict["faceValue"] = face_value
        if accrued_interest is not UNSET:
            field_dict["accruedInterest"] = accrued_interest
        if splice_type is not UNSET:
            field_dict["spliceType"] = splice_type
        if splice_time_type is not UNSET:
            field_dict["spliceTimeType"] = splice_time_type
        if splice_time_days is not UNSET:
            field_dict["spliceTimeDays"] = splice_time_days
        if margin_hedged is not UNSET:
            field_dict["marginHedged"] = margin_hedged
        if margin_rate_currency is not UNSET:
            field_dict["marginRateCurrency"] = margin_rate_currency
        if filter_gap is not UNSET:
            field_dict["filterGap"] = filter_gap
        if filter_gap_ticks is not UNSET:
            field_dict["filterGapTicks"] = filter_gap_ticks
        if chart_mode is not UNSET:
            field_dict["chartMode"] = chart_mode
        if ie_flags is not UNSET:
            field_dict["ieFlags"] = ie_flags
        if volume_min_ext is not UNSET:
            field_dict["volumeMinExt"] = volume_min_ext
        if volume_max_ext is not UNSET:
            field_dict["volumeMaxExt"] = volume_max_ext
        if volume_step_ext is not UNSET:
            field_dict["volumeStepExt"] = volume_step_ext
        if volume_limit_ext is not UNSET:
            field_dict["volumeLimitExt"] = volume_limit_ext
        if ie_volume_max_ext is not UNSET:
            field_dict["ieVolumeMaxExt"] = ie_volume_max_ext
        if category is not UNSET:
            field_dict["category"] = category
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if cfi is not UNSET:
            field_dict["cfi"] = cfi
        if sector is not UNSET:
            field_dict["sector"] = sector
        if industry is not UNSET:
            field_dict["industry"] = industry
        if country is not UNSET:
            field_dict["country"] = country
        if subscriptions_delay is not UNSET:
            field_dict["subscriptionsDelay"] = subscriptions_delay
        if swap_year_days is not UNSET:
            field_dict["swapYearDays"] = swap_year_days
        if swap_flags is not UNSET:
            field_dict["swapFlags"] = swap_flags
        if swap_rate_sunday is not UNSET:
            field_dict["swapRateSunday"] = swap_rate_sunday
        if swap_rate_monday is not UNSET:
            field_dict["swapRateMonday"] = swap_rate_monday
        if swap_rate_tuesday is not UNSET:
            field_dict["swapRateTuesday"] = swap_rate_tuesday
        if swap_rate_wednesday is not UNSET:
            field_dict["swapRateWednesday"] = swap_rate_wednesday
        if swap_rate_thursday is not UNSET:
            field_dict["swapRateThursday"] = swap_rate_thursday
        if swap_rate_friday is not UNSET:
            field_dict["swapRateFriday"] = swap_rate_friday
        if swap_rate_saturday is not UNSET:
            field_dict["swapRateSaturday"] = swap_rate_saturday

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_symbol_margin_rate_initial_type_0 import MT5SymbolMarginRateInitialType0
        from ..models.mt5_symbol_margin_rate_maintenance_type_0 import MT5SymbolMarginRateMaintenanceType0
        from ..models.mt5_symbol_session import MT5SymbolSession
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))


        def _parse_isin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isin = _parse_isin(d.pop("isin", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_international(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        international = _parse_international(d.pop("international", UNSET))


        def _parse_basis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basis = _parse_basis(d.pop("basis", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page = _parse_page(d.pop("page", UNSET))


        def _parse_currency_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_base = _parse_currency_base(d.pop("currencyBase", UNSET))


        def _parse_currency_base_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_base_digits = _parse_currency_base_digits(d.pop("currencyBaseDigits", UNSET))


        def _parse_currency_profit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_profit = _parse_currency_profit(d.pop("currencyProfit", UNSET))


        def _parse_currency_profit_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_profit_digits = _parse_currency_profit_digits(d.pop("currencyProfitDigits", UNSET))


        def _parse_currency_margin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_margin = _parse_currency_margin(d.pop("currencyMargin", UNSET))


        def _parse_currency_margin_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_margin_digits = _parse_currency_margin_digits(d.pop("currencyMarginDigits", UNSET))


        def _parse_color(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        color = _parse_color(d.pop("color", UNSET))


        def _parse_color_background(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        color_background = _parse_color_background(d.pop("colorBackground", UNSET))


        def _parse_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits = _parse_digits(d.pop("digits", UNSET))


        def _parse_point(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point = _parse_point(d.pop("point", UNSET))


        def _parse_multiply(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        multiply = _parse_multiply(d.pop("multiply", UNSET))


        def _parse_tick_flags(data: object) -> EnTickFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tick_flags_type_1 = EnTickFlags(data)



                return tick_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnTickFlags | None | Unset, data)

        tick_flags = _parse_tick_flags(d.pop("tickFlags", UNSET))


        def _parse_tick_book_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tick_book_depth = _parse_tick_book_depth(d.pop("tickBookDepth", UNSET))


        def _parse_filter_soft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_soft = _parse_filter_soft(d.pop("filterSoft", UNSET))


        def _parse_filter_soft_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_soft_ticks = _parse_filter_soft_ticks(d.pop("filterSoftTicks", UNSET))


        def _parse_filter_hard(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_hard = _parse_filter_hard(d.pop("filterHard", UNSET))


        def _parse_filter_hard_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_hard_ticks = _parse_filter_hard_ticks(d.pop("filterHardTicks", UNSET))


        def _parse_filter_discard(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_discard = _parse_filter_discard(d.pop("filterDiscard", UNSET))


        def _parse_filter_spread_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_spread_max = _parse_filter_spread_max(d.pop("filterSpreadMax", UNSET))


        def _parse_filter_spread_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_spread_min = _parse_filter_spread_min(d.pop("filterSpreadMin", UNSET))


        def _parse_trade_mode(data: object) -> EnTradeMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trade_mode_type_1 = EnTradeMode(data)



                return trade_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnTradeMode | None | Unset, data)

        trade_mode = _parse_trade_mode(d.pop("tradeMode", UNSET))


        def _parse_calc_mode(data: object) -> EnCalcMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                calc_mode_type_1 = EnCalcMode(data)



                return calc_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCalcMode | None | Unset, data)

        calc_mode = _parse_calc_mode(d.pop("calcMode", UNSET))


        def _parse_exec_mode(data: object) -> EnExecutionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exec_mode_type_1 = EnExecutionMode(data)



                return exec_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnExecutionMode | None | Unset, data)

        exec_mode = _parse_exec_mode(d.pop("execMode", UNSET))


        def _parse_gtc_mode(data: object) -> EnGtcMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gtc_mode_type_1 = EnGtcMode(data)



                return gtc_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnGtcMode | None | Unset, data)

        gtc_mode = _parse_gtc_mode(d.pop("gtcMode", UNSET))


        def _parse_fill_flags(data: object) -> EnFillingFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fill_flags_type_1 = EnFillingFlags(data)



                return fill_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnFillingFlags | None | Unset, data)

        fill_flags = _parse_fill_flags(d.pop("fillFlags", UNSET))


        def _parse_expir_flags(data: object) -> EnExpirationFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expir_flags_type_1 = EnExpirationFlags(data)



                return expir_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnExpirationFlags | None | Unset, data)

        expir_flags = _parse_expir_flags(d.pop("expirFlags", UNSET))


        def _parse_spread(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spread = _parse_spread(d.pop("spread", UNSET))


        def _parse_spread_balance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spread_balance = _parse_spread_balance(d.pop("spreadBalance", UNSET))


        def _parse_spread_diff(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spread_diff = _parse_spread_diff(d.pop("spreadDiff", UNSET))


        def _parse_spread_diff_balance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spread_diff_balance = _parse_spread_diff_balance(d.pop("spreadDiffBalance", UNSET))


        def _parse_tick_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_value = _parse_tick_value(d.pop("tickValue", UNSET))


        def _parse_tick_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_size = _parse_tick_size(d.pop("tickSize", UNSET))


        def _parse_contract_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        contract_size = _parse_contract_size(d.pop("contractSize", UNSET))


        def _parse_stops_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stops_level = _parse_stops_level(d.pop("stopsLevel", UNSET))


        def _parse_freeze_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        freeze_level = _parse_freeze_level(d.pop("freezeLevel", UNSET))


        def _parse_quotes_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quotes_timeout = _parse_quotes_timeout(d.pop("quotesTimeout", UNSET))


        def _parse_volume_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_min = _parse_volume_min(d.pop("volumeMin", UNSET))


        def _parse_volume_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_max = _parse_volume_max(d.pop("volumeMax", UNSET))


        def _parse_volume_step(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_step = _parse_volume_step(d.pop("volumeStep", UNSET))


        def _parse_volume_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_limit = _parse_volume_limit(d.pop("volumeLimit", UNSET))


        def _parse_margin_flags(data: object) -> EnMarginFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_flags_type_1 = EnMarginFlags(data)



                return margin_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnMarginFlags | None | Unset, data)

        margin_flags = _parse_margin_flags(d.pop("marginFlags", UNSET))


        def _parse_margin_initial(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_initial = _parse_margin_initial(d.pop("marginInitial", UNSET))


        def _parse_margin_maintenance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_maintenance = _parse_margin_maintenance(d.pop("marginMaintenance", UNSET))


        def _parse_margin_long(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_long = _parse_margin_long(d.pop("marginLong", UNSET))


        def _parse_margin_short(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_short = _parse_margin_short(d.pop("marginShort", UNSET))


        def _parse_margin_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_limit = _parse_margin_limit(d.pop("marginLimit", UNSET))


        def _parse_margin_stop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_stop = _parse_margin_stop(d.pop("marginStop", UNSET))


        def _parse_margin_stop_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_stop_limit = _parse_margin_stop_limit(d.pop("marginStopLimit", UNSET))


        def _parse_swap_mode(data: object) -> EnSwapMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                swap_mode_type_1 = EnSwapMode(data)



                return swap_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSwapMode | None | Unset, data)

        swap_mode = _parse_swap_mode(d.pop("swapMode", UNSET))


        def _parse_swap_long(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_long = _parse_swap_long(d.pop("swapLong", UNSET))


        def _parse_swap_short(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_short = _parse_swap_short(d.pop("swapShort", UNSET))


        def _parse_swap_3_day(data: object) -> EnSwapDays | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                swap_3_day_type_1 = EnSwapDays(data)



                return swap_3_day_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSwapDays | None | Unset, data)

        swap_3_day = _parse_swap_3_day(d.pop("swap3Day", UNSET))


        def _parse_time_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_start_type_0 = datetime.datetime.fromisoformat(data)



                return time_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_start = _parse_time_start(d.pop("timeStart", UNSET))


        def _parse_time_expiration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_expiration_type_0 = datetime.datetime.fromisoformat(data)



                return time_expiration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_expiration = _parse_time_expiration(d.pop("timeExpiration", UNSET))


        def _parse_session_quote(data: object) -> list[list[MT5SymbolSession]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                session_quote_type_0 = []
                _session_quote_type_0 = data
                for session_quote_type_0_item_data in (_session_quote_type_0):
                    session_quote_type_0_item = []
                    _session_quote_type_0_item = session_quote_type_0_item_data
                    for session_quote_type_0_item_item_data in (_session_quote_type_0_item):
                        session_quote_type_0_item_item = MT5SymbolSession.from_dict(session_quote_type_0_item_item_data)



                        session_quote_type_0_item.append(session_quote_type_0_item_item)

                    session_quote_type_0.append(session_quote_type_0_item)

                return session_quote_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[MT5SymbolSession]] | None | Unset, data)

        session_quote = _parse_session_quote(d.pop("sessionQuote", UNSET))


        def _parse_session_trade(data: object) -> list[list[MT5SymbolSession]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                session_trade_type_0 = []
                _session_trade_type_0 = data
                for session_trade_type_0_item_data in (_session_trade_type_0):
                    session_trade_type_0_item = []
                    _session_trade_type_0_item = session_trade_type_0_item_data
                    for session_trade_type_0_item_item_data in (_session_trade_type_0_item):
                        session_trade_type_0_item_item = MT5SymbolSession.from_dict(session_trade_type_0_item_item_data)



                        session_trade_type_0_item.append(session_trade_type_0_item_item)

                    session_trade_type_0.append(session_trade_type_0_item)

                return session_trade_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[MT5SymbolSession]] | None | Unset, data)

        session_trade = _parse_session_trade(d.pop("sessionTrade", UNSET))


        def _parse_re_flags(data: object) -> EnRequestFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                re_flags_type_1 = EnRequestFlags(data)



                return re_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnRequestFlags | None | Unset, data)

        re_flags = _parse_re_flags(d.pop("reFlags", UNSET))


        def _parse_re_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        re_timeout = _parse_re_timeout(d.pop("reTimeout", UNSET))


        def _parse_ie_check_mode(data: object) -> EnInstantMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ie_check_mode_type_1 = EnInstantMode(data)



                return ie_check_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnInstantMode | None | Unset, data)

        ie_check_mode = _parse_ie_check_mode(d.pop("ieCheckMode", UNSET))


        def _parse_ie_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ie_timeout = _parse_ie_timeout(d.pop("ieTimeout", UNSET))


        def _parse_ie_slip_profit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ie_slip_profit = _parse_ie_slip_profit(d.pop("ieSlipProfit", UNSET))


        def _parse_ie_slip_losing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ie_slip_losing = _parse_ie_slip_losing(d.pop("ieSlipLosing", UNSET))


        def _parse_ie_volume_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ie_volume_max = _parse_ie_volume_max(d.pop("ieVolumeMax", UNSET))


        def _parse_price_settle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_settle = _parse_price_settle(d.pop("priceSettle", UNSET))


        def _parse_price_limit_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_limit_max = _parse_price_limit_max(d.pop("priceLimitMax", UNSET))


        def _parse_price_limit_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_limit_min = _parse_price_limit_min(d.pop("priceLimitMin", UNSET))


        def _parse_trade_flags(data: object) -> EnTradeFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trade_flags_type_1 = EnTradeFlags(data)



                return trade_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnTradeFlags | None | Unset, data)

        trade_flags = _parse_trade_flags(d.pop("tradeFlags", UNSET))


        def _parse_order_flags(data: object) -> EnOrderFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_flags_type_1 = EnOrderFlags(data)



                return order_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnOrderFlags | None | Unset, data)

        order_flags = _parse_order_flags(d.pop("orderFlags", UNSET))


        def _parse_margin_rate_initial(data: object) -> MT5SymbolMarginRateInitialType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                margin_rate_initial_type_0 = MT5SymbolMarginRateInitialType0.from_dict(data)



                return margin_rate_initial_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SymbolMarginRateInitialType0 | None | Unset, data)

        margin_rate_initial = _parse_margin_rate_initial(d.pop("marginRateInitial", UNSET))


        def _parse_margin_rate_maintenance(data: object) -> MT5SymbolMarginRateMaintenanceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                margin_rate_maintenance_type_0 = MT5SymbolMarginRateMaintenanceType0.from_dict(data)



                return margin_rate_maintenance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SymbolMarginRateMaintenanceType0 | None | Unset, data)

        margin_rate_maintenance = _parse_margin_rate_maintenance(d.pop("marginRateMaintenance", UNSET))


        def _parse_options_mode(data: object) -> EnOptionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                options_mode_type_1 = EnOptionMode(data)



                return options_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnOptionMode | None | Unset, data)

        options_mode = _parse_options_mode(d.pop("optionsMode", UNSET))


        def _parse_price_strike(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_strike = _parse_price_strike(d.pop("priceStrike", UNSET))


        def _parse_margin_rate_liquidity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_rate_liquidity = _parse_margin_rate_liquidity(d.pop("marginRateLiquidity", UNSET))


        def _parse_face_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        face_value = _parse_face_value(d.pop("faceValue", UNSET))


        def _parse_accrued_interest(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        accrued_interest = _parse_accrued_interest(d.pop("accruedInterest", UNSET))


        def _parse_splice_type(data: object) -> EnSpliceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                splice_type_type_1 = EnSpliceType(data)



                return splice_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSpliceType | None | Unset, data)

        splice_type = _parse_splice_type(d.pop("spliceType", UNSET))


        def _parse_splice_time_type(data: object) -> EnSpliceTimeType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                splice_time_type_type_1 = EnSpliceTimeType(data)



                return splice_time_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSpliceTimeType | None | Unset, data)

        splice_time_type = _parse_splice_time_type(d.pop("spliceTimeType", UNSET))


        def _parse_splice_time_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        splice_time_days = _parse_splice_time_days(d.pop("spliceTimeDays", UNSET))


        def _parse_margin_hedged(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_hedged = _parse_margin_hedged(d.pop("marginHedged", UNSET))


        def _parse_margin_rate_currency(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_rate_currency = _parse_margin_rate_currency(d.pop("marginRateCurrency", UNSET))


        def _parse_filter_gap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_gap = _parse_filter_gap(d.pop("filterGap", UNSET))


        def _parse_filter_gap_ticks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_gap_ticks = _parse_filter_gap_ticks(d.pop("filterGapTicks", UNSET))


        def _parse_chart_mode(data: object) -> EnChartMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chart_mode_type_1 = EnChartMode(data)



                return chart_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnChartMode | None | Unset, data)

        chart_mode = _parse_chart_mode(d.pop("chartMode", UNSET))


        def _parse_ie_flags(data: object) -> EnInstantFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ie_flags_type_1 = EnInstantFlags(data)



                return ie_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnInstantFlags | None | Unset, data)

        ie_flags = _parse_ie_flags(d.pop("ieFlags", UNSET))


        def _parse_volume_min_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_min_ext = _parse_volume_min_ext(d.pop("volumeMinExt", UNSET))


        def _parse_volume_max_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_max_ext = _parse_volume_max_ext(d.pop("volumeMaxExt", UNSET))


        def _parse_volume_step_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_step_ext = _parse_volume_step_ext(d.pop("volumeStepExt", UNSET))


        def _parse_volume_limit_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_limit_ext = _parse_volume_limit_ext(d.pop("volumeLimitExt", UNSET))


        def _parse_ie_volume_max_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ie_volume_max_ext = _parse_ie_volume_max_ext(d.pop("ieVolumeMaxExt", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))


        def _parse_cfi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cfi = _parse_cfi(d.pop("cfi", UNSET))


        def _parse_sector(data: object) -> EnSectors | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sector_type_1 = EnSectors(data)



                return sector_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSectors | None | Unset, data)

        sector = _parse_sector(d.pop("sector", UNSET))


        def _parse_industry(data: object) -> EnIndustries | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                industry_type_1 = EnIndustries(data)



                return industry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnIndustries | None | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_subscriptions_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscriptions_delay = _parse_subscriptions_delay(d.pop("subscriptionsDelay", UNSET))


        def _parse_swap_year_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        swap_year_days = _parse_swap_year_days(d.pop("swapYearDays", UNSET))


        def _parse_swap_flags(data: object) -> EnSwapFlags | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                swap_flags_type_1 = EnSwapFlags(data)



                return swap_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnSwapFlags | None | Unset, data)

        swap_flags = _parse_swap_flags(d.pop("swapFlags", UNSET))


        def _parse_swap_rate_sunday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_sunday = _parse_swap_rate_sunday(d.pop("swapRateSunday", UNSET))


        def _parse_swap_rate_monday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_monday = _parse_swap_rate_monday(d.pop("swapRateMonday", UNSET))


        def _parse_swap_rate_tuesday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_tuesday = _parse_swap_rate_tuesday(d.pop("swapRateTuesday", UNSET))


        def _parse_swap_rate_wednesday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_wednesday = _parse_swap_rate_wednesday(d.pop("swapRateWednesday", UNSET))


        def _parse_swap_rate_thursday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_thursday = _parse_swap_rate_thursday(d.pop("swapRateThursday", UNSET))


        def _parse_swap_rate_friday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_friday = _parse_swap_rate_friday(d.pop("swapRateFriday", UNSET))


        def _parse_swap_rate_saturday(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_rate_saturday = _parse_swap_rate_saturday(d.pop("swapRateSaturday", UNSET))


        mt5_symbol = cls(
            symbol=symbol,
            path=path,
            isin=isin,
            description=description,
            international=international,
            basis=basis,
            source=source,
            page=page,
            currency_base=currency_base,
            currency_base_digits=currency_base_digits,
            currency_profit=currency_profit,
            currency_profit_digits=currency_profit_digits,
            currency_margin=currency_margin,
            currency_margin_digits=currency_margin_digits,
            color=color,
            color_background=color_background,
            digits=digits,
            point=point,
            multiply=multiply,
            tick_flags=tick_flags,
            tick_book_depth=tick_book_depth,
            filter_soft=filter_soft,
            filter_soft_ticks=filter_soft_ticks,
            filter_hard=filter_hard,
            filter_hard_ticks=filter_hard_ticks,
            filter_discard=filter_discard,
            filter_spread_max=filter_spread_max,
            filter_spread_min=filter_spread_min,
            trade_mode=trade_mode,
            calc_mode=calc_mode,
            exec_mode=exec_mode,
            gtc_mode=gtc_mode,
            fill_flags=fill_flags,
            expir_flags=expir_flags,
            spread=spread,
            spread_balance=spread_balance,
            spread_diff=spread_diff,
            spread_diff_balance=spread_diff_balance,
            tick_value=tick_value,
            tick_size=tick_size,
            contract_size=contract_size,
            stops_level=stops_level,
            freeze_level=freeze_level,
            quotes_timeout=quotes_timeout,
            volume_min=volume_min,
            volume_max=volume_max,
            volume_step=volume_step,
            volume_limit=volume_limit,
            margin_flags=margin_flags,
            margin_initial=margin_initial,
            margin_maintenance=margin_maintenance,
            margin_long=margin_long,
            margin_short=margin_short,
            margin_limit=margin_limit,
            margin_stop=margin_stop,
            margin_stop_limit=margin_stop_limit,
            swap_mode=swap_mode,
            swap_long=swap_long,
            swap_short=swap_short,
            swap_3_day=swap_3_day,
            time_start=time_start,
            time_expiration=time_expiration,
            session_quote=session_quote,
            session_trade=session_trade,
            re_flags=re_flags,
            re_timeout=re_timeout,
            ie_check_mode=ie_check_mode,
            ie_timeout=ie_timeout,
            ie_slip_profit=ie_slip_profit,
            ie_slip_losing=ie_slip_losing,
            ie_volume_max=ie_volume_max,
            price_settle=price_settle,
            price_limit_max=price_limit_max,
            price_limit_min=price_limit_min,
            trade_flags=trade_flags,
            order_flags=order_flags,
            margin_rate_initial=margin_rate_initial,
            margin_rate_maintenance=margin_rate_maintenance,
            options_mode=options_mode,
            price_strike=price_strike,
            margin_rate_liquidity=margin_rate_liquidity,
            face_value=face_value,
            accrued_interest=accrued_interest,
            splice_type=splice_type,
            splice_time_type=splice_time_type,
            splice_time_days=splice_time_days,
            margin_hedged=margin_hedged,
            margin_rate_currency=margin_rate_currency,
            filter_gap=filter_gap,
            filter_gap_ticks=filter_gap_ticks,
            chart_mode=chart_mode,
            ie_flags=ie_flags,
            volume_min_ext=volume_min_ext,
            volume_max_ext=volume_max_ext,
            volume_step_ext=volume_step_ext,
            volume_limit_ext=volume_limit_ext,
            ie_volume_max_ext=ie_volume_max_ext,
            category=category,
            exchange=exchange,
            cfi=cfi,
            sector=sector,
            industry=industry,
            country=country,
            subscriptions_delay=subscriptions_delay,
            swap_year_days=swap_year_days,
            swap_flags=swap_flags,
            swap_rate_sunday=swap_rate_sunday,
            swap_rate_monday=swap_rate_monday,
            swap_rate_tuesday=swap_rate_tuesday,
            swap_rate_wednesday=swap_rate_wednesday,
            swap_rate_thursday=swap_rate_thursday,
            swap_rate_friday=swap_rate_friday,
            swap_rate_saturday=swap_rate_saturday,
        )

        return mt5_symbol

