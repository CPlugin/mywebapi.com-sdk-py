from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5UserDeleteBatchRequest")



@_attrs_define
class MT5UserDeleteBatchRequest:
    """ Request to remove several trading accounts in one call.

        Attributes:
            logins (list[int] | None | Unset): Logins of the accounts to remove.
     """

    logins: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        logins: list[int] | None | Unset
        if isinstance(self.logins, Unset):
            logins = UNSET
        elif isinstance(self.logins, list):
            logins = self.logins


        else:
            logins = self.logins


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if logins is not UNSET:
            field_dict["logins"] = logins

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_logins(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logins_type_0 = cast(list[int], data)

                return logins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        logins = _parse_logins(d.pop("logins", UNSET))


        mt5_user_delete_batch_request = cls(
            logins=logins,
        )

        return mt5_user_delete_batch_request

