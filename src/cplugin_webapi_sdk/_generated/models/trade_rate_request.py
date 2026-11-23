from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TradeRateRequest")



@_attrs_define
class TradeRateRequest:
    """ Conditions of a conversion rate calculation, v2 request DTO.

        Attributes:
            base (None | str | Unset): Currency bought or sold, a three-letter code such as `EUR`.
            currency (None | str | Unset): Currency the base currency is paid with, a three-letter code such as `USD`.
            group (None | str | Unset): Group whose spread adjustment is applied; omitted means market prices.
            symbol (None | str | Unset): Symbol to use in place of the market one.
            price (float | None | Unset): Price of the symbol above; ignored for the symbols always converted at the market
                price.
     """

    base: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    symbol: None | str | Unset = UNSET
    price: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        base: None | str | Unset
        if isinstance(self.base, Unset):
            base = UNSET
        else:
            base = self.base

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

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

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if base is not UNSET:
            field_dict["base"] = base
        if currency is not UNSET:
            field_dict["currency"] = currency
        if group is not UNSET:
            field_dict["group"] = group
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base = _parse_base(d.pop("base", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


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


        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))


        trade_rate_request = cls(
            base=base,
            currency=currency,
            group=group,
            symbol=symbol,
            price=price,
        )

        return trade_rate_request

