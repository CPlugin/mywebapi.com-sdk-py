from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_geo_record import MT5GeoRecord





T = TypeVar("T", bound="MT5GeoResolveResult")



@_attrs_define
class MT5GeoResolveResult:
    """ Outcome of resolving one address of a batch.

        Attributes:
            address (None | str | Unset): The address as it was submitted.
            result (MT5Result | Unset):
            record (MT5GeoRecord | None | Unset): Description of the address; absent when the address was not resolved.
     """

    address: None | str | Unset = UNSET
    result: MT5Result | Unset = UNSET
    record: MT5GeoRecord | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_geo_record import MT5GeoRecord
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value


        record: dict[str, Any] | None | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        elif isinstance(self.record, MT5GeoRecord):
            record = self.record.to_dict()
        else:
            record = self.record


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if result is not UNSET:
            field_dict["result"] = result
        if record is not UNSET:
            field_dict["record"] = record

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_geo_record import MT5GeoRecord
        d = dict(src_dict)
        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        _result = d.pop("result", UNSET)
        result: MT5Result | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = MT5Result(_result)




        def _parse_record(data: object) -> MT5GeoRecord | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_1 = MT5GeoRecord.from_dict(data)



                return record_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5GeoRecord | None | Unset, data)

        record = _parse_record(d.pop("record", UNSET))


        mt5_geo_resolve_result = cls(
            address=address,
            result=result,
            record=record,
        )

        return mt5_geo_resolve_result

