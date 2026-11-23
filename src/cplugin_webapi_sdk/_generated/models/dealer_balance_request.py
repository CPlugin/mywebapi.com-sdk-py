from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_deal_action import EnDealAction
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DealerBalanceRequest")



@_attrs_define
class DealerBalanceRequest:
    """ 
        Attributes:
            login (int):
            value (float):
            type_ (EnDealAction | None | Unset): if none specified - it will be Balance operation. Buy/Sell actions here -
                pointless.
            comment (None | str | Unset):
     """

    login: int
    value: float
    type_: EnDealAction | None | Unset = UNSET
    comment: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        value = self.value

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, EnDealAction):
            type_ = self.type_.value
        else:
            type_ = self.type_

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "login": login,
            "value": value,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login")

        value = d.pop("value")

        def _parse_type_(data: object) -> EnDealAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = EnDealAction(data)



                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnDealAction | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        dealer_balance_request = cls(
            login=login,
            value=value,
            type_=type_,
            comment=comment,
        )

        return dealer_balance_request

