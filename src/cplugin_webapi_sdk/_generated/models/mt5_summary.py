from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Summary")



@_attrs_define
class MT5Summary:
    """ Summary of the client and hedging positions of one symbol, v2 read DTO.

        Attributes:
            symbol (None | str | Unset): Symbol the record is calculated for; empty in the total record.
            digits (int | Unset): Number of decimal places in the weighted average prices.
            position_clients (int | Unset): Number of open client positions on the symbol.
            position_coverage (int | Unset): Number of hedging positions on the symbol.
            volume_buy_clients (int | Unset): Total volume of client buy positions.
            volume_buy_clients_ext (int | Unset): Total volume of client buy positions with extended precision.
            volume_buy_coverage (int | Unset): Total volume of hedging buy positions.
            volume_buy_coverage_ext (int | Unset): Total volume of hedging buy positions with extended precision.
            volume_sell_clients (int | Unset): Total volume of client sell positions.
            volume_sell_clients_ext (int | Unset): Total volume of client sell positions with extended precision.
            volume_sell_coverage (int | Unset): Total volume of hedging sell positions.
            volume_sell_coverage_ext (int | Unset): Total volume of hedging sell positions with extended precision.
            volume_net (float | Unset): Net total: client buy volume minus client sell volume, with the hedged amount
                deducted.
            price_buy_clients (float | Unset): Weighted average open price of client buy positions.
            price_buy_coverage (float | Unset): Weighted average open price of hedging buy positions.
            price_sell_clients (float | Unset): Weighted average open price of client sell positions.
            price_sell_coverage (float | Unset): Weighted average open price of hedging sell positions.
            profit_clients (float | Unset): Total profit or loss of client positions, excluding swaps and commissions.
            profit_coverage (float | Unset): Total profit or loss of hedging positions, excluding swaps and commissions.
            profit_full_clients (float | Unset): Total profit or loss of client positions, including swaps and commissions.
            profit_full_coverage (float | Unset): Total profit or loss of hedging positions, including swaps and
                commissions.
            profit_uncovered (float | Unset): Difference between the client and the hedging profit, excluding swaps and
                commissions.
            profit_uncovered_full (float | Unset): Difference between the client and the hedging profit, including swaps and
                commissions.
     """

    symbol: None | str | Unset = UNSET
    digits: int | Unset = UNSET
    position_clients: int | Unset = UNSET
    position_coverage: int | Unset = UNSET
    volume_buy_clients: int | Unset = UNSET
    volume_buy_clients_ext: int | Unset = UNSET
    volume_buy_coverage: int | Unset = UNSET
    volume_buy_coverage_ext: int | Unset = UNSET
    volume_sell_clients: int | Unset = UNSET
    volume_sell_clients_ext: int | Unset = UNSET
    volume_sell_coverage: int | Unset = UNSET
    volume_sell_coverage_ext: int | Unset = UNSET
    volume_net: float | Unset = UNSET
    price_buy_clients: float | Unset = UNSET
    price_buy_coverage: float | Unset = UNSET
    price_sell_clients: float | Unset = UNSET
    price_sell_coverage: float | Unset = UNSET
    profit_clients: float | Unset = UNSET
    profit_coverage: float | Unset = UNSET
    profit_full_clients: float | Unset = UNSET
    profit_full_coverage: float | Unset = UNSET
    profit_uncovered: float | Unset = UNSET
    profit_uncovered_full: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        digits = self.digits

        position_clients = self.position_clients

        position_coverage = self.position_coverage

        volume_buy_clients = self.volume_buy_clients

        volume_buy_clients_ext = self.volume_buy_clients_ext

        volume_buy_coverage = self.volume_buy_coverage

        volume_buy_coverage_ext = self.volume_buy_coverage_ext

        volume_sell_clients = self.volume_sell_clients

        volume_sell_clients_ext = self.volume_sell_clients_ext

        volume_sell_coverage = self.volume_sell_coverage

        volume_sell_coverage_ext = self.volume_sell_coverage_ext

        volume_net = self.volume_net

        price_buy_clients = self.price_buy_clients

        price_buy_coverage = self.price_buy_coverage

        price_sell_clients = self.price_sell_clients

        price_sell_coverage = self.price_sell_coverage

        profit_clients = self.profit_clients

        profit_coverage = self.profit_coverage

        profit_full_clients = self.profit_full_clients

        profit_full_coverage = self.profit_full_coverage

        profit_uncovered = self.profit_uncovered

        profit_uncovered_full = self.profit_uncovered_full


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if digits is not UNSET:
            field_dict["digits"] = digits
        if position_clients is not UNSET:
            field_dict["positionClients"] = position_clients
        if position_coverage is not UNSET:
            field_dict["positionCoverage"] = position_coverage
        if volume_buy_clients is not UNSET:
            field_dict["volumeBuyClients"] = volume_buy_clients
        if volume_buy_clients_ext is not UNSET:
            field_dict["volumeBuyClientsExt"] = volume_buy_clients_ext
        if volume_buy_coverage is not UNSET:
            field_dict["volumeBuyCoverage"] = volume_buy_coverage
        if volume_buy_coverage_ext is not UNSET:
            field_dict["volumeBuyCoverageExt"] = volume_buy_coverage_ext
        if volume_sell_clients is not UNSET:
            field_dict["volumeSellClients"] = volume_sell_clients
        if volume_sell_clients_ext is not UNSET:
            field_dict["volumeSellClientsExt"] = volume_sell_clients_ext
        if volume_sell_coverage is not UNSET:
            field_dict["volumeSellCoverage"] = volume_sell_coverage
        if volume_sell_coverage_ext is not UNSET:
            field_dict["volumeSellCoverageExt"] = volume_sell_coverage_ext
        if volume_net is not UNSET:
            field_dict["volumeNet"] = volume_net
        if price_buy_clients is not UNSET:
            field_dict["priceBuyClients"] = price_buy_clients
        if price_buy_coverage is not UNSET:
            field_dict["priceBuyCoverage"] = price_buy_coverage
        if price_sell_clients is not UNSET:
            field_dict["priceSellClients"] = price_sell_clients
        if price_sell_coverage is not UNSET:
            field_dict["priceSellCoverage"] = price_sell_coverage
        if profit_clients is not UNSET:
            field_dict["profitClients"] = profit_clients
        if profit_coverage is not UNSET:
            field_dict["profitCoverage"] = profit_coverage
        if profit_full_clients is not UNSET:
            field_dict["profitFullClients"] = profit_full_clients
        if profit_full_coverage is not UNSET:
            field_dict["profitFullCoverage"] = profit_full_coverage
        if profit_uncovered is not UNSET:
            field_dict["profitUncovered"] = profit_uncovered
        if profit_uncovered_full is not UNSET:
            field_dict["profitUncoveredFull"] = profit_uncovered_full

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

        position_clients = d.pop("positionClients", UNSET)

        position_coverage = d.pop("positionCoverage", UNSET)

        volume_buy_clients = d.pop("volumeBuyClients", UNSET)

        volume_buy_clients_ext = d.pop("volumeBuyClientsExt", UNSET)

        volume_buy_coverage = d.pop("volumeBuyCoverage", UNSET)

        volume_buy_coverage_ext = d.pop("volumeBuyCoverageExt", UNSET)

        volume_sell_clients = d.pop("volumeSellClients", UNSET)

        volume_sell_clients_ext = d.pop("volumeSellClientsExt", UNSET)

        volume_sell_coverage = d.pop("volumeSellCoverage", UNSET)

        volume_sell_coverage_ext = d.pop("volumeSellCoverageExt", UNSET)

        volume_net = d.pop("volumeNet", UNSET)

        price_buy_clients = d.pop("priceBuyClients", UNSET)

        price_buy_coverage = d.pop("priceBuyCoverage", UNSET)

        price_sell_clients = d.pop("priceSellClients", UNSET)

        price_sell_coverage = d.pop("priceSellCoverage", UNSET)

        profit_clients = d.pop("profitClients", UNSET)

        profit_coverage = d.pop("profitCoverage", UNSET)

        profit_full_clients = d.pop("profitFullClients", UNSET)

        profit_full_coverage = d.pop("profitFullCoverage", UNSET)

        profit_uncovered = d.pop("profitUncovered", UNSET)

        profit_uncovered_full = d.pop("profitUncoveredFull", UNSET)

        mt5_summary = cls(
            symbol=symbol,
            digits=digits,
            position_clients=position_clients,
            position_coverage=position_coverage,
            volume_buy_clients=volume_buy_clients,
            volume_buy_clients_ext=volume_buy_clients_ext,
            volume_buy_coverage=volume_buy_coverage,
            volume_buy_coverage_ext=volume_buy_coverage_ext,
            volume_sell_clients=volume_sell_clients,
            volume_sell_clients_ext=volume_sell_clients_ext,
            volume_sell_coverage=volume_sell_coverage,
            volume_sell_coverage_ext=volume_sell_coverage_ext,
            volume_net=volume_net,
            price_buy_clients=price_buy_clients,
            price_buy_coverage=price_buy_coverage,
            price_sell_clients=price_sell_clients,
            price_sell_coverage=price_sell_coverage,
            profit_clients=profit_clients,
            profit_coverage=profit_coverage,
            profit_full_clients=profit_full_clients,
            profit_full_coverage=profit_full_coverage,
            profit_uncovered=profit_uncovered,
            profit_uncovered_full=profit_uncovered_full,
        )

        return mt5_summary

