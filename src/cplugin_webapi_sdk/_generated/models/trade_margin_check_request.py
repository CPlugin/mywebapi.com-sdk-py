from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_type import OrderType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TradeMarginCheckRequest")



@_attrs_define
class TradeMarginCheckRequest:
    """ Order whose margin requirement is checked, v2 request DTO.

        Attributes:
            login (int | Unset): Login of the account the hypothetical order would be placed on.
            symbol (None | str | Unset): Symbol of the hypothetical order.
            type_ (None | OrderType | Unset): Type of the hypothetical order.
            volume (int | Unset): Order volume; one unit is 1/10000 lot in the standard variant and 1/100000000 in the
                extended one.
            price (float | Unset): Execution price of the hypothetical order.
     """

    login: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    type_: None | OrderType | Unset = UNSET
    volume: int | Unset = UNSET
    price: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

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

        price = self.price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if type_ is not UNSET:
            field_dict["type"] = type_
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

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

        price = d.pop("price", UNSET)

        trade_margin_check_request = cls(
            login=login,
            symbol=symbol,
            type_=type_,
            volume=volume,
            price=price,
        )

        return trade_margin_check_request

