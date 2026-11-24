from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MT5SubscriptionTarget")



@_attrs_define
class MT5SubscriptionTarget:
    """ An account and a subscription configuration to act on.

        Attributes:
            login (int | Unset): Login of the account.
            subscription (int | Unset): Identifier of the subscription configuration.
     """

    login: int | Unset = UNSET
    subscription: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        subscription = self.subscription


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if subscription is not UNSET:
            field_dict["subscription"] = subscription

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        subscription = d.pop("subscription", UNSET)

        mt5_subscription_target = cls(
            login=login,
            subscription=subscription,
        )

        return mt5_subscription_target

