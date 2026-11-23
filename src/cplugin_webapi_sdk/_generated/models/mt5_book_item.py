from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5BookItem")



@_attrs_define
class MT5BookItem:
    """ One entry of the Depth of Market, v2 read DTO.

        Attributes:
            type_ (None | str | Unset): Kind of the request: `Sell`, `Buy`, `SellMarket` or `BuyMarket`.
            price (float | Unset): Price of the entry.
            volume (int | Unset): Volume in the units the data provider supplies, as the trade server shows it.
            volume_ext (int | Unset): Volume with extended precision — eight decimal places.
     """

    type_: None | str | Unset = UNSET
    price: float | Unset = UNSET
    volume: int | Unset = UNSET
    volume_ext: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        price = self.price

        volume = self.volume

        volume_ext = self.volume_ext


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if price is not UNSET:
            field_dict["price"] = price
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_ext is not UNSET:
            field_dict["volumeExt"] = volume_ext

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        price = d.pop("price", UNSET)

        volume = d.pop("volume", UNSET)

        volume_ext = d.pop("volumeExt", UNSET)

        mt5_book_item = cls(
            type_=type_,
            price=price,
            volume=volume,
            volume_ext=volume_ext,
        )

        return mt5_book_item

