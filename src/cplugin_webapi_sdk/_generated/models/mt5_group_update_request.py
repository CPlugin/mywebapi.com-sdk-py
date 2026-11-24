from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_stop_out_mode import EnStopOutMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5GroupUpdateRequest")



@_attrs_define
class MT5GroupUpdateRequest:
    """ Fields of a group configuration to change. Every field is optional: a field left out keeps
    its current server value, so the same body is safe to send repeatedly.

        Attributes:
            margin_call (float | None | Unset): Margin call level, percent of the margin.
            margin_stop_out (float | None | Unset): Stop out level, percent of the margin.
            margin_so_mode (EnStopOutMode | None | Unset): Mode of checking the margin call and stop out levels.
            trade_flags (None | str | Unset): Group trade options.
     """

    margin_call: float | None | Unset = UNSET
    margin_stop_out: float | None | Unset = UNSET
    margin_so_mode: EnStopOutMode | None | Unset = UNSET
    trade_flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        margin_call: float | None | Unset
        if isinstance(self.margin_call, Unset):
            margin_call = UNSET
        else:
            margin_call = self.margin_call

        margin_stop_out: float | None | Unset
        if isinstance(self.margin_stop_out, Unset):
            margin_stop_out = UNSET
        else:
            margin_stop_out = self.margin_stop_out

        margin_so_mode: None | str | Unset
        if isinstance(self.margin_so_mode, Unset):
            margin_so_mode = UNSET
        elif isinstance(self.margin_so_mode, EnStopOutMode):
            margin_so_mode = self.margin_so_mode.value
        else:
            margin_so_mode = self.margin_so_mode

        trade_flags: None | str | Unset
        if isinstance(self.trade_flags, Unset):
            trade_flags = UNSET
        else:
            trade_flags = self.trade_flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if margin_call is not UNSET:
            field_dict["marginCall"] = margin_call
        if margin_stop_out is not UNSET:
            field_dict["marginStopOut"] = margin_stop_out
        if margin_so_mode is not UNSET:
            field_dict["marginSOMode"] = margin_so_mode
        if trade_flags is not UNSET:
            field_dict["tradeFlags"] = trade_flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_margin_call(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_call = _parse_margin_call(d.pop("marginCall", UNSET))


        def _parse_margin_stop_out(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_stop_out = _parse_margin_stop_out(d.pop("marginStopOut", UNSET))


        def _parse_margin_so_mode(data: object) -> EnStopOutMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                margin_so_mode_type_1 = EnStopOutMode(data)



                return margin_so_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnStopOutMode | None | Unset, data)

        margin_so_mode = _parse_margin_so_mode(d.pop("marginSOMode", UNSET))


        def _parse_trade_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_flags = _parse_trade_flags(d.pop("tradeFlags", UNSET))


        mt5_group_update_request = cls(
            margin_call=margin_call,
            margin_stop_out=margin_stop_out,
            margin_so_mode=margin_so_mode,
            trade_flags=trade_flags,
        )

        return mt5_group_update_request

