from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_user import MT5User





T = TypeVar("T", bound="MT5UserAddResult")



@_attrs_define
class MT5UserAddResult:
    """ The created account and the passwords it was created with.

        Attributes:
            user (MT5User | None | Unset): The account as the trade server stored it, including the allocated login.
            password (None | str | Unset): The master password the account was created with.
            password_investor (None | str | Unset): The investor (read-only) password the account was created with.
     """

    user: MT5User | None | Unset = UNSET
    password: None | str | Unset = UNSET
    password_investor: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_user import MT5User
        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, MT5User):
            user = self.user.to_dict()
        else:
            user = self.user

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        password_investor: None | str | Unset
        if isinstance(self.password_investor, Unset):
            password_investor = UNSET
        else:
            password_investor = self.password_investor


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if password_investor is not UNSET:
            field_dict["passwordInvestor"] = password_investor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_user import MT5User
        d = dict(src_dict)
        def _parse_user(data: object) -> MT5User | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = MT5User.from_dict(data)



                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5User | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        def _parse_password_investor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password_investor = _parse_password_investor(d.pop("passwordInvestor", UNSET))


        mt5_user_add_result = cls(
            user=user,
            password=password,
            password_investor=password_investor,
        )

        return mt5_user_add_result

