from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_subscription_action import MT5SubscriptionAction
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5SubscriptionHistory")



@_attrs_define
class MT5SubscriptionHistory:
    """ An action performed with a subscription of a trading account.

        Attributes:
            id (int | None | Unset): Identifier of the action record. Required when an existing action is updated.
            login (int | None | Unset): Login of the account the subscription belongs to.
            subscription (int | None | Unset): Identifier of the subscription configuration the action was performed with.
            record (int | None | Unset): Identifier of the subscription record the action was performed on.
            action (MT5SubscriptionAction | None | Unset): Action performed with the subscription.<br/>One of: Subscribe,
                Renewal, Suspend, Cancel, Deleted. Case-insensitive; the numeric value is accepted too. Any other value is
                refused with error code Validation.
            time (int | None | Unset): Time of the action, in seconds since 1970-01-01.
            amount (float | None | Unset): Amount charged or returned by the action.
            amount_digits (int | None | Unset): Number of decimal places in `amount`.
            amount_deal (int | None | Unset): Ticket of the balance deal through which the payment was made; zero when there
                was no payment.
     """

    id: int | None | Unset = UNSET
    login: int | None | Unset = UNSET
    subscription: int | None | Unset = UNSET
    record: int | None | Unset = UNSET
    action: MT5SubscriptionAction | None | Unset = UNSET
    time: int | None | Unset = UNSET
    amount: float | None | Unset = UNSET
    amount_digits: int | None | Unset = UNSET
    amount_deal: int | None | Unset = UNSET





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

        record: int | None | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        else:
            record = self.record

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, MT5SubscriptionAction):
            action = self.action.value
        else:
            action = self.action

        time: int | None | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        amount_digits: int | None | Unset
        if isinstance(self.amount_digits, Unset):
            amount_digits = UNSET
        else:
            amount_digits = self.amount_digits

        amount_deal: int | None | Unset
        if isinstance(self.amount_deal, Unset):
            amount_deal = UNSET
        else:
            amount_deal = self.amount_deal


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if login is not UNSET:
            field_dict["login"] = login
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if record is not UNSET:
            field_dict["record"] = record
        if action is not UNSET:
            field_dict["action"] = action
        if time is not UNSET:
            field_dict["time"] = time
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_digits is not UNSET:
            field_dict["amountDigits"] = amount_digits
        if amount_deal is not UNSET:
            field_dict["amountDeal"] = amount_deal

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


        def _parse_record(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record = _parse_record(d.pop("record", UNSET))


        def _parse_action(data: object) -> MT5SubscriptionAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = MT5SubscriptionAction(data)



                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SubscriptionAction | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_amount_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        amount_digits = _parse_amount_digits(d.pop("amountDigits", UNSET))


        def _parse_amount_deal(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        amount_deal = _parse_amount_deal(d.pop("amountDeal", UNSET))


        mt5_subscription_history = cls(
            id=id,
            login=login,
            subscription=subscription,
            record=record,
            action=action,
            time=time,
            amount=amount,
            amount_digits=amount_digits,
            amount_deal=amount_deal,
        )

        return mt5_subscription_history

