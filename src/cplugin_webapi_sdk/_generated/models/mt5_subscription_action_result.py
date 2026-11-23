from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_subscription import MT5Subscription
  from ..models.mt5_subscription_history import MT5SubscriptionHistory





T = TypeVar("T", bound="MT5SubscriptionActionResult")



@_attrs_define
class MT5SubscriptionActionResult:
    """ The subscription record and the action record produced by one subscription change.

        Attributes:
            record (MT5Subscription | None | Unset): The subscription record as the trade server stored it.
            history (MT5SubscriptionHistory | None | Unset): The action record the change was written as.
     """

    record: MT5Subscription | None | Unset = UNSET
    history: MT5SubscriptionHistory | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_subscription import MT5Subscription
        from ..models.mt5_subscription_history import MT5SubscriptionHistory
        record: dict[str, Any] | None | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        elif isinstance(self.record, MT5Subscription):
            record = self.record.to_dict()
        else:
            record = self.record

        history: dict[str, Any] | None | Unset
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, MT5SubscriptionHistory):
            history = self.history.to_dict()
        else:
            history = self.history


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if record is not UNSET:
            field_dict["record"] = record
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_subscription import MT5Subscription
        from ..models.mt5_subscription_history import MT5SubscriptionHistory
        d = dict(src_dict)
        def _parse_record(data: object) -> MT5Subscription | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_1 = MT5Subscription.from_dict(data)



                return record_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5Subscription | None | Unset, data)

        record = _parse_record(d.pop("record", UNSET))


        def _parse_history(data: object) -> MT5SubscriptionHistory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_type_1 = MT5SubscriptionHistory.from_dict(data)



                return history_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SubscriptionHistory | None | Unset, data)

        history = _parse_history(d.pop("history", UNSET))


        mt5_subscription_action_result = cls(
            record=record,
            history=history,
        )

        return mt5_subscription_action_result

