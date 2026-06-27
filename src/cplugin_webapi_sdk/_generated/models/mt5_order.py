from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_filling import OrderFilling
from ..models.order_reason import OrderReason
from ..models.order_state import OrderState
from ..models.order_time import OrderTime
from ..models.order_type import OrderType
from ..models.trade_activation_flags import TradeActivationFlags
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Order")



@_attrs_define
class MT5Order:
    """ 
        Attributes:
            order (int | None | Unset): order ticket
            external_id (None | str | Unset): order ticket in external system (exchange, ECN, etc)
            login (int | None | Unset): client login
            dealer (int | None | Unset): processed dealer login (0-means auto)
            party_id (int | None | Unset): counterparty identification
            symbol (None | str | Unset): order symbol
            digits (int | None | Unset): price digits
            digits_currency (int | None | Unset): currency digits
            contract_size (float | None | Unset): contract size
            state (None | OrderState | Unset): OrderState
            reason (None | OrderReason | Unset): OrderReason
            time_setup (datetime.datetime | None | Unset): order setup time
            time_expiration (datetime.datetime | None | Unset): order expiration
            time_done (datetime.datetime | None | Unset): order filling/cancel time
            type_ (None | OrderType | Unset): OrderType
            type_fill (None | OrderFilling | Unset): OrderFilling
            type_time (None | OrderTime | Unset): OrderTime
            price_order (float | None | Unset): order price
            price_trigger (float | None | Unset): order trigger price (stop-limit price)
            price_current (float | None | Unset): order current price
            price_sl (float | None | Unset): order SL
            price_tp (float | None | Unset): order TP
            volume_initial (int | None | Unset): order initial volume
            volume_current (int | None | Unset): order current volume
            expert_id (int | None | Unset): expert id (filled by expert advisor)
            position_id (int | None | Unset): position id
            comment (None | str | Unset): order comment
            activation_mode (int | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
                            order activation state, time and price
            activation_time (datetime.datetime | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to
                read this value.</strong>
                <br />
                <br />
            activation_price (float | None | Unset): <strong>Has No Setter In ManagerAPI, so all you can is to read this
                value.</strong>
                <br />
                <br />
                            Gets the price, at which the order was activated
            activation_flags (None | TradeActivationFlags | Unset): <strong>Has No Setter In ManagerAPI, so all you can is
                to read this value.</strong>
                <br />
                <br />
            time_setup_msc (datetime.datetime | None | Unset): Gets and sets the order placing time in milliseconds, since
                1970.01.01
                <br /><strong>If the value of this field is specified, the TimeSetup value will be filled in
                automatically.</strong>
            time_done_msc (datetime.datetime | None | Unset): Gets and sets the order execution time in milliseconds, since
                1970.01.01
                <br /><strong>If the value of this field is specified, the TimeDone value will be filled in
                automatically.</strong>
            rate_margin (float | None | Unset): margin conversion rate (from symbol margin currency to deposit currency)
            position_by_id (int | None | Unset): position by id
            modification_flags (int | None | Unset): modification flags
            volume_initial_ext (int | None | Unset): order initial volume with extended accuracy
            volume_current_ext (int | None | Unset): order current volume with extended accuracy
     """

    order: int | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    login: int | None | Unset = UNSET
    dealer: int | None | Unset = UNSET
    party_id: int | None | Unset = UNSET
    symbol: None | str | Unset = UNSET
    digits: int | None | Unset = UNSET
    digits_currency: int | None | Unset = UNSET
    contract_size: float | None | Unset = UNSET
    state: None | OrderState | Unset = UNSET
    reason: None | OrderReason | Unset = UNSET
    time_setup: datetime.datetime | None | Unset = UNSET
    time_expiration: datetime.datetime | None | Unset = UNSET
    time_done: datetime.datetime | None | Unset = UNSET
    type_: None | OrderType | Unset = UNSET
    type_fill: None | OrderFilling | Unset = UNSET
    type_time: None | OrderTime | Unset = UNSET
    price_order: float | None | Unset = UNSET
    price_trigger: float | None | Unset = UNSET
    price_current: float | None | Unset = UNSET
    price_sl: float | None | Unset = UNSET
    price_tp: float | None | Unset = UNSET
    volume_initial: int | None | Unset = UNSET
    volume_current: int | None | Unset = UNSET
    expert_id: int | None | Unset = UNSET
    position_id: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    activation_mode: int | None | Unset = UNSET
    activation_time: datetime.datetime | None | Unset = UNSET
    activation_price: float | None | Unset = UNSET
    activation_flags: None | TradeActivationFlags | Unset = UNSET
    time_setup_msc: datetime.datetime | None | Unset = UNSET
    time_done_msc: datetime.datetime | None | Unset = UNSET
    rate_margin: float | None | Unset = UNSET
    position_by_id: int | None | Unset = UNSET
    modification_flags: int | None | Unset = UNSET
    volume_initial_ext: int | None | Unset = UNSET
    volume_current_ext: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

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

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

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

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, OrderState):
            state = self.state.value
        else:
            state = self.state

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, OrderReason):
            reason = self.reason.value
        else:
            reason = self.reason

        time_setup: None | str | Unset
        if isinstance(self.time_setup, Unset):
            time_setup = UNSET
        elif isinstance(self.time_setup, datetime.datetime):
            time_setup = self.time_setup.isoformat()
        else:
            time_setup = self.time_setup

        time_expiration: None | str | Unset
        if isinstance(self.time_expiration, Unset):
            time_expiration = UNSET
        elif isinstance(self.time_expiration, datetime.datetime):
            time_expiration = self.time_expiration.isoformat()
        else:
            time_expiration = self.time_expiration

        time_done: None | str | Unset
        if isinstance(self.time_done, Unset):
            time_done = UNSET
        elif isinstance(self.time_done, datetime.datetime):
            time_done = self.time_done.isoformat()
        else:
            time_done = self.time_done

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, OrderType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        type_fill: None | str | Unset
        if isinstance(self.type_fill, Unset):
            type_fill = UNSET
        elif isinstance(self.type_fill, OrderFilling):
            type_fill = self.type_fill.value
        else:
            type_fill = self.type_fill

        type_time: None | str | Unset
        if isinstance(self.type_time, Unset):
            type_time = UNSET
        elif isinstance(self.type_time, OrderTime):
            type_time = self.type_time.value
        else:
            type_time = self.type_time

        price_order: float | None | Unset
        if isinstance(self.price_order, Unset):
            price_order = UNSET
        else:
            price_order = self.price_order

        price_trigger: float | None | Unset
        if isinstance(self.price_trigger, Unset):
            price_trigger = UNSET
        else:
            price_trigger = self.price_trigger

        price_current: float | None | Unset
        if isinstance(self.price_current, Unset):
            price_current = UNSET
        else:
            price_current = self.price_current

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

        volume_initial: int | None | Unset
        if isinstance(self.volume_initial, Unset):
            volume_initial = UNSET
        else:
            volume_initial = self.volume_initial

        volume_current: int | None | Unset
        if isinstance(self.volume_current, Unset):
            volume_current = UNSET
        else:
            volume_current = self.volume_current

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

        activation_mode: int | None | Unset
        if isinstance(self.activation_mode, Unset):
            activation_mode = UNSET
        else:
            activation_mode = self.activation_mode

        activation_time: None | str | Unset
        if isinstance(self.activation_time, Unset):
            activation_time = UNSET
        elif isinstance(self.activation_time, datetime.datetime):
            activation_time = self.activation_time.isoformat()
        else:
            activation_time = self.activation_time

        activation_price: float | None | Unset
        if isinstance(self.activation_price, Unset):
            activation_price = UNSET
        else:
            activation_price = self.activation_price

        activation_flags: None | str | Unset
        if isinstance(self.activation_flags, Unset):
            activation_flags = UNSET
        elif isinstance(self.activation_flags, TradeActivationFlags):
            activation_flags = self.activation_flags.value
        else:
            activation_flags = self.activation_flags

        time_setup_msc: None | str | Unset
        if isinstance(self.time_setup_msc, Unset):
            time_setup_msc = UNSET
        elif isinstance(self.time_setup_msc, datetime.datetime):
            time_setup_msc = self.time_setup_msc.isoformat()
        else:
            time_setup_msc = self.time_setup_msc

        time_done_msc: None | str | Unset
        if isinstance(self.time_done_msc, Unset):
            time_done_msc = UNSET
        elif isinstance(self.time_done_msc, datetime.datetime):
            time_done_msc = self.time_done_msc.isoformat()
        else:
            time_done_msc = self.time_done_msc

        rate_margin: float | None | Unset
        if isinstance(self.rate_margin, Unset):
            rate_margin = UNSET
        else:
            rate_margin = self.rate_margin

        position_by_id: int | None | Unset
        if isinstance(self.position_by_id, Unset):
            position_by_id = UNSET
        else:
            position_by_id = self.position_by_id

        modification_flags: int | None | Unset
        if isinstance(self.modification_flags, Unset):
            modification_flags = UNSET
        else:
            modification_flags = self.modification_flags

        volume_initial_ext: int | None | Unset
        if isinstance(self.volume_initial_ext, Unset):
            volume_initial_ext = UNSET
        else:
            volume_initial_ext = self.volume_initial_ext

        volume_current_ext: int | None | Unset
        if isinstance(self.volume_current_ext, Unset):
            volume_current_ext = UNSET
        else:
            volume_current_ext = self.volume_current_ext


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order is not UNSET:
            field_dict["order"] = order
        if external_id is not UNSET:
            field_dict["externalID"] = external_id
        if login is not UNSET:
            field_dict["login"] = login
        if dealer is not UNSET:
            field_dict["dealer"] = dealer
        if party_id is not UNSET:
            field_dict["partyID"] = party_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if digits is not UNSET:
            field_dict["digits"] = digits
        if digits_currency is not UNSET:
            field_dict["digitsCurrency"] = digits_currency
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if state is not UNSET:
            field_dict["state"] = state
        if reason is not UNSET:
            field_dict["reason"] = reason
        if time_setup is not UNSET:
            field_dict["timeSetup"] = time_setup
        if time_expiration is not UNSET:
            field_dict["timeExpiration"] = time_expiration
        if time_done is not UNSET:
            field_dict["timeDone"] = time_done
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_fill is not UNSET:
            field_dict["typeFill"] = type_fill
        if type_time is not UNSET:
            field_dict["typeTime"] = type_time
        if price_order is not UNSET:
            field_dict["priceOrder"] = price_order
        if price_trigger is not UNSET:
            field_dict["priceTrigger"] = price_trigger
        if price_current is not UNSET:
            field_dict["priceCurrent"] = price_current
        if price_sl is not UNSET:
            field_dict["priceSL"] = price_sl
        if price_tp is not UNSET:
            field_dict["priceTP"] = price_tp
        if volume_initial is not UNSET:
            field_dict["volumeInitial"] = volume_initial
        if volume_current is not UNSET:
            field_dict["volumeCurrent"] = volume_current
        if expert_id is not UNSET:
            field_dict["expertID"] = expert_id
        if position_id is not UNSET:
            field_dict["positionID"] = position_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if activation_mode is not UNSET:
            field_dict["activationMode"] = activation_mode
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if activation_price is not UNSET:
            field_dict["activationPrice"] = activation_price
        if activation_flags is not UNSET:
            field_dict["activationFlags"] = activation_flags
        if time_setup_msc is not UNSET:
            field_dict["timeSetupMsc"] = time_setup_msc
        if time_done_msc is not UNSET:
            field_dict["timeDoneMsc"] = time_done_msc
        if rate_margin is not UNSET:
            field_dict["rateMargin"] = rate_margin
        if position_by_id is not UNSET:
            field_dict["positionByID"] = position_by_id
        if modification_flags is not UNSET:
            field_dict["modificationFlags"] = modification_flags
        if volume_initial_ext is not UNSET:
            field_dict["volumeInitialExt"] = volume_initial_ext
        if volume_current_ext is not UNSET:
            field_dict["volumeCurrentExt"] = volume_current_ext

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))


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


        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


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


        def _parse_state(data: object) -> None | OrderState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_1 = OrderState(data)



                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderState | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_reason(data: object) -> None | OrderReason | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = OrderReason(data)



                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderReason | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_time_setup(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_setup_type_0 = datetime.datetime.fromisoformat(data)



                return time_setup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_setup = _parse_time_setup(d.pop("timeSetup", UNSET))


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


        def _parse_time_done(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_done_type_0 = datetime.datetime.fromisoformat(data)



                return time_done_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_done = _parse_time_done(d.pop("timeDone", UNSET))


        def _parse_type_(data: object) -> None | OrderType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = OrderType(data)



                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderType | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_type_fill(data: object) -> None | OrderFilling | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_fill_type_1 = OrderFilling(data)



                return type_fill_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderFilling | Unset, data)

        type_fill = _parse_type_fill(d.pop("typeFill", UNSET))


        def _parse_type_time(data: object) -> None | OrderTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_time_type_1 = OrderTime(data)



                return type_time_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderTime | Unset, data)

        type_time = _parse_type_time(d.pop("typeTime", UNSET))


        def _parse_price_order(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_order = _parse_price_order(d.pop("priceOrder", UNSET))


        def _parse_price_trigger(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_trigger = _parse_price_trigger(d.pop("priceTrigger", UNSET))


        def _parse_price_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_current = _parse_price_current(d.pop("priceCurrent", UNSET))


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


        def _parse_volume_initial(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_initial = _parse_volume_initial(d.pop("volumeInitial", UNSET))


        def _parse_volume_current(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_current = _parse_volume_current(d.pop("volumeCurrent", UNSET))


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


        def _parse_activation_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        activation_mode = _parse_activation_mode(d.pop("activationMode", UNSET))


        def _parse_activation_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_time_type_0 = datetime.datetime.fromisoformat(data)



                return activation_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        activation_time = _parse_activation_time(d.pop("activationTime", UNSET))


        def _parse_activation_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        activation_price = _parse_activation_price(d.pop("activationPrice", UNSET))


        def _parse_activation_flags(data: object) -> None | TradeActivationFlags | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_flags_type_1 = TradeActivationFlags(data)



                return activation_flags_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradeActivationFlags | Unset, data)

        activation_flags = _parse_activation_flags(d.pop("activationFlags", UNSET))


        def _parse_time_setup_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_setup_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_setup_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_setup_msc = _parse_time_setup_msc(d.pop("timeSetupMsc", UNSET))


        def _parse_time_done_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_done_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_done_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_done_msc = _parse_time_done_msc(d.pop("timeDoneMsc", UNSET))


        def _parse_rate_margin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rate_margin = _parse_rate_margin(d.pop("rateMargin", UNSET))


        def _parse_position_by_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_by_id = _parse_position_by_id(d.pop("positionByID", UNSET))


        def _parse_modification_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        modification_flags = _parse_modification_flags(d.pop("modificationFlags", UNSET))


        def _parse_volume_initial_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_initial_ext = _parse_volume_initial_ext(d.pop("volumeInitialExt", UNSET))


        def _parse_volume_current_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_current_ext = _parse_volume_current_ext(d.pop("volumeCurrentExt", UNSET))


        mt5_order = cls(
            order=order,
            external_id=external_id,
            login=login,
            dealer=dealer,
            party_id=party_id,
            symbol=symbol,
            digits=digits,
            digits_currency=digits_currency,
            contract_size=contract_size,
            state=state,
            reason=reason,
            time_setup=time_setup,
            time_expiration=time_expiration,
            time_done=time_done,
            type_=type_,
            type_fill=type_fill,
            type_time=type_time,
            price_order=price_order,
            price_trigger=price_trigger,
            price_current=price_current,
            price_sl=price_sl,
            price_tp=price_tp,
            volume_initial=volume_initial,
            volume_current=volume_current,
            expert_id=expert_id,
            position_id=position_id,
            comment=comment,
            activation_mode=activation_mode,
            activation_time=activation_time,
            activation_price=activation_price,
            activation_flags=activation_flags,
            time_setup_msc=time_setup_msc,
            time_done_msc=time_done_msc,
            rate_margin=rate_margin,
            position_by_id=position_by_id,
            modification_flags=modification_flags,
            volume_initial_ext=volume_initial_ext,
            volume_current_ext=volume_current_ext,
        )

        return mt5_order

