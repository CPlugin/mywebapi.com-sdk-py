from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GroupMargin")



@_attrs_define
class MT4GroupMargin:
    """ v2 DTO for one of a group's "special securities" margin overrides. Curated
    from `ConGroupMargin` — the wrapper's per-symbol swap/margin overrides
    stored as a 128-element array on `ConGroup.SecMargins`. The
    `Reserved` int[7] padding is dropped.

        Attributes:
            symbol (None | str | Unset): Symbol the override applies to (max 12 chars)
            swap_long (float | Unset): Swap charge for long positions
            swap_short (float | Unset): Swap charge for short positions
            margin_divider (float | Unset): Margin divider override (1.0 = use default)
     """

    symbol: None | str | Unset = UNSET
    swap_long: float | Unset = UNSET
    swap_short: float | Unset = UNSET
    margin_divider: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        swap_long = self.swap_long

        swap_short = self.swap_short

        margin_divider = self.margin_divider


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if swap_long is not UNSET:
            field_dict["swapLong"] = swap_long
        if swap_short is not UNSET:
            field_dict["swapShort"] = swap_short
        if margin_divider is not UNSET:
            field_dict["marginDivider"] = margin_divider

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


        swap_long = d.pop("swapLong", UNSET)

        swap_short = d.pop("swapShort", UNSET)

        margin_divider = d.pop("marginDivider", UNSET)

        mt4_group_margin = cls(
            symbol=symbol,
            swap_long=swap_long,
            swap_short=swap_short,
            margin_divider=margin_divider,
        )

        return mt4_group_margin

