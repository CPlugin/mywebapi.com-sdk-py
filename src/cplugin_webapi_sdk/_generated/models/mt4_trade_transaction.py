from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4TradeTransaction")



@_attrs_define
class MT4TradeTransaction:
    """ v2 DTO for a trade transaction — input AND output of `TradeTransaction`.
    The wrapper's `TradeTransInfo` is in/out: the caller fills the request
    fields (operation type, command, symbol, volume, price), submits via POST,
    and the server populates the resulting `Order` id (for Open) or
    echoes the modified record (for Modify/Close).

    Enum fields (`TradeTransactionType`, `TradeCommand`,
    `TradeRequestFlags`) are exposed as plain strings. Clients submit
    the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
    echoes the names back. This dodges the leaf-enum nested-generic STJ
    source-gen quirk documented in feedback-stj-enum-leaf-nested.

        Attributes:
            trade_transaction_type (None | str | Unset): Transaction type: OpenPending, OpenMarket, ModifyPending,
                ModifyTrade, DeletePending, CloseMarket, BalanceAdd, CreditAdd, etc.
            trade_command (None | str | Unset): Trade command: Buy, Sell, BuyLimit, SellLimit, BuyStop, SellStop, Balance,
                Credit
            trade_request_flags (None | str | Unset): Request flags: None, MarketOpen, Partial, NoExpiration, etc.
            expiration (datetime.datetime | Unset): Pending order expiration time. Default value means GTC.
            order (int | Unset): Order ticket. 0 on Open requests; server fills this on success.
            order_by (int | Unset): Login (account number). Required for Balance/Credit operations.
            symbol (None | str | Unset): Symbol (max 12 chars)
            volume (int | Unset): Volume in MT4 internal units. 1 lot = 100, so e.g. 250 = 2.5 lots.
            price (float | Unset): Order price
            sl (float | Unset): Stop-loss price (0 = none)
            tp (float | Unset): Take-profit price (0 = none)
            ie_deviation (int | Unset): Instant-execution price deviation tolerance (points)
            comment (None | str | Unset): Free-form comment (broker-visible)
            crc (int | Unset): CRC for transaction integrity; usually 0 (server fills).
     """

    trade_transaction_type: None | str | Unset = UNSET
    trade_command: None | str | Unset = UNSET
    trade_request_flags: None | str | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    order: int | Unset = UNSET
    order_by: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    volume: int | Unset = UNSET
    price: float | Unset = UNSET
    sl: float | Unset = UNSET
    tp: float | Unset = UNSET
    ie_deviation: int | Unset = UNSET
    comment: None | str | Unset = UNSET
    crc: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        trade_transaction_type: None | str | Unset
        if isinstance(self.trade_transaction_type, Unset):
            trade_transaction_type = UNSET
        else:
            trade_transaction_type = self.trade_transaction_type

        trade_command: None | str | Unset
        if isinstance(self.trade_command, Unset):
            trade_command = UNSET
        else:
            trade_command = self.trade_command

        trade_request_flags: None | str | Unset
        if isinstance(self.trade_request_flags, Unset):
            trade_request_flags = UNSET
        else:
            trade_request_flags = self.trade_request_flags

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        order = self.order

        order_by = self.order_by

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        volume = self.volume

        price = self.price

        sl = self.sl

        tp = self.tp

        ie_deviation = self.ie_deviation

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        crc = self.crc


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if trade_transaction_type is not UNSET:
            field_dict["tradeTransactionType"] = trade_transaction_type
        if trade_command is not UNSET:
            field_dict["tradeCommand"] = trade_command
        if trade_request_flags is not UNSET:
            field_dict["tradeRequestFlags"] = trade_request_flags
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if order is not UNSET:
            field_dict["order"] = order
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if sl is not UNSET:
            field_dict["sl"] = sl
        if tp is not UNSET:
            field_dict["tp"] = tp
        if ie_deviation is not UNSET:
            field_dict["ieDeviation"] = ie_deviation
        if comment is not UNSET:
            field_dict["comment"] = comment
        if crc is not UNSET:
            field_dict["crc"] = crc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_trade_transaction_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_transaction_type = _parse_trade_transaction_type(d.pop("tradeTransactionType", UNSET))


        def _parse_trade_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_command = _parse_trade_command(d.pop("tradeCommand", UNSET))


        def _parse_trade_request_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_request_flags = _parse_trade_request_flags(d.pop("tradeRequestFlags", UNSET))


        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration,  Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)




        order = d.pop("order", UNSET)

        order_by = d.pop("orderBy", UNSET)

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        volume = d.pop("volume", UNSET)

        price = d.pop("price", UNSET)

        sl = d.pop("sl", UNSET)

        tp = d.pop("tp", UNSET)

        ie_deviation = d.pop("ieDeviation", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        crc = d.pop("crc", UNSET)

        mt4_trade_transaction = cls(
            trade_transaction_type=trade_transaction_type,
            trade_command=trade_command,
            trade_request_flags=trade_request_flags,
            expiration=expiration,
            order=order,
            order_by=order_by,
            symbol=symbol,
            volume=volume,
            price=price,
            sl=sl,
            tp=tp,
            ie_deviation=ie_deviation,
            comment=comment,
            crc=crc,
        )

        return mt4_trade_transaction

