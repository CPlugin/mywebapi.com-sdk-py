from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4TickRecord")



@_attrs_define
class MT4TickRecord:
    """ v2 DTO for one historical tick from `TicksRequest`. Same fields as the
    wrapper's `TickRecord`; `Ctm` is renamed to `Time` at the API
    boundary (consistent with CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4TickInfo). The wrapper's
    `TickRequestFlags` enum is exposed as a string to avoid the leaf-enum
    nested-generic serialization issue documented in feedback-stj-enum-leaf-nested.

        Attributes:
            time (datetime.datetime | Unset): Server-side tick timestamp (UTC)
            bid (float | Unset): Bid price
            ask (float | Unset): Ask price
            data_feed (int | Unset): Index of the data feed source
            flags (None | str | Unset): Tick flags as string — combination of `Raw`, `Normal`, `All`.
                String-typed for the same STJ source-gen reason as CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4ServerLog.Code.
     """

    time: datetime.datetime | Unset = UNSET
    bid: float | Unset = UNSET
    ask: float | Unset = UNSET
    data_feed: int | Unset = UNSET
    flags: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        bid = self.bid

        ask = self.ask

        data_feed = self.data_feed

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask
        if data_feed is not UNSET:
            field_dict["dataFeed"] = data_feed
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        data_feed = d.pop("dataFeed", UNSET)

        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        mt4_tick_record = cls(
            time=time,
            bid=bid,
            ask=ask,
            data_feed=data_feed,
            flags=flags,
        )

        return mt4_tick_record

