from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.deal_action import DealAction
from ..models.deal_reason import DealReason
from ..models.entry_flag import EntryFlag
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Deal")



@_attrs_define
class MT5Deal:
    """ 
        Attributes:
            deal (int): deal ticket
            external_id (None | str | Unset): deal ticket in external system (exchange, ECN, etc)
            login (int | None | Unset): client login
            dealer (int | None | Unset): processed dealer login (0-means auto)
            party_id (int | None | Unset): counterparty identification
            order (int | None | Unset): deal order ticket
            action (DealAction | None | Unset): DealAction
            entry (EntryFlag | None | Unset): EntryFlags
            digits (int | None | Unset): price digits
            digits_currency (int | None | Unset): currency digits
            contract_size (float | None | Unset): symbol contract size
            time (datetime.datetime | None | Unset): deal creation datetime in seconds. If the value of this field is
                specified, the IMTDeal::TimeMsc value will be filled in automatically.
            symbol (None | str | Unset): deal symbol
            price (float | None | Unset): deal price
            price_sl (float | None | Unset): order SL
            price_tp (float | None | Unset): order TP
            volume (int | None | Unset): deal volume
            volume_ext (int | None | Unset): deal volume with extended accuracy
            volume_closed (int | None | Unset): closed volume
            volume_closed_ext (int | None | Unset): closed volume with extended accuracy
            profit (float | None | Unset): deal profit
            value (float | None | Unset): value
            storage (float | None | Unset): deal collected swaps
            commission (float | None | Unset): deal commission
            obsolete_value (float | None | Unset): obsolete value
            fee (float | None | Unset): fee
            rate_profit (float | None | Unset): profit conversion rate (from symbol profit currency to deposit currency)
            rate_margin (float | None | Unset): margin conversion rate (from symbol margin currency to deposit currency)
            expert_id (int | None | Unset): expert id (filled by expert advisor)
            position_id (int | None | Unset): position id
            comment (None | str | Unset): deal comment
            profit_raw (float | None | Unset): deal profit in symbol's profit currency
            price_position (float | None | Unset): closed position  price
            tick_value (float | None | Unset): tick value
            tick_size (float | None | Unset): tick size
            flags (int | None | Unset): flags
            time_msc (datetime.datetime | None | Unset): deal creation datetime in msc since 1970.01.01. If the value of
                this field is specified, the IMTDeal::Time value will be filled in automatically
            reason (DealReason | None | Unset): DealReason
            gateway (None | str | Unset): source gateway name
            price_gateway (float | None | Unset): deal price on gateway
            market_bid (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            Get the market Bid price as at the time of deal execution by the server
            market_ask (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            Get the market Ask price as at the time of deal execution by the server
            market_last (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            Get the market Last price as at the time of deal execution by the server
            modification_flags (None | str | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            modification flags
     """

    deal: int
    external_id: None | str | Unset = UNSET
    login: int | None | Unset = UNSET
    dealer: int | None | Unset = UNSET
    party_id: int | None | Unset = UNSET
    order: int | None | Unset = UNSET
    action: DealAction | None | Unset = UNSET
    entry: EntryFlag | None | Unset = UNSET
    digits: int | None | Unset = UNSET
    digits_currency: int | None | Unset = UNSET
    contract_size: float | None | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    symbol: None | str | Unset = UNSET
    price: float | None | Unset = UNSET
    price_sl: float | None | Unset = UNSET
    price_tp: float | None | Unset = UNSET
    volume: int | None | Unset = UNSET
    volume_ext: int | None | Unset = UNSET
    volume_closed: int | None | Unset = UNSET
    volume_closed_ext: int | None | Unset = UNSET
    profit: float | None | Unset = UNSET
    value: float | None | Unset = UNSET
    storage: float | None | Unset = UNSET
    commission: float | None | Unset = UNSET
    obsolete_value: float | None | Unset = UNSET
    fee: float | None | Unset = UNSET
    rate_profit: float | None | Unset = UNSET
    rate_margin: float | None | Unset = UNSET
    expert_id: int | None | Unset = UNSET
    position_id: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    profit_raw: float | None | Unset = UNSET
    price_position: float | None | Unset = UNSET
    tick_value: float | None | Unset = UNSET
    tick_size: float | None | Unset = UNSET
    flags: int | None | Unset = UNSET
    time_msc: datetime.datetime | None | Unset = UNSET
    reason: DealReason | None | Unset = UNSET
    gateway: None | str | Unset = UNSET
    price_gateway: float | None | Unset = UNSET
    market_bid: float | None | Unset = UNSET
    market_ask: float | None | Unset = UNSET
    market_last: float | None | Unset = UNSET
    modification_flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deal = self.deal

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        login: int | None | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        dealer: int | None | Unset
        if isinstance(self.dealer, Unset):
            dealer = UNSET
        else:
            dealer = self.dealer

        party_id: int | None | Unset
        if isinstance(self.party_id, Unset):
            party_id = UNSET
        else:
            party_id = self.party_id

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, DealAction):
            action = self.action.value
        else:
            action = self.action

        entry: None | str | Unset
        if isinstance(self.entry, Unset):
            entry = UNSET
        elif isinstance(self.entry, EntryFlag):
            entry = self.entry.value
        else:
            entry = self.entry

        digits: int | None | Unset
        if isinstance(self.digits, Unset):
            digits = UNSET
        else:
            digits = self.digits

        digits_currency: int | None | Unset
        if isinstance(self.digits_currency, Unset):
            digits_currency = UNSET
        else:
            digits_currency = self.digits_currency

        contract_size: float | None | Unset
        if isinstance(self.contract_size, Unset):
            contract_size = UNSET
        else:
            contract_size = self.contract_size

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        price_sl: float | None | Unset
        if isinstance(self.price_sl, Unset):
            price_sl = UNSET
        else:
            price_sl = self.price_sl

        price_tp: float | None | Unset
        if isinstance(self.price_tp, Unset):
            price_tp = UNSET
        else:
            price_tp = self.price_tp

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

        volume_closed: int | None | Unset
        if isinstance(self.volume_closed, Unset):
            volume_closed = UNSET
        else:
            volume_closed = self.volume_closed

        volume_closed_ext: int | None | Unset
        if isinstance(self.volume_closed_ext, Unset):
            volume_closed_ext = UNSET
        else:
            volume_closed_ext = self.volume_closed_ext

        profit: float | None | Unset
        if isinstance(self.profit, Unset):
            profit = UNSET
        else:
            profit = self.profit

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        storage: float | None | Unset
        if isinstance(self.storage, Unset):
            storage = UNSET
        else:
            storage = self.storage

        commission: float | None | Unset
        if isinstance(self.commission, Unset):
            commission = UNSET
        else:
            commission = self.commission

        obsolete_value: float | None | Unset
        if isinstance(self.obsolete_value, Unset):
            obsolete_value = UNSET
        else:
            obsolete_value = self.obsolete_value

        fee: float | None | Unset
        if isinstance(self.fee, Unset):
            fee = UNSET
        else:
            fee = self.fee

        rate_profit: float | None | Unset
        if isinstance(self.rate_profit, Unset):
            rate_profit = UNSET
        else:
            rate_profit = self.rate_profit

        rate_margin: float | None | Unset
        if isinstance(self.rate_margin, Unset):
            rate_margin = UNSET
        else:
            rate_margin = self.rate_margin

        expert_id: int | None | Unset
        if isinstance(self.expert_id, Unset):
            expert_id = UNSET
        else:
            expert_id = self.expert_id

        position_id: int | None | Unset
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        profit_raw: float | None | Unset
        if isinstance(self.profit_raw, Unset):
            profit_raw = UNSET
        else:
            profit_raw = self.profit_raw

        price_position: float | None | Unset
        if isinstance(self.price_position, Unset):
            price_position = UNSET
        else:
            price_position = self.price_position

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

        flags: int | None | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        time_msc: None | str | Unset
        if isinstance(self.time_msc, Unset):
            time_msc = UNSET
        elif isinstance(self.time_msc, datetime.datetime):
            time_msc = self.time_msc.isoformat()
        else:
            time_msc = self.time_msc

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, DealReason):
            reason = self.reason.value
        else:
            reason = self.reason

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        price_gateway: float | None | Unset
        if isinstance(self.price_gateway, Unset):
            price_gateway = UNSET
        else:
            price_gateway = self.price_gateway

        market_bid: float | None | Unset
        if isinstance(self.market_bid, Unset):
            market_bid = UNSET
        else:
            market_bid = self.market_bid

        market_ask: float | None | Unset
        if isinstance(self.market_ask, Unset):
            market_ask = UNSET
        else:
            market_ask = self.market_ask

        market_last: float | None | Unset
        if isinstance(self.market_last, Unset):
            market_last = UNSET
        else:
            market_last = self.market_last

        modification_flags: None | str | Unset
        if isinstance(self.modification_flags, Unset):
            modification_flags = UNSET
        else:
            modification_flags = self.modification_flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "deal": deal,
        })
        if external_id is not UNSET:
            field_dict["externalID"] = external_id
        if login is not UNSET:
            field_dict["login"] = login
        if dealer is not UNSET:
            field_dict["dealer"] = dealer
        if party_id is not UNSET:
            field_dict["partyID"] = party_id
        if order is not UNSET:
            field_dict["order"] = order
        if action is not UNSET:
            field_dict["action"] = action
        if entry is not UNSET:
            field_dict["entry"] = entry
        if digits is not UNSET:
            field_dict["digits"] = digits
        if digits_currency is not UNSET:
            field_dict["digitsCurrency"] = digits_currency
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if time is not UNSET:
            field_dict["time"] = time
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if price is not UNSET:
            field_dict["price"] = price
        if price_sl is not UNSET:
            field_dict["priceSL"] = price_sl
        if price_tp is not UNSET:
            field_dict["priceTP"] = price_tp
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext
        if volume_closed is not UNSET:
            field_dict["volumeClosed"] = volume_closed
        if volume_closed_ext is not UNSET:
            field_dict["volumeClosedExt"] = volume_closed_ext
        if profit is not UNSET:
            field_dict["profit"] = profit
        if value is not UNSET:
            field_dict["value"] = value
        if storage is not UNSET:
            field_dict["storage"] = storage
        if commission is not UNSET:
            field_dict["commission"] = commission
        if obsolete_value is not UNSET:
            field_dict["obsoleteValue"] = obsolete_value
        if fee is not UNSET:
            field_dict["fee"] = fee
        if rate_profit is not UNSET:
            field_dict["rateProfit"] = rate_profit
        if rate_margin is not UNSET:
            field_dict["rateMargin"] = rate_margin
        if expert_id is not UNSET:
            field_dict["expertID"] = expert_id
        if position_id is not UNSET:
            field_dict["positionID"] = position_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if profit_raw is not UNSET:
            field_dict["profitRaw"] = profit_raw
        if price_position is not UNSET:
            field_dict["pricePosition"] = price_position
        if tick_value is not UNSET:
            field_dict["tickValue"] = tick_value
        if tick_size is not UNSET:
            field_dict["tickSize"] = tick_size
        if flags is not UNSET:
            field_dict["flags"] = flags
        if time_msc is not UNSET:
            field_dict["timeMsc"] = time_msc
        if reason is not UNSET:
            field_dict["reason"] = reason
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if price_gateway is not UNSET:
            field_dict["priceGateway"] = price_gateway
        if market_bid is not UNSET:
            field_dict["marketBid"] = market_bid
        if market_ask is not UNSET:
            field_dict["marketAsk"] = market_ask
        if market_last is not UNSET:
            field_dict["marketLast"] = market_last
        if modification_flags is not UNSET:
            field_dict["modificationFlags"] = modification_flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deal = d.pop("deal")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalID", UNSET))


        def _parse_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_dealer(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dealer = _parse_dealer(d.pop("dealer", UNSET))


        def _parse_party_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        party_id = _parse_party_id(d.pop("partyID", UNSET))


        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))


        def _parse_action(data: object) -> DealAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = DealAction(data)



                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DealAction | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_entry(data: object) -> EntryFlag | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entry_type_1 = EntryFlag(data)



                return entry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EntryFlag | None | Unset, data)

        entry = _parse_entry(d.pop("entry", UNSET))


        def _parse_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits = _parse_digits(d.pop("digits", UNSET))


        def _parse_digits_currency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits_currency = _parse_digits_currency(d.pop("digitsCurrency", UNSET))


        def _parse_contract_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        contract_size = _parse_contract_size(d.pop("contractSize", UNSET))


        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)



                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))


        def _parse_price_sl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_sl = _parse_price_sl(d.pop("priceSL", UNSET))


        def _parse_price_tp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_tp = _parse_price_tp(d.pop("priceTP", UNSET))


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


        def _parse_volume_closed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_closed = _parse_volume_closed(d.pop("volumeClosed", UNSET))


        def _parse_volume_closed_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_closed_ext = _parse_volume_closed_ext(d.pop("volumeClosedExt", UNSET))


        def _parse_profit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profit = _parse_profit(d.pop("profit", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        def _parse_storage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage = _parse_storage(d.pop("storage", UNSET))


        def _parse_commission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        commission = _parse_commission(d.pop("commission", UNSET))


        def _parse_obsolete_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        obsolete_value = _parse_obsolete_value(d.pop("obsoleteValue", UNSET))


        def _parse_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fee = _parse_fee(d.pop("fee", UNSET))


        def _parse_rate_profit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rate_profit = _parse_rate_profit(d.pop("rateProfit", UNSET))


        def _parse_rate_margin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rate_margin = _parse_rate_margin(d.pop("rateMargin", UNSET))


        def _parse_expert_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expert_id = _parse_expert_id(d.pop("expertID", UNSET))


        def _parse_position_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_id = _parse_position_id(d.pop("positionID", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_profit_raw(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profit_raw = _parse_profit_raw(d.pop("profitRaw", UNSET))


        def _parse_price_position(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_position = _parse_price_position(d.pop("pricePosition", UNSET))


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


        def _parse_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_time_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_msc = _parse_time_msc(d.pop("timeMsc", UNSET))


        def _parse_reason(data: object) -> DealReason | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = DealReason(data)



                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DealReason | None | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))


        def _parse_price_gateway(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_gateway = _parse_price_gateway(d.pop("priceGateway", UNSET))


        def _parse_market_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_bid = _parse_market_bid(d.pop("marketBid", UNSET))


        def _parse_market_ask(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_ask = _parse_market_ask(d.pop("marketAsk", UNSET))


        def _parse_market_last(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_last = _parse_market_last(d.pop("marketLast", UNSET))


        def _parse_modification_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modification_flags = _parse_modification_flags(d.pop("modificationFlags", UNSET))


        mt5_deal = cls(
            deal=deal,
            external_id=external_id,
            login=login,
            dealer=dealer,
            party_id=party_id,
            order=order,
            action=action,
            entry=entry,
            digits=digits,
            digits_currency=digits_currency,
            contract_size=contract_size,
            time=time,
            symbol=symbol,
            price=price,
            price_sl=price_sl,
            price_tp=price_tp,
            volume=volume,
            volume_ext=volume_ext,
            volume_closed=volume_closed,
            volume_closed_ext=volume_closed_ext,
            profit=profit,
            value=value,
            storage=storage,
            commission=commission,
            obsolete_value=obsolete_value,
            fee=fee,
            rate_profit=rate_profit,
            rate_margin=rate_margin,
            expert_id=expert_id,
            position_id=position_id,
            comment=comment,
            profit_raw=profit_raw,
            price_position=price_position,
            tick_value=tick_value,
            tick_size=tick_size,
            flags=flags,
            time_msc=time_msc,
            reason=reason,
            gateway=gateway,
            price_gateway=price_gateway,
            market_bid=market_bid,
            market_ask=market_ask,
            market_last=market_last,
            modification_flags=modification_flags,
        )

        return mt5_deal

