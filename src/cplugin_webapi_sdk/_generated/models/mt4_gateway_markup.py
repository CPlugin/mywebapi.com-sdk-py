from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GatewayMarkup")



@_attrs_define
class MT4GatewayMarkup:
    """ v2 DTO for a single MT4 gateway markup rule. Curated subset of the
    wrapper's ConGatewayMarkup — drops the 16-int Reserved padding.
    Source describes the external symbol (or a wildcard/group mask)
    being mapped onto Symbol on this server, with per-side spread
    adjustments BidMarkup and AskMarkup expressed in pips.

        Attributes:
            enable (bool | Unset): Whether the markup rule is active
            source (None | str | Unset): External symbol name, mask, or symbol-group identifier
            symbol (None | str | Unset): Local symbol name this markup applies to
            account_name (None | str | Unset): Gateway-account name (obsolete in modern MT4 builds — preserved for API
                completeness)
            account_id (int | Unset): Gateway-account internal id (obsolete — see AccountName note)
            bid_markup (int | Unset): Bid-side markup in pips (added to the external bid quote)
            ask_markup (int | Unset): Ask-side markup in pips (added to the external ask quote)
     """

    enable: bool | Unset = UNSET
    source: None | str | Unset = UNSET
    symbol: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    account_id: int | Unset = UNSET
    bid_markup: int | Unset = UNSET
    ask_markup: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        account_id = self.account_id

        bid_markup = self.bid_markup

        ask_markup = self.ask_markup


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enable is not UNSET:
            field_dict["enable"] = enable
        if source is not UNSET:
            field_dict["source"] = source
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if bid_markup is not UNSET:
            field_dict["bidMarkup"] = bid_markup
        if ask_markup is not UNSET:
            field_dict["askMarkup"] = ask_markup

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        account_id = d.pop("accountId", UNSET)

        bid_markup = d.pop("bidMarkup", UNSET)

        ask_markup = d.pop("askMarkup", UNSET)

        mt4_gateway_markup = cls(
            enable=enable,
            source=source,
            symbol=symbol,
            account_name=account_name,
            account_id=account_id,
            bid_markup=bid_markup,
            ask_markup=ask_markup,
        )

        return mt4_gateway_markup

