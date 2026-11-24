from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_user_update_batch_item import MT5UserUpdateBatchItem





T = TypeVar("T", bound="MT5UserUpdateBatchRequest")



@_attrs_define
class MT5UserUpdateBatchRequest:
    """ Request to change several trading accounts in one call.

        Attributes:
            users (list[MT5UserUpdateBatchItem] | None | Unset): Accounts to change; each is applied on its own and reported
                on its own.
     """

    users: list[MT5UserUpdateBatchItem] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_user_update_batch_item import MT5UserUpdateBatchItem
        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)


        else:
            users = self.users


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_user_update_batch_item import MT5UserUpdateBatchItem
        d = dict(src_dict)
        def _parse_users(data: object) -> list[MT5UserUpdateBatchItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in (_users_type_0):
                    users_type_0_item = MT5UserUpdateBatchItem.from_dict(users_type_0_item_data)



                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5UserUpdateBatchItem] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))


        mt5_user_update_batch_request = cls(
            users=users,
        )

        return mt5_user_update_batch_request

