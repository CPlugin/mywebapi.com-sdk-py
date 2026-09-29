from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.activation_modes import ActivationModes
from ..models.position_actions import PositionActions
from ..models.position_reasons import PositionReasons
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Position")



@_attrs_define
class MT5Position:
    """ 
        Attributes:
            login (int | None | Unset): Gets the login of the client, to whom the trade position belongs
            symbol (None | str | Unset): position symbol
            action (None | PositionActions | Unset): PositionAction
            digits (int | None | Unset): price digits
            digits_currency (int | None | Unset): currency digits
            contract_size (float | None | Unset): symbol contract size
            position (int | None | Unset): position ticket
            external_id (None | str | Unset): The ticket of a position in an external trading system
            time_create (datetime.datetime | None | Unset): position create time
            time_update (datetime.datetime | None | Unset): position last update time
            time_create_msc (datetime.datetime | None | Unset): position create time in msc since 1970.01.01
                <br /><strong>If the value of this field is specified, the TimeCreate value will be filled in
                automatically.</strong>
            time_update_msc (datetime.datetime | None | Unset): position last update time in msc since 1970.01.01
                <br /><strong>If the value of this field is specified, the TimeUpdate value will be filled in
                automatically.</strong>
            price_open (float | None | Unset): position weighted average open price
            price_current (float | None | Unset): position current price
            price_sl (float | None | Unset): position SL price
            price_tp (float | None | Unset): position TP price
            volume (int | None | Unset): position volume
            volume_ext (int | None | Unset): position volume
            profit (float | None | Unset): position floating profit
            storage (float | None | Unset): position accumulated swaps
            rate_profit (float | None | Unset): profit conversion rate (from symbol profit currency to deposit currency)
            rate_margin (float | None | Unset): margin conversion rate (from symbol margin currency to deposit currency)
            expert_id (int | None | Unset): expert id (filled by expert advisor)
            expert_position_id (int | None | Unset): expert position id
            comment (None | str | Unset):
            dealer (int | None | Unset): The login of a dealer, who has processed the order that opened the position. 0
                means that the order was processed automatically by the server
            activation_mode (ActivationModes | None | Unset): order activation state, time and price
            activation_time (datetime.datetime | None | Unset):
            activation_price (float | None | Unset):
            activation_flags (None | str | Unset):
            modification_flags (None | str | Unset): modification flags
            reason (None | PositionReasons | Unset): position reason - PositionReason
     """

    login: int | None | Unset = UNSET
    symbol: None | str | Unset = UNSET
    action: None | PositionActions | Unset = UNSET
    digits: int | None | Unset = UNSET
    digits_currency: int | None | Unset = UNSET
    contract_size: float | None | Unset = UNSET
    position: int | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    time_create: datetime.datetime | None | Unset = UNSET
    time_update: datetime.datetime | None | Unset = UNSET
    time_create_msc: datetime.datetime | None | Unset = UNSET
    time_update_msc: datetime.datetime | None | Unset = UNSET
    price_open: float | None | Unset = UNSET
    price_current: float | None | Unset = UNSET
    price_sl: float | None | Unset = UNSET
    price_tp: float | None | Unset = UNSET
    volume: int | None | Unset = UNSET
    volume_ext: int | None | Unset = UNSET
    profit: float | None | Unset = UNSET
    storage: float | None | Unset = UNSET
    rate_profit: float | None | Unset = UNSET
    rate_margin: float | None | Unset = UNSET
    expert_id: int | None | Unset = UNSET
    expert_position_id: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    dealer: int | None | Unset = UNSET
    activation_mode: ActivationModes | None | Unset = UNSET
    activation_time: datetime.datetime | None | Unset = UNSET
    activation_price: float | None | Unset = UNSET
    activation_flags: None | str | Unset = UNSET
    modification_flags: None | str | Unset = UNSET
    reason: None | PositionReasons | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login: int | None | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, PositionActions):
            action = self.action.value
        else:
            action = self.action

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

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        time_create: None | str | Unset
        if isinstance(self.time_create, Unset):
            time_create = UNSET
        elif isinstance(self.time_create, datetime.datetime):
            time_create = self.time_create.isoformat()
        else:
            time_create = self.time_create

        time_update: None | str | Unset
        if isinstance(self.time_update, Unset):
            time_update = UNSET
        elif isinstance(self.time_update, datetime.datetime):
            time_update = self.time_update.isoformat()
        else:
            time_update = self.time_update

        time_create_msc: None | str | Unset
        if isinstance(self.time_create_msc, Unset):
            time_create_msc = UNSET
        elif isinstance(self.time_create_msc, datetime.datetime):
            time_create_msc = self.time_create_msc.isoformat()
        else:
            time_create_msc = self.time_create_msc

        time_update_msc: None | str | Unset
        if isinstance(self.time_update_msc, Unset):
            time_update_msc = UNSET
        elif isinstance(self.time_update_msc, datetime.datetime):
            time_update_msc = self.time_update_msc.isoformat()
        else:
            time_update_msc = self.time_update_msc

        price_open: float | None | Unset
        if isinstance(self.price_open, Unset):
            price_open = UNSET
        else:
            price_open = self.price_open

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

        profit: float | None | Unset
        if isinstance(self.profit, Unset):
            profit = UNSET
        else:
            profit = self.profit

        storage: float | None | Unset
        if isinstance(self.storage, Unset):
            storage = UNSET
        else:
            storage = self.storage

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

        expert_position_id: int | None | Unset
        if isinstance(self.expert_position_id, Unset):
            expert_position_id = UNSET
        else:
            expert_position_id = self.expert_position_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        dealer: int | None | Unset
        if isinstance(self.dealer, Unset):
            dealer = UNSET
        else:
            dealer = self.dealer

        activation_mode: None | str | Unset
        if isinstance(self.activation_mode, Unset):
            activation_mode = UNSET
        elif isinstance(self.activation_mode, ActivationModes):
            activation_mode = self.activation_mode.value
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
        else:
            activation_flags = self.activation_flags

        modification_flags: None | str | Unset
        if isinstance(self.modification_flags, Unset):
            modification_flags = UNSET
        else:
            modification_flags = self.modification_flags

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, PositionReasons):
            reason = self.reason.value
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if action is not UNSET:
            field_dict["action"] = action
        if digits is not UNSET:
            field_dict["digits"] = digits
        if digits_currency is not UNSET:
            field_dict["digitsCurrency"] = digits_currency
        if contract_size is not UNSET:
            field_dict["contractSize"] = contract_size
        if position is not UNSET:
            field_dict["position"] = position
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if time_create is not UNSET:
            field_dict["timeCreate"] = time_create
        if time_update is not UNSET:
            field_dict["timeUpdate"] = time_update
        if time_create_msc is not UNSET:
            field_dict["timeCreateMsc"] = time_create_msc
        if time_update_msc is not UNSET:
            field_dict["timeUpdateMsc"] = time_update_msc
        if price_open is not UNSET:
            field_dict["priceOpen"] = price_open
        if price_current is not UNSET:
            field_dict["priceCurrent"] = price_current
        if price_sl is not UNSET:
            field_dict["priceSL"] = price_sl
        if price_tp is not UNSET:
            field_dict["priceTP"] = price_tp
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext
        if profit is not UNSET:
            field_dict["profit"] = profit
        if storage is not UNSET:
            field_dict["storage"] = storage
        if rate_profit is not UNSET:
            field_dict["rateProfit"] = rate_profit
        if rate_margin is not UNSET:
            field_dict["rateMargin"] = rate_margin
        if expert_id is not UNSET:
            field_dict["expertId"] = expert_id
        if expert_position_id is not UNSET:
            field_dict["expertPositionId"] = expert_position_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if dealer is not UNSET:
            field_dict["dealer"] = dealer
        if activation_mode is not UNSET:
            field_dict["activationMode"] = activation_mode
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if activation_price is not UNSET:
            field_dict["activationPrice"] = activation_price
        if activation_flags is not UNSET:
            field_dict["activationFlags"] = activation_flags
        if modification_flags is not UNSET:
            field_dict["modificationFlags"] = modification_flags
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_action(data: object) -> None | PositionActions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = PositionActions(data)



                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PositionActions | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


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


        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))


        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))


        def _parse_time_create(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_create_type_0 = datetime.datetime.fromisoformat(data)



                return time_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_create = _parse_time_create(d.pop("timeCreate", UNSET))


        def _parse_time_update(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_update_type_0 = datetime.datetime.fromisoformat(data)



                return time_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_update = _parse_time_update(d.pop("timeUpdate", UNSET))


        def _parse_time_create_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_create_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_create_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_create_msc = _parse_time_create_msc(d.pop("timeCreateMsc", UNSET))


        def _parse_time_update_msc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_update_msc_type_0 = datetime.datetime.fromisoformat(data)



                return time_update_msc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_update_msc = _parse_time_update_msc(d.pop("timeUpdateMsc", UNSET))


        def _parse_price_open(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_open = _parse_price_open(d.pop("priceOpen", UNSET))


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


        def _parse_profit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profit = _parse_profit(d.pop("profit", UNSET))


        def _parse_storage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage = _parse_storage(d.pop("storage", UNSET))


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

        expert_id = _parse_expert_id(d.pop("expertId", UNSET))


        def _parse_expert_position_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expert_position_id = _parse_expert_position_id(d.pop("expertPositionId", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_dealer(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dealer = _parse_dealer(d.pop("dealer", UNSET))


        def _parse_activation_mode(data: object) -> ActivationModes | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_mode_type_1 = ActivationModes(data)



                return activation_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivationModes | None | Unset, data)

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


        def _parse_activation_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_flags = _parse_activation_flags(d.pop("activationFlags", UNSET))


        def _parse_modification_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modification_flags = _parse_modification_flags(d.pop("modificationFlags", UNSET))


        def _parse_reason(data: object) -> None | PositionReasons | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = PositionReasons(data)



                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PositionReasons | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        mt5_position = cls(
            login=login,
            symbol=symbol,
            action=action,
            digits=digits,
            digits_currency=digits_currency,
            contract_size=contract_size,
            position=position,
            external_id=external_id,
            time_create=time_create,
            time_update=time_update,
            time_create_msc=time_create_msc,
            time_update_msc=time_update_msc,
            price_open=price_open,
            price_current=price_current,
            price_sl=price_sl,
            price_tp=price_tp,
            volume=volume,
            volume_ext=volume_ext,
            profit=profit,
            storage=storage,
            rate_profit=rate_profit,
            rate_margin=rate_margin,
            expert_id=expert_id,
            expert_position_id=expert_position_id,
            comment=comment,
            dealer=dealer,
            activation_mode=activation_mode,
            activation_time=activation_time,
            activation_price=activation_price,
            activation_flags=activation_flags,
            modification_flags=modification_flags,
            reason=reason,
        )

        return mt5_position

