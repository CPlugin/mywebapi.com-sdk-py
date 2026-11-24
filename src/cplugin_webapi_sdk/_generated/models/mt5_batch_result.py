from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5BatchResult")



@_attrs_define
class MT5BatchResult:
    """ Outcome of one entry of a batch operation. The entries are returned in the order of the request.

        Attributes:
            id (int | None | Unset): Identifier the entry was addressed to or created for: the record identifier on the
                document,
                comment and attachment routes, and the account login on the account-binding routes.
            result (MT5Result | Unset):
     """

    id: int | None | Unset = UNSET
    result: MT5Result | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _result = d.pop("result", UNSET)
        result: MT5Result | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = MT5Result(_result)




        mt5_batch_result = cls(
            id=id,
            result=result,
        )

        return mt5_batch_result

