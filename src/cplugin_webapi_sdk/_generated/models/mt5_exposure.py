from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Exposure")



@_attrs_define
class MT5Exposure:
    """ Exposure of the company on one asset, v2 read DTO.

        Attributes:
            symbol (None | str | Unset): Name of the asset; empty in the net total record.
            digits (int | Unset): Number of decimal places in the price of the asset.
            volume_clients (float | Unset): Volume of client positions on the asset.
            volume_coverage (float | Unset): Volume of positions on the hedging account for the asset.
            price_rate (float | Unset): Rate of conversion of the net total to the summary currency.
            volume_net (float | Unset): Difference between the client volume and the hedged volume.
     """

    symbol: None | str | Unset = UNSET
    digits: int | Unset = UNSET
    volume_clients: float | Unset = UNSET
    volume_coverage: float | Unset = UNSET
    price_rate: float | Unset = UNSET
    volume_net: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        digits = self.digits

        volume_clients = self.volume_clients

        volume_coverage = self.volume_coverage

        price_rate = self.price_rate

        volume_net = self.volume_net


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if digits is not UNSET:
            field_dict["digits"] = digits
        if volume_clients is not UNSET:
            field_dict["volumeClients"] = volume_clients
        if volume_coverage is not UNSET:
            field_dict["volumeCoverage"] = volume_coverage
        if price_rate is not UNSET:
            field_dict["priceRate"] = price_rate
        if volume_net is not UNSET:
            field_dict["volumeNet"] = volume_net

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        digits = d.pop("digits", UNSET)

        volume_clients = d.pop("volumeClients", UNSET)

        volume_coverage = d.pop("volumeCoverage", UNSET)

        price_rate = d.pop("priceRate", UNSET)

        volume_net = d.pop("volumeNet", UNSET)

        mt5_exposure = cls(
            symbol=symbol,
            digits=digits,
            volume_clients=volume_clients,
            volume_coverage=volume_coverage,
            price_rate=price_rate,
            volume_net=volume_net,
        )

        return mt5_exposure

