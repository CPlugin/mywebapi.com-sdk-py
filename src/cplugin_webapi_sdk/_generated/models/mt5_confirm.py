from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Confirm")



@_attrs_define
class MT5Confirm:
    """ 
        Attributes:
            id (int | None | Unset): request id
            ret_code (MT5Result | None | Unset): confirmation retcode
            volume (int | None | Unset): confirmed volume
            price (float | None | Unset): confirmed price
            tick_bid (float | None | Unset): confirmed tick bid
            tick_ask (float | None | Unset): confirmed tick ask
            tick_last (float | None | Unset): confirmed tick last
            comment (None | str | Unset): confirmation comment
            flags (int | None | Unset): flags
            deal_id (None | str | Unset): linked deal id in external system
            order_id (None | str | Unset): linked order id in external system
            price_gateway (float | None | Unset): execution price on gateway
            position_external_id (None | str | Unset): linked  position ticket in external system
            external_ret_code (int | None | Unset): external trade system return code
            volume_ext (int | None | Unset):
     """

    id: int | None | Unset = UNSET
    ret_code: MT5Result | None | Unset = UNSET
    volume: int | None | Unset = UNSET
    price: float | None | Unset = UNSET
    tick_bid: float | None | Unset = UNSET
    tick_ask: float | None | Unset = UNSET
    tick_last: float | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    flags: int | None | Unset = UNSET
    deal_id: None | str | Unset = UNSET
    order_id: None | str | Unset = UNSET
    price_gateway: float | None | Unset = UNSET
    position_external_id: None | str | Unset = UNSET
    external_ret_code: int | None | Unset = UNSET
    volume_ext: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        ret_code: None | str | Unset
        if isinstance(self.ret_code, Unset):
            ret_code = UNSET
        elif isinstance(self.ret_code, MT5Result):
            ret_code = self.ret_code.value
        else:
            ret_code = self.ret_code

        volume: int | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        tick_bid: float | None | Unset
        if isinstance(self.tick_bid, Unset):
            tick_bid = UNSET
        else:
            tick_bid = self.tick_bid

        tick_ask: float | None | Unset
        if isinstance(self.tick_ask, Unset):
            tick_ask = UNSET
        else:
            tick_ask = self.tick_ask

        tick_last: float | None | Unset
        if isinstance(self.tick_last, Unset):
            tick_last = UNSET
        else:
            tick_last = self.tick_last

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        flags: int | None | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        deal_id: None | str | Unset
        if isinstance(self.deal_id, Unset):
            deal_id = UNSET
        else:
            deal_id = self.deal_id

        order_id: None | str | Unset
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        price_gateway: float | None | Unset
        if isinstance(self.price_gateway, Unset):
            price_gateway = UNSET
        else:
            price_gateway = self.price_gateway

        position_external_id: None | str | Unset
        if isinstance(self.position_external_id, Unset):
            position_external_id = UNSET
        else:
            position_external_id = self.position_external_id

        external_ret_code: int | None | Unset
        if isinstance(self.external_ret_code, Unset):
            external_ret_code = UNSET
        else:
            external_ret_code = self.external_ret_code

        volume_ext: int | None | Unset
        if isinstance(self.volume_ext, Unset):
            volume_ext = UNSET
        else:
            volume_ext = self.volume_ext


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if ret_code is not UNSET:
            field_dict["retCode"] = ret_code
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if tick_bid is not UNSET:
            field_dict["tickBid"] = tick_bid
        if tick_ask is not UNSET:
            field_dict["tickAsk"] = tick_ask
        if tick_last is not UNSET:
            field_dict["tickLast"] = tick_last
        if comment is not UNSET:
            field_dict["comment"] = comment
        if flags is not UNSET:
            field_dict["flags"] = flags
        if deal_id is not UNSET:
            field_dict["dealID"] = deal_id
        if order_id is not UNSET:
            field_dict["orderID"] = order_id
        if price_gateway is not UNSET:
            field_dict["priceGateway"] = price_gateway
        if position_external_id is not UNSET:
            field_dict["positionExternalID"] = position_external_id
        if external_ret_code is not UNSET:
            field_dict["externalRetCode"] = external_ret_code
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_ret_code(data: object) -> MT5Result | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ret_code_type_1 = MT5Result(data)



                return ret_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5Result | None | Unset, data)

        ret_code = _parse_ret_code(d.pop("retCode", UNSET))


        def _parse_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))


        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))


        def _parse_tick_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_bid = _parse_tick_bid(d.pop("tickBid", UNSET))


        def _parse_tick_ask(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_ask = _parse_tick_ask(d.pop("tickAsk", UNSET))


        def _parse_tick_last(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tick_last = _parse_tick_last(d.pop("tickLast", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_deal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deal_id = _parse_deal_id(d.pop("dealID", UNSET))


        def _parse_order_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_id = _parse_order_id(d.pop("orderID", UNSET))


        def _parse_price_gateway(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_gateway = _parse_price_gateway(d.pop("priceGateway", UNSET))


        def _parse_position_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position_external_id = _parse_position_external_id(d.pop("positionExternalID", UNSET))


        def _parse_external_ret_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        external_ret_code = _parse_external_ret_code(d.pop("externalRetCode", UNSET))


        def _parse_volume_ext(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume_ext = _parse_volume_ext(d.pop("volumeExt", UNSET))


        mt5_confirm = cls(
            id=id,
            ret_code=ret_code,
            volume=volume,
            price=price,
            tick_bid=tick_bid,
            tick_ask=tick_ask,
            tick_last=tick_last,
            comment=comment,
            flags=flags,
            deal_id=deal_id,
            order_id=order_id,
            price_gateway=price_gateway,
            position_external_id=position_external_id,
            external_ret_code=external_ret_code,
            volume_ext=volume_ext,
        )

        return mt5_confirm

