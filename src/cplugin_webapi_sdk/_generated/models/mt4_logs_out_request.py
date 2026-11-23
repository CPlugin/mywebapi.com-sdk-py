from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4LogsOutRequest")



@_attrs_define
class MT4LogsOutRequest:
    """ One record written to the trade server's Manager API log. The entry is
    filed under the connection that serves the request, with the result code
    and source text supplied by the caller.

        Attributes:
            code (None | str | Unset): Result code recorded with the entry, reported by name (e.g. `Ok`).<br/>One of: Ok,
                OkNone, Error, InvalidData, TechProblem, OldVersion, NoConnect, NotEnoughRights, TooFrequent, Malfunction,
                GenerateKey, SecuritySession, InvalidCompany, AccountDisabled, BadAccountInfo, PublicKeyMissing, TradeTimeout,
                TradeBadPrices, TradeBadStops, TradeBadVolume, TradeMarketClosed, TradeDisable, TradeNoMoney, TradePriceChanged,
                TradeOffquotes, TradeBrokerBusy, TradeRequote, TradeOrderLocked, TradeLongOnly, TradeTooManyReq, TradeAccepted,
                TradeProcess, TradeUserCancel, TradeModifyDenied, TradeContextBusy, TradeExpirationDenied, TradeTooManyOrders,
                TradeHedgeProhibited, TradeProhibitedByFIFO, UnhandledException. Case-insensitive; the numeric value is accepted
                too. Any other value is refused with error code Validation.
            source (None | str | Unset): Source of the entry — the subsystem or integration the record is attributed to
            message (None | str | Unset): Text of the entry
     """

    code: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if source is not UNSET:
            field_dict["source"] = source
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        mt4_logs_out_request = cls(
            code=code,
            source=source,
            message=message,
        )

        return mt4_logs_out_request

