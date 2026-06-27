from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_commission_mode import EnCommissionMode
from ..models.en_commission_volume_type import EnCommissionVolumeType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5ConCommTier")



@_attrs_define
class MT5ConCommTier:
    """ 
        Attributes:
            mode (EnCommissionMode | None | Unset): EnCommissionMode
            type_ (EnCommissionVolumeType | None | Unset): EnCommissionVolumeType
            value (float | None | Unset): commission value
            minimal (float | None | Unset): minimal commission value
            range_from (float | None | Unset): tier range from
            range_to (float | None | Unset): tier range to
            currency (None | str | Unset): commission currency (for Mode==COMM_MONEY_SPECIFIED)
            maximal (float | None | Unset): maximal commission value
     """

    mode: EnCommissionMode | None | Unset = UNSET
    type_: EnCommissionVolumeType | None | Unset = UNSET
    value: float | None | Unset = UNSET
    minimal: float | None | Unset = UNSET
    range_from: float | None | Unset = UNSET
    range_to: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    maximal: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, EnCommissionMode):
            mode = self.mode.value
        else:
            mode = self.mode

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, EnCommissionVolumeType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        minimal: float | None | Unset
        if isinstance(self.minimal, Unset):
            minimal = UNSET
        else:
            minimal = self.minimal

        range_from: float | None | Unset
        if isinstance(self.range_from, Unset):
            range_from = UNSET
        else:
            range_from = self.range_from

        range_to: float | None | Unset
        if isinstance(self.range_to, Unset):
            range_to = UNSET
        else:
            range_to = self.range_to

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        maximal: float | None | Unset
        if isinstance(self.maximal, Unset):
            maximal = UNSET
        else:
            maximal = self.maximal


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if mode is not UNSET:
            field_dict["mode"] = mode
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if minimal is not UNSET:
            field_dict["minimal"] = minimal
        if range_from is not UNSET:
            field_dict["rangeFrom"] = range_from
        if range_to is not UNSET:
            field_dict["rangeTo"] = range_to
        if currency is not UNSET:
            field_dict["currency"] = currency
        if maximal is not UNSET:
            field_dict["maximal"] = maximal

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_mode(data: object) -> EnCommissionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = EnCommissionMode(data)



                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommissionMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        def _parse_type_(data: object) -> EnCommissionVolumeType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = EnCommissionVolumeType(data)



                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnCommissionVolumeType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        def _parse_minimal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        minimal = _parse_minimal(d.pop("minimal", UNSET))


        def _parse_range_from(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_from = _parse_range_from(d.pop("rangeFrom", UNSET))


        def _parse_range_to(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_to = _parse_range_to(d.pop("rangeTo", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_maximal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        maximal = _parse_maximal(d.pop("maximal", UNSET))


        mt5_con_comm_tier = cls(
            mode=mode,
            type_=type_,
            value=value,
            minimal=minimal,
            range_from=range_from,
            range_to=range_to,
            currency=currency,
            maximal=maximal,
        )

        return mt5_con_comm_tier

