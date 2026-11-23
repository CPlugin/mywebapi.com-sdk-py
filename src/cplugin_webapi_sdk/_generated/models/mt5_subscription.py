from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_subscription_status import MT5SubscriptionStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5Subscription")



@_attrs_define
class MT5Subscription:
    """ A subscription of a trading account, as stored by the trade server.

        Attributes:
            id (int | None | Unset): Identifier of the subscription record. Required when an existing record is updated.
            login (int | None | Unset): Login of the account the subscription belongs to.
            subscription (int | None | Unset): Identifier of the subscription configuration the account is subscribed to.
            status (MT5SubscriptionStatus | None | Unset): Subscription state.<br/>One of: Active, Suspended, Canceled.
                Case-insensitive; the numeric value is accepted too. Any other value is refused with error code Validation.
            flags (None | str | Unset): Additional subscription property flags.
            time_subscribe (int | None | Unset): Start of the subscription, in seconds since 1970-01-01.
            time_renewal (int | None | Unset): Time of the last subscription renewal, in seconds since 1970-01-01.
            time_expire (int | None | Unset): End of the subscription, in seconds since 1970-01-01.
     """

    id: int | None | Unset = UNSET
    login: int | None | Unset = UNSET
    subscription: int | None | Unset = UNSET
    status: MT5SubscriptionStatus | None | Unset = UNSET
    flags: None | str | Unset = UNSET
    time_subscribe: int | None | Unset = UNSET
    time_renewal: int | None | Unset = UNSET
    time_expire: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        login: int | None | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        subscription: int | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        else:
            subscription = self.subscription

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, MT5SubscriptionStatus):
            status = self.status.value
        else:
            status = self.status

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        time_subscribe: int | None | Unset
        if isinstance(self.time_subscribe, Unset):
            time_subscribe = UNSET
        else:
            time_subscribe = self.time_subscribe

        time_renewal: int | None | Unset
        if isinstance(self.time_renewal, Unset):
            time_renewal = UNSET
        else:
            time_renewal = self.time_renewal

        time_expire: int | None | Unset
        if isinstance(self.time_expire, Unset):
            time_expire = UNSET
        else:
            time_expire = self.time_expire


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if login is not UNSET:
            field_dict["login"] = login
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if status is not UNSET:
            field_dict["status"] = status
        if flags is not UNSET:
            field_dict["flags"] = flags
        if time_subscribe is not UNSET:
            field_dict["timeSubscribe"] = time_subscribe
        if time_renewal is not UNSET:
            field_dict["timeRenewal"] = time_renewal
        if time_expire is not UNSET:
            field_dict["timeExpire"] = time_expire

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


        def _parse_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_subscription(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))


        def _parse_status(data: object) -> MT5SubscriptionStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = MT5SubscriptionStatus(data)



                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SubscriptionStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_time_subscribe(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_subscribe = _parse_time_subscribe(d.pop("timeSubscribe", UNSET))


        def _parse_time_renewal(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_renewal = _parse_time_renewal(d.pop("timeRenewal", UNSET))


        def _parse_time_expire(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_expire = _parse_time_expire(d.pop("timeExpire", UNSET))


        mt5_subscription = cls(
            id=id,
            login=login,
            subscription=subscription,
            status=status,
            flags=flags,
            time_subscribe=time_subscribe,
            time_renewal=time_renewal,
            time_expire=time_expire,
        )

        return mt5_subscription

