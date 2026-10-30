from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.activation_type import ActivationType
from ..models.trade_command import TradeCommand
from ..models.trade_record_reason import TradeRecordReason
from ..models.trade_record_state import TradeRecordState
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4Trade")



@_attrs_define
class MT4Trade:
    """ v2 DTO mirroring the platform's TradeRecord. The set of fields is curated
    for typical client use-cases — order monitoring, P&L reporting, trade
    history reconciliation. Internal padding/reserved/gateway-internal/raw
    underscore-prefixed fields are intentionally excluded, as are the raw
    conversion-rate and API data blocks (ConvRates, ConvReserv, APIData).
    Enum members (TradeCommand, TradeRecordState, TradeRecordReason,
    ActivationType) are returned as their names — e.g. "Buy" rather than 0.

        Attributes:
            order (int | Unset): Order ticket number
            login (int | Unset): Owner account login
            symbol (None | str | Unset): Symbol traded (e.g. EURUSD)
            digits (int | Unset): Symbol precision (number of digits after the decimal point)
            trade_command (TradeCommand | Unset):
            volume (int | Unset): Volume stored ×100 (e.g. 15 means 0.15 lots — see VolumeLots)
            volume_lots (float | Unset): Volume expressed in lots, for human consumption (Volume / 100)
            trade_record_state (TradeRecordState | Unset):
            open_price (float | Unset): Price at which the order was opened
            sl (float | Unset): Stop-loss price (0 if unset)
            tp (float | Unset): Take-profit price (0 if unset)
            open_time (datetime.datetime | Unset): Order open timestamp
            close_time (datetime.datetime | Unset): Order close timestamp (default for still-open orders)
            close_price (float | Unset): Price at which the order was closed
            commission (float | Unset): Broker commission
            commission_agent (float | Unset): Agent (IB) commission
            storage (float | Unset): Accumulated swap / rollover charges
            profit (float | Unset): Realised / floating profit
            taxes (float | Unset): Taxes withheld
            magic (int | Unset): Expert advisor magic number — client-supplied tag
            comment (None | str | Unset): Free-form order comment
            expiration (datetime.datetime | Unset): Expiration timestamp for pending orders
            trade_record_reason (TradeRecordReason | Unset):
            activation_type (ActivationType | Unset):
            time_stamp (datetime.datetime | Unset): Last modification timestamp of the trade record
            margin_rate (float | Unset): Margin conversion rate (margin currency → deposit currency)
     """

    order: int | Unset = UNSET
    login: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    digits: int | Unset = UNSET
    trade_command: TradeCommand | Unset = UNSET
    volume: int | Unset = UNSET
    volume_lots: float | Unset = UNSET
    trade_record_state: TradeRecordState | Unset = UNSET
    open_price: float | Unset = UNSET
    sl: float | Unset = UNSET
    tp: float | Unset = UNSET
    open_time: datetime.datetime | Unset = UNSET
    close_time: datetime.datetime | Unset = UNSET
    close_price: float | Unset = UNSET
    commission: float | Unset = UNSET
    commission_agent: float | Unset = UNSET
    storage: float | Unset = UNSET
    profit: float | Unset = UNSET
    taxes: float | Unset = UNSET
    magic: int | Unset = UNSET
    comment: None | str | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    trade_record_reason: TradeRecordReason | Unset = UNSET
    activation_type: ActivationType | Unset = UNSET
    time_stamp: datetime.datetime | Unset = UNSET
    margin_rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        order = self.order

        login = self.login

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        digits = self.digits

        trade_command: str | Unset = UNSET
        if not isinstance(self.trade_command, Unset):
            trade_command = self.trade_command.value


        volume = self.volume

        volume_lots = self.volume_lots

        trade_record_state: str | Unset = UNSET
        if not isinstance(self.trade_record_state, Unset):
            trade_record_state = self.trade_record_state.value


        open_price = self.open_price

        sl = self.sl

        tp = self.tp

        open_time: str | Unset = UNSET
        if not isinstance(self.open_time, Unset):
            open_time = self.open_time.isoformat()

        close_time: str | Unset = UNSET
        if not isinstance(self.close_time, Unset):
            close_time = self.close_time.isoformat()

        close_price = self.close_price

        commission = self.commission

        commission_agent = self.commission_agent

        storage = self.storage

        profit = self.profit

        taxes = self.taxes

        magic = self.magic

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        trade_record_reason: str | Unset = UNSET
        if not isinstance(self.trade_record_reason, Unset):
            trade_record_reason = self.trade_record_reason.value


        activation_type: str | Unset = UNSET
        if not isinstance(self.activation_type, Unset):
            activation_type = self.activation_type.value


        time_stamp: str | Unset = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        margin_rate = self.margin_rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order is not UNSET:
            field_dict["order"] = order
        if login is not UNSET:
            field_dict["login"] = login
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if digits is not UNSET:
            field_dict["digits"] = digits
        if trade_command is not UNSET:
            field_dict["tradeCommand"] = trade_command
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_lots is not UNSET:
            field_dict["volumeLots"] = volume_lots
        if trade_record_state is not UNSET:
            field_dict["tradeRecordState"] = trade_record_state
        if open_price is not UNSET:
            field_dict["openPrice"] = open_price
        if sl is not UNSET:
            field_dict["sl"] = sl
        if tp is not UNSET:
            field_dict["tp"] = tp
        if open_time is not UNSET:
            field_dict["openTime"] = open_time
        if close_time is not UNSET:
            field_dict["closeTime"] = close_time
        if close_price is not UNSET:
            field_dict["closePrice"] = close_price
        if commission is not UNSET:
            field_dict["commission"] = commission
        if commission_agent is not UNSET:
            field_dict["commissionAgent"] = commission_agent
        if storage is not UNSET:
            field_dict["storage"] = storage
        if profit is not UNSET:
            field_dict["profit"] = profit
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if magic is not UNSET:
            field_dict["magic"] = magic
        if comment is not UNSET:
            field_dict["comment"] = comment
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if trade_record_reason is not UNSET:
            field_dict["tradeRecordReason"] = trade_record_reason
        if activation_type is not UNSET:
            field_dict["activationType"] = activation_type
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if margin_rate is not UNSET:
            field_dict["marginRate"] = margin_rate

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


        digits = d.pop("digits", UNSET)

        _trade_command = d.pop("tradeCommand", UNSET)
        trade_command: TradeCommand | Unset
        if isinstance(_trade_command,  Unset):
            trade_command = UNSET
        else:
            trade_command = TradeCommand(_trade_command)




        volume = d.pop("volume", UNSET)

        volume_lots = d.pop("volumeLots", UNSET)

        _trade_record_state = d.pop("tradeRecordState", UNSET)
        trade_record_state: TradeRecordState | Unset
        if isinstance(_trade_record_state,  Unset):
            trade_record_state = UNSET
        else:
            trade_record_state = TradeRecordState(_trade_record_state)




        open_price = d.pop("openPrice", UNSET)

        sl = d.pop("sl", UNSET)

        tp = d.pop("tp", UNSET)

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




        close_price = d.pop("closePrice", UNSET)

        commission = d.pop("commission", UNSET)

        commission_agent = d.pop("commissionAgent", UNSET)

        storage = d.pop("storage", UNSET)

        profit = d.pop("profit", UNSET)

        taxes = d.pop("taxes", UNSET)

        magic = d.pop("magic", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration,  Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)




        _trade_record_reason = d.pop("tradeRecordReason", UNSET)
        trade_record_reason: TradeRecordReason | Unset
        if isinstance(_trade_record_reason,  Unset):
            trade_record_reason = UNSET
        else:
            trade_record_reason = TradeRecordReason(_trade_record_reason)




        _activation_type = d.pop("activationType", UNSET)
        activation_type: ActivationType | Unset
        if isinstance(_activation_type,  Unset):
            activation_type = UNSET
        else:
            activation_type = ActivationType(_activation_type)




        _time_stamp = d.pop("timeStamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp,  Unset):
            time_stamp = UNSET
        else:
            time_stamp = datetime.datetime.fromisoformat(_time_stamp)




        margin_rate = d.pop("marginRate", UNSET)

        mt4_trade = cls(
            order=order,
            login=login,
            symbol=symbol,
            digits=digits,
            trade_command=trade_command,
            volume=volume,
            volume_lots=volume_lots,
            trade_record_state=trade_record_state,
            open_price=open_price,
            sl=sl,
            tp=tp,
            open_time=open_time,
            close_time=close_time,
            close_price=close_price,
            commission=commission,
            commission_agent=commission_agent,
            storage=storage,
            profit=profit,
            taxes=taxes,
            magic=magic,
            comment=comment,
            expiration=expiration,
            trade_record_reason=trade_record_reason,
            activation_type=activation_type,
            time_stamp=time_stamp,
            margin_rate=margin_rate,
        )

        return mt4_trade

