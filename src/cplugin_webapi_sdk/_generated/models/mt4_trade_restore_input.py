from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.trade_command import TradeCommand
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4TradeRestoreInput")



@_attrs_define
class MT4TradeRestoreInput:
    """ v2 narrow input DTO for `BackupRestoreOrders`. Carries the trade
    identity + economic state that a disaster-recovery flow needs.

        Attributes:
            order (int | Unset): Order ticket (the input array position is the binding key for the result)
            login (int | Unset): Owner's login
            symbol (None | str | Unset): Symbol (e.g. `EURUSD`; max 12 ASCII chars on the platform side)
            trade_command (TradeCommand | Unset):
            volume (int | Unset): Volume in 1/100 lots (15 = 0.15 lot)
            open_price (float | Unset): Open price
            sl (float | Unset): Stop loss
            tp (float | Unset): Take profit
            close_price (float | Unset): Close price (0 for still-open trades)
            profit (float | Unset): Trade profit/loss
            storage (float | Unset): Swap (rollover charge)
            commission (float | Unset): Commission
            open_time (datetime.datetime | Unset): Open time (UTC)
            close_time (datetime.datetime | Unset): Close time (UTC; default for still-open)
            expiration (datetime.datetime | Unset): Expiration time (UTC; default for non-pending orders)
            magic (int | Unset): Magic number (EA identifier)
            comment (None | str | Unset): Free-form comment (max ~31 ASCII chars on the platform side)
     """

    order: int | Unset = UNSET
    login: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    trade_command: TradeCommand | Unset = UNSET
    volume: int | Unset = UNSET
    open_price: float | Unset = UNSET
    sl: float | Unset = UNSET
    tp: float | Unset = UNSET
    close_price: float | Unset = UNSET
    profit: float | Unset = UNSET
    storage: float | Unset = UNSET
    commission: float | Unset = UNSET
    open_time: datetime.datetime | Unset = UNSET
    close_time: datetime.datetime | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    magic: int | Unset = UNSET
    comment: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        order = self.order

        login = self.login

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        trade_command: str | Unset = UNSET
        if not isinstance(self.trade_command, Unset):
            trade_command = self.trade_command.value


        volume = self.volume

        open_price = self.open_price

        sl = self.sl

        tp = self.tp

        close_price = self.close_price

        profit = self.profit

        storage = self.storage

        commission = self.commission

        open_time: str | Unset = UNSET
        if not isinstance(self.open_time, Unset):
            open_time = self.open_time.isoformat()

        close_time: str | Unset = UNSET
        if not isinstance(self.close_time, Unset):
            close_time = self.close_time.isoformat()

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        magic = self.magic

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order is not UNSET:
            field_dict["order"] = order
        if login is not UNSET:
            field_dict["login"] = login
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if trade_command is not UNSET:
            field_dict["tradeCommand"] = trade_command
        if volume is not UNSET:
            field_dict["volume"] = volume
        if open_price is not UNSET:
            field_dict["openPrice"] = open_price
        if sl is not UNSET:
            field_dict["sl"] = sl
        if tp is not UNSET:
            field_dict["tp"] = tp
        if close_price is not UNSET:
            field_dict["closePrice"] = close_price
        if profit is not UNSET:
            field_dict["profit"] = profit
        if storage is not UNSET:
            field_dict["storage"] = storage
        if commission is not UNSET:
            field_dict["commission"] = commission
        if open_time is not UNSET:
            field_dict["openTime"] = open_time
        if close_time is not UNSET:
            field_dict["closeTime"] = close_time
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if magic is not UNSET:
            field_dict["magic"] = magic
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order = d.pop("order", UNSET)

        login = d.pop("login", UNSET)

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        _trade_command = d.pop("tradeCommand", UNSET)
        trade_command: TradeCommand | Unset
        if isinstance(_trade_command,  Unset):
            trade_command = UNSET
        else:
            trade_command = TradeCommand(_trade_command)




        volume = d.pop("volume", UNSET)

        open_price = d.pop("openPrice", UNSET)

        sl = d.pop("sl", UNSET)

        tp = d.pop("tp", UNSET)

        close_price = d.pop("closePrice", UNSET)

        profit = d.pop("profit", UNSET)

        storage = d.pop("storage", UNSET)

        commission = d.pop("commission", UNSET)

        _open_time = d.pop("openTime", UNSET)
        open_time: datetime.datetime | Unset
        if isinstance(_open_time,  Unset):
            open_time = UNSET
        else:
            open_time = datetime.datetime.fromisoformat(_open_time)




        _close_time = d.pop("closeTime", UNSET)
        close_time: datetime.datetime | Unset
        if isinstance(_close_time,  Unset):
            close_time = UNSET
        else:
            close_time = datetime.datetime.fromisoformat(_close_time)




        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration,  Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)




        magic = d.pop("magic", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        mt4_trade_restore_input = cls(
            order=order,
            login=login,
            symbol=symbol,
            trade_command=trade_command,
            volume=volume,
            open_price=open_price,
            sl=sl,
            tp=tp,
            close_price=close_price,
            profit=profit,
            storage=storage,
            commission=commission,
            open_time=open_time,
            close_time=close_time,
            expiration=expiration,
            magic=magic,
            comment=comment,
        )

        return mt4_trade_restore_input

