from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5PositionSplitRequest")



@_attrs_define
class MT5PositionSplitRequest:
    """ Request body of the position split: the positions to convert, the conversion ratio and the
    rounding rules applied to the recalculated prices and volumes.

        Attributes:
            tickets (list[int] | None | Unset): Tickets of the positions to split or consolidate. Every ticket must belong
                to the trade
                server the request is addressed to.
            adjustments (list[float] | None | Unset): Balance adjustments, one per ticket and in the same order. Omit the
                whole array to let the
                server calculate the adjustments; send an array of zeros when no adjustment is needed.
            new_shares (int | Unset): Number of shares after the conversion (the numerator of the ratio).
            old_shares (int | Unset): Number of shares before the conversion (the denominator of the ratio).
            round_rule_price (int | Unset): Price rounding rule when the recalculated price has more digits than the symbol
                allows.
            round_rule_volume (int | Unset): Volume rounding rule when the conversion leaves a fractional number of shares.
            flags (int | Unset): Additional split options.
     """

    tickets: list[int] | None | Unset = UNSET
    adjustments: list[float] | None | Unset = UNSET
    new_shares: int | Unset = UNSET
    old_shares: int | Unset = UNSET
    round_rule_price: int | Unset = UNSET
    round_rule_volume: int | Unset = UNSET
    flags: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        tickets: list[int] | None | Unset
        if isinstance(self.tickets, Unset):
            tickets = UNSET
        elif isinstance(self.tickets, list):
            tickets = self.tickets


        else:
            tickets = self.tickets

        adjustments: list[float] | None | Unset
        if isinstance(self.adjustments, Unset):
            adjustments = UNSET
        elif isinstance(self.adjustments, list):
            adjustments = self.adjustments


        else:
            adjustments = self.adjustments

        new_shares = self.new_shares

        old_shares = self.old_shares

        round_rule_price = self.round_rule_price

        round_rule_volume = self.round_rule_volume

        flags = self.flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if tickets is not UNSET:
            field_dict["tickets"] = tickets
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if new_shares is not UNSET:
            field_dict["newShares"] = new_shares
        if old_shares is not UNSET:
            field_dict["oldShares"] = old_shares
        if round_rule_price is not UNSET:
            field_dict["roundRulePrice"] = round_rule_price
        if round_rule_volume is not UNSET:
            field_dict["roundRuleVolume"] = round_rule_volume
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_tickets(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tickets_type_0 = cast(list[int], data)

                return tickets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        tickets = _parse_tickets(d.pop("tickets", UNSET))


        def _parse_adjustments(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                adjustments_type_0 = cast(list[float], data)

                return adjustments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        adjustments = _parse_adjustments(d.pop("adjustments", UNSET))


        new_shares = d.pop("newShares", UNSET)

        old_shares = d.pop("oldShares", UNSET)

        round_rule_price = d.pop("roundRulePrice", UNSET)

        round_rule_volume = d.pop("roundRuleVolume", UNSET)

        flags = d.pop("flags", UNSET)

        mt5_position_split_request = cls(
            tickets=tickets,
            adjustments=adjustments,
            new_shares=new_shares,
            old_shares=old_shares,
            round_rule_price=round_rule_price,
            round_rule_volume=round_rule_volume,
            flags=flags,
        )

        return mt5_position_split_request

