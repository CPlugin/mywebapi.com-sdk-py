from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_user_update import MT5UserUpdate





T = TypeVar("T", bound="MT5UserUpdateBatchItem")



@_attrs_define
class MT5UserUpdateBatchItem:
    """ One account of a batch update: the login it belongs to and the fields to change.

        Attributes:
            login (int | Unset): Login of the account to change.
            user (MT5UserUpdate | None | Unset): Fields to change on that account.
     """

    login: int | Unset = UNSET
    user: MT5UserUpdate | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_user_update import MT5UserUpdate
        login = self.login

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, MT5UserUpdate):
            user = self.user.to_dict()
        else:
            user = self.user


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_user_update import MT5UserUpdate
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_user(data: object) -> MT5UserUpdate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = MT5UserUpdate.from_dict(data)



                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5UserUpdate | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        mt5_user_update_batch_item = cls(
            login=login,
            user=user,
        )

        return mt5_user_update_batch_item

