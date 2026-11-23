from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..models.order_filling import OrderFilling
from ..models.order_time import OrderTime
from ..models.order_type import OrderType
from ..models.trade_actions import TradeActions
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Request")



@_attrs_define
class MT5Request:
    """ 
        Attributes:
            login (int): client login
            symbol (str): symbol
            action (TradeActions):
            type_ (OrderType):
            volume (int): 1 lot = 10_000
            price_order (float): order price
            id (int | None | Unset): <strong>Read-only: the trade server does not let this value be changed.</strong>
                <br />
                <br />
                            request id
            group (None | str | Unset): <strong>Read-only: the trade server does not let this value be changed.</strong>
                <br />
                <br />
            digits (int | None | Unset): price digits
            time_expiration (datetime.datetime | None | Unset): order expiration
            type_fill (None | OrderFilling | Unset): IMTOrder::OrderFilling
            type_time (None | OrderTime | Unset): IMTOrder::OrderTime
            flags (None | str | Unset): additional flags TradeActionFlags
            order (int | None | Unset): order ticket
            order_external_id (None | str | Unset): order ticket in external system (exchange, ECN, etc)
            price_trigger (float | None | Unset): order trigger price
            price_sl (float | None | Unset): order SL price
            price_tp (float | None | Unset): order TP price
            price_deviation (int | None | Unset): price deviation details
            price_deviation_top (float | None | Unset):
            price_deviation_bottom (float | None | Unset):
            comment (None | str | Unset): comment
            result_ret_code (MT5Result | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result information
            result_dealer (int | None | Unset): request result deal
                request dealer
            result_deal (int | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result deal
            result_order (int | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result order
            result_volume (int | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result confirmed volume
            result_price (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result confirmed price
            result_dealer_bid (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result dealer prices
            result_dealer_ask (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
            result_dealer_last (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
            result_market_bid (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result market prices
            result_market_ask (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
            result_market_last (float | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
            result_comment (None | str | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result comment
            external_account (None | str | Unset): external system trade account (exchange, ECN, etc)
            id_client (int | None | Unset): <strong>Read-only: the trade server does not let this value be changed.</strong>
                <br />
                <br />
                            client side request id
            ip (None | str | Unset): source request ip
            source_login (int | None | Unset): source dealer login (for dealer transaction)
            position (int | None | Unset): position ticket
            position_by (int | None | Unset): position ticket for close-by
            position_external_id (None | str | Unset): position ticket in external system (exchange, ECN, etc)
            position_by_external_id (None | str | Unset): position ticket in external system (exchange, ECN, etc)
            volume_ext (int | None | Unset): volume with extended accuracy, 1 lot = 100_000_000
            result_volume_ext (int | None | Unset): <strong>Read-only: the trade server does not let this value be
                changed.</strong>
                <br />
                <br />
                            request result confirmed volume with extended accuracy
            volume_current (int | None | Unset): current order volume
            volume_current_ext (int | None | Unset): current order volume
     """

    login: int
    symbol: str
    action: TradeActions
    type_: OrderType
    volume: int
    price_order: float
    id: int | None | Unset = UNSET
    group: None | str | Unset = UNSET
    digits: int | None | Unset = UNSET
    time_expiration: datetime.datetime | None | Unset = UNSET
    type_fill: None | OrderFilling | Unset = UNSET
    type_time: None | OrderTime | Unset = UNSET
    flags: None | str | Unset = UNSET
    order: int | None | Unset = UNSET
    order_external_id: None | str | Unset = UNSET
    price_trigger: float | None | Unset = UNSET
    price_sl: float | None | Unset = UNSET
    price_tp: float | None | Unset = UNSET
    price_deviation: int | None | Unset = UNSET
    price_deviation_top: float | None | Unset = UNSET
    price_deviation_bottom: float | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    result_ret_code: MT5Result | None | Unset = UNSET
    result_dealer: int | None | Unset = UNSET
    result_deal: int | None | Unset = UNSET
    result_order: int | None | Unset = UNSET
    result_volume: int | None | Unset = UNSET
    result_price: float | None | Unset = UNSET
    result_dealer_bid: float | None | Unset = UNSET
    result_dealer_ask: float | None | Unset = UNSET
    result_dealer_last: float | None | Unset = UNSET
    result_market_bid: float | None | Unset = UNSET
    result_market_ask: float | None | Unset = UNSET
    result_market_last: float | None | Unset = UNSET
    result_comment: None | str | Unset = UNSET
    external_account: None | str | Unset = UNSET
    id_client: int | None | Unset = UNSET
    ip: None | str | Unset = UNSET
    source_login: int | None | Unset = UNSET
    position: int | None | Unset = UNSET
    position_by: int | None | Unset = UNSET
    position_external_id: None | str | Unset = UNSET
    position_by_external_id: None | str | Unset = UNSET
    volume_ext: int | None | Unset = UNSET
    result_volume_ext: int | None | Unset = UNSET
    volume_current: int | None | Unset = UNSET
    volume_current_ext: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        symbol = self.symbol

        action = self.action.value

        type_ = self.type_.value

        volume = self.volume

        price_order = self.price_order

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        digits: int | None | Unset
        if isinstance(self.digits, Unset):
            digits = UNSET
        else:
            digits = self.digits

        time_expiration: None | str | Unset
        if isinstance(self.time_expiration, Unset):
            time_expiration = UNSET
        elif isinstance(self.time_expiration, datetime.datetime):
            time_expiration = self.time_expiration.isoformat()
        else:
            time_expiration = self.time_expiration

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

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        order_external_id: None | str | Unset
        if isinstance(self.order_external_id, Unset):
            order_external_id = UNSET
        else:
            order_external_id = self.order_external_id

        price_trigger: float | None | Unset
        if isinstance(self.price_trigger, Unset):
            price_trigger = UNSET
        else:
            price_trigger = self.price_trigger

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

        price_deviation: int | None | Unset
        if isinstance(self.price_deviation, Unset):
            price_deviation = UNSET
        else:
            price_deviation = self.price_deviation

        price_deviation_top: float | None | Unset
        if isinstance(self.price_deviation_top, Unset):
            price_deviation_top = UNSET
        else:
            price_deviation_top = self.price_deviation_top

        price_deviation_bottom: float | None | Unset
        if isinstance(self.price_deviation_bottom, Unset):
            price_deviation_bottom = UNSET
        else:
            price_deviation_bottom = self.price_deviation_bottom

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        result_ret_code: None | str | Unset
        if isinstance(self.result_ret_code, Unset):
            result_ret_code = UNSET
        elif isinstance(self.result_ret_code, MT5Result):
            result_ret_code = self.result_ret_code.value
        else:
            result_ret_code = self.result_ret_code

        result_dealer: int | None | Unset
        if isinstance(self.result_dealer, Unset):
            result_dealer = UNSET
        else:
            result_dealer = self.result_dealer

        result_deal: int | None | Unset
        if isinstance(self.result_deal, Unset):
            result_deal = UNSET
        else:
            result_deal = self.result_deal

        result_order: int | None | Unset
        if isinstance(self.result_order, Unset):
            result_order = UNSET
        else:
            result_order = self.result_order

        result_volume: int | None | Unset
        if isinstance(self.result_volume, Unset):
            result_volume = UNSET
        else:
            result_volume = self.result_volume

        result_price: float | None | Unset
        if isinstance(self.result_price, Unset):
            result_price = UNSET
        else:
            result_price = self.result_price

        result_dealer_bid: float | None | Unset
        if isinstance(self.result_dealer_bid, Unset):
            result_dealer_bid = UNSET
        else:
            result_dealer_bid = self.result_dealer_bid

        result_dealer_ask: float | None | Unset
        if isinstance(self.result_dealer_ask, Unset):
            result_dealer_ask = UNSET
        else:
            result_dealer_ask = self.result_dealer_ask

        result_dealer_last: float | None | Unset
        if isinstance(self.result_dealer_last, Unset):
            result_dealer_last = UNSET
        else:
            result_dealer_last = self.result_dealer_last

        result_market_bid: float | None | Unset
        if isinstance(self.result_market_bid, Unset):
            result_market_bid = UNSET
        else:
            result_market_bid = self.result_market_bid

        result_market_ask: float | None | Unset
        if isinstance(self.result_market_ask, Unset):
            result_market_ask = UNSET
        else:
            result_market_ask = self.result_market_ask

        result_market_last: float | None | Unset
        if isinstance(self.result_market_last, Unset):
            result_market_last = UNSET
        else:
            result_market_last = self.result_market_last

        result_comment: None | str | Unset
        if isinstance(self.result_comment, Unset):
            result_comment = UNSET
        else:
            result_comment = self.result_comment

        external_account: None | str | Unset
        if isinstance(self.external_account, Unset):
            external_account = UNSET
        else:
            external_account = self.external_account

        id_client: int | None | Unset
        if isinstance(self.id_client, Unset):
            id_client = UNSET
        else:
            id_client = self.id_client

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        source_login: int | None | Unset
        if isinstance(self.source_login, Unset):
            source_login = UNSET
        else:
            source_login = self.source_login

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        position_by: int | None | Unset
        if isinstance(self.position_by, Unset):
            position_by = UNSET
        else:
            position_by = self.position_by

        position_external_id: None | str | Unset
        if isinstance(self.position_external_id, Unset):
            position_external_id = UNSET
        else:
            position_external_id = self.position_external_id

        position_by_external_id: None | str | Unset
        if isinstance(self.position_by_external_id, Unset):
            position_by_external_id = UNSET
        else:
            position_by_external_id = self.position_by_external_id

        volume_ext: int | None | Unset
        if isinstance(self.volume_ext, Unset):
            volume_ext = UNSET
        else:
            volume_ext = self.volume_ext

        result_volume_ext: int | None | Unset
        if isinstance(self.result_volume_ext, Unset):
            result_volume_ext = UNSET
        else:
            result_volume_ext = self.result_volume_ext

        volume_current: int | None | Unset
        if isinstance(self.volume_current, Unset):
            volume_current = UNSET
        else:
            volume_current = self.volume_current

        volume_current_ext: int | None | Unset
        if isinstance(self.volume_current_ext, Unset):
            volume_current_ext = UNSET
        else:
            volume_current_ext = self.volume_current_ext


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "login": login,
            "symbol": symbol,
            "action": action,
            "type": type_,
            "volume": volume,
            "priceOrder": price_order,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if group is not UNSET:
            field_dict["group"] = group
        if digits is not UNSET:
            field_dict["digits"] = digits
        if time_expiration is not UNSET:
            field_dict["timeExpiration"] = time_expiration
        if type_fill is not UNSET:
            field_dict["typeFill"] = type_fill
        if type_time is not UNSET:
            field_dict["typeTime"] = type_time
        if flags is not UNSET:
            field_dict["flags"] = flags
        if order is not UNSET:
            field_dict["order"] = order
        if order_external_id is not UNSET:
            field_dict["orderExternalID"] = order_external_id
        if price_trigger is not UNSET:
            field_dict["priceTrigger"] = price_trigger
        if price_sl is not UNSET:
            field_dict["priceSL"] = price_sl
        if price_tp is not UNSET:
            field_dict["priceTP"] = price_tp
        if price_deviation is not UNSET:
            field_dict["priceDeviation"] = price_deviation
        if price_deviation_top is not UNSET:
            field_dict["priceDeviationTop"] = price_deviation_top
        if price_deviation_bottom is not UNSET:
            field_dict["priceDeviationBottom"] = price_deviation_bottom
        if comment is not UNSET:
            field_dict["comment"] = comment
        if result_ret_code is not UNSET:
            field_dict["resultRetCode"] = result_ret_code
        if result_dealer is not UNSET:
            field_dict["resultDealer"] = result_dealer
        if result_deal is not UNSET:
            field_dict["resultDeal"] = result_deal
        if result_order is not UNSET:
            field_dict["resultOrder"] = result_order
        if result_volume is not UNSET:
            field_dict["resultVolume"] = result_volume
        if result_price is not UNSET:
            field_dict["resultPrice"] = result_price
        if result_dealer_bid is not UNSET:
            field_dict["resultDealerBid"] = result_dealer_bid
        if result_dealer_ask is not UNSET:
            field_dict["resultDealerAsk"] = result_dealer_ask
        if result_dealer_last is not UNSET:
            field_dict["resultDealerLast"] = result_dealer_last
        if result_market_bid is not UNSET:
            field_dict["resultMarketBid"] = result_market_bid
        if result_market_ask is not UNSET:
            field_dict["resultMarketAsk"] = result_market_ask
        if result_market_last is not UNSET:
            field_dict["resultMarketLast"] = result_market_last
        if result_comment is not UNSET:
            field_dict["resultComment"] = result_comment
        if external_account is not UNSET:
            field_dict["externalAccount"] = external_account
        if id_client is not UNSET:
            field_dict["idClient"] = id_client
        if ip is not UNSET:
            field_dict["ip"] = ip
        if source_login is not UNSET:
            field_dict["sourceLogin"] = source_login
        if position is not UNSET:
            field_dict["position"] = position
        if position_by is not UNSET:
            field_dict["positionBy"] = position_by
        if position_external_id is not UNSET:
            field_dict["positionExternalID"] = position_external_id
        if position_by_external_id is not UNSET:
            field_dict["positionByExternalID"] = position_by_external_id
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext
        if result_volume_ext is not UNSET:
            field_dict["resultVolumeExt"] = result_volume_ext
        if volume_current is not UNSET:
            field_dict["volumeCurrent"] = volume_current
        if volume_current_ext is not UNSET:
            field_dict["volumeCurrentExt"] = volume_current_ext

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login")

        symbol = d.pop("symbol")

        action = TradeActions(d.pop("action"))




        type_ = OrderType(d.pop("type"))




        volume = d.pop("volume")

        price_order = d.pop("priceOrder")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits = _parse_digits(d.pop("digits", UNSET))


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


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))


        def _parse_order_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_external_id = _parse_order_external_id(d.pop("orderExternalID", UNSET))


        def _parse_price_trigger(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_trigger = _parse_price_trigger(d.pop("priceTrigger", UNSET))


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


        def _parse_price_deviation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_deviation = _parse_price_deviation(d.pop("priceDeviation", UNSET))


        def _parse_price_deviation_top(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_deviation_top = _parse_price_deviation_top(d.pop("priceDeviationTop", UNSET))


        def _parse_price_deviation_bottom(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_deviation_bottom = _parse_price_deviation_bottom(d.pop("priceDeviationBottom", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_result_ret_code(data: object) -> MT5Result | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_ret_code_type_1 = MT5Result(data)



                return result_ret_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5Result | None | Unset, data)

        result_ret_code = _parse_result_ret_code(d.pop("resultRetCode", UNSET))


        def _parse_result_dealer(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_dealer = _parse_result_dealer(d.pop("resultDealer", UNSET))


        def _parse_result_deal(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_deal = _parse_result_deal(d.pop("resultDeal", UNSET))


        def _parse_result_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_order = _parse_result_order(d.pop("resultOrder", UNSET))


        def _parse_result_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_volume = _parse_result_volume(d.pop("resultVolume", UNSET))


        def _parse_result_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_price = _parse_result_price(d.pop("resultPrice", UNSET))


        def _parse_result_dealer_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_dealer_bid = _parse_result_dealer_bid(d.pop("resultDealerBid", UNSET))


        def _parse_result_dealer_ask(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_dealer_ask = _parse_result_dealer_ask(d.pop("resultDealerAsk", UNSET))


        def _parse_result_dealer_last(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_dealer_last = _parse_result_dealer_last(d.pop("resultDealerLast", UNSET))


        def _parse_result_market_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_market_bid = _parse_result_market_bid(d.pop("resultMarketBid", UNSET))


        def _parse_result_market_ask(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_market_ask = _parse_result_market_ask(d.pop("resultMarketAsk", UNSET))


        def _parse_result_market_last(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        result_market_last = _parse_result_market_last(d.pop("resultMarketLast", UNSET))


        def _parse_result_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_comment = _parse_result_comment(d.pop("resultComment", UNSET))


        def _parse_external_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account = _parse_external_account(d.pop("externalAccount", UNSET))


        def _parse_id_client(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id_client = _parse_id_client(d.pop("idClient", UNSET))


        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))


        def _parse_source_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_login = _parse_source_login(d.pop("sourceLogin", UNSET))


        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))


        def _parse_position_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_by = _parse_position_by(d.pop("positionBy", UNSET))


        def _parse_position_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position_external_id = _parse_position_external_id(d.pop("positionExternalID", UNSET))


        def _parse_position_by_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position_by_external_id = _parse_position_by_external_id(d.pop("positionByExternalID", UNSET))


        def _parse_volume_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_ext = _parse_volume_ext(d.pop("volumeExt", UNSET))


        def _parse_result_volume_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_volume_ext = _parse_result_volume_ext(d.pop("resultVolumeExt", UNSET))


        def _parse_volume_current(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_current = _parse_volume_current(d.pop("volumeCurrent", UNSET))


        def _parse_volume_current_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_current_ext = _parse_volume_current_ext(d.pop("volumeCurrentExt", UNSET))


        mt5_request = cls(
            login=login,
            symbol=symbol,
            action=action,
            type_=type_,
            volume=volume,
            price_order=price_order,
            id=id,
            group=group,
            digits=digits,
            time_expiration=time_expiration,
            type_fill=type_fill,
            type_time=type_time,
            flags=flags,
            order=order,
            order_external_id=order_external_id,
            price_trigger=price_trigger,
            price_sl=price_sl,
            price_tp=price_tp,
            price_deviation=price_deviation,
            price_deviation_top=price_deviation_top,
            price_deviation_bottom=price_deviation_bottom,
            comment=comment,
            result_ret_code=result_ret_code,
            result_dealer=result_dealer,
            result_deal=result_deal,
            result_order=result_order,
            result_volume=result_volume,
            result_price=result_price,
            result_dealer_bid=result_dealer_bid,
            result_dealer_ask=result_dealer_ask,
            result_dealer_last=result_dealer_last,
            result_market_bid=result_market_bid,
            result_market_ask=result_market_ask,
            result_market_last=result_market_last,
            result_comment=result_comment,
            external_account=external_account,
            id_client=id_client,
            ip=ip,
            source_login=source_login,
            position=position,
            position_by=position_by,
            position_external_id=position_external_id,
            position_by_external_id=position_by_external_id,
            volume_ext=volume_ext,
            result_volume_ext=result_volume_ext,
            volume_current=volume_current,
            volume_current_ext=volume_current_ext,
        )

        return mt5_request

