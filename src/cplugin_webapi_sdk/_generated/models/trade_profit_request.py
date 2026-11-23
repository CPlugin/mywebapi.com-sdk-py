from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_type import OrderType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TradeProfitRequest")



@_attrs_define
class TradeProfitRequest:
    """ Conditions of a profit calculation, v2 request DTO.

        Attributes:
            group (None | str | Unset): Group whose deposit currency and prices are used for the calculation.
            symbol (None | str | Unset): Symbol the calculation is performed for.
            type_ (None | OrderType | Unset): Direction of the hypothetical position; only buy and sell are meaningful here.
            volume (int | Unset): Position volume; one unit is 1/10000 lot in the standard variant and 1/100000000 in the
                extended one.
            price_open (float | Unset): Open price of the hypothetical position.
            price_close (float | Unset): Close price of the hypothetical position.
     """

    group: None | str | Unset = UNSET
    symbol: None | str | Unset = UNSET
    type_: None | OrderType | Unset = UNSET
    volume: int | Unset = UNSET
    price_open: float | Unset = UNSET
    price_close: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, OrderType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        volume = self.volume

        price_open = self.price_open

        price_close = self.price_close


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if type_ is not UNSET:
            field_dict["type"] = type_
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price_open is not UNSET:
            field_dict["priceOpen"] = price_open
        if price_close is not UNSET:
            field_dict["priceClose"] = price_close

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


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


        volume = d.pop("volume", UNSET)

        price_open = d.pop("priceOpen", UNSET)

        price_close = d.pop("priceClose", UNSET)

        trade_profit_request = cls(
            group=group,
            symbol=symbol,
            type_=type_,
            volume=volume,
            price_open=price_open,
            price_close=price_close,
        )

        return trade_profit_request

