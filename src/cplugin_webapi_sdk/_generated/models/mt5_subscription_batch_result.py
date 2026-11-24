from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_subscription import MT5Subscription
  from ..models.mt5_subscription_history import MT5SubscriptionHistory





T = TypeVar("T", bound="MT5SubscriptionBatchResult")



@_attrs_define
class MT5SubscriptionBatchResult:
    """ The per-item outcome of a bulk subscription change.

        Attributes:
            results (list[MT5Result] | None | Unset): Result code of each requested change, in request order.
            records (list[MT5Subscription] | None | Unset): The subscription records the server produced, in request order.
            history (list[MT5SubscriptionHistory] | None | Unset): The action records the changes were written as, in
                request order.
     """

    results: list[MT5Result] | None | Unset = UNSET
    records: list[MT5Subscription] | None | Unset = UNSET
    history: list[MT5SubscriptionHistory] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_subscription import MT5Subscription
        from ..models.mt5_subscription_history import MT5SubscriptionHistory
        results: list[str] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.value
                results.append(results_type_0_item)


        else:
            results = self.results

        records: list[dict[str, Any]] | None | Unset
        if isinstance(self.records, Unset):
            records = UNSET
        elif isinstance(self.records, list):
            records = []
            for records_type_0_item_data in self.records:
                records_type_0_item = records_type_0_item_data.to_dict()
                records.append(records_type_0_item)


        else:
            records = self.records

        history: list[dict[str, Any]] | None | Unset
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, list):
            history = []
            for history_type_0_item_data in self.history:
                history_type_0_item = history_type_0_item_data.to_dict()
                history.append(history_type_0_item)


        else:
            history = self.history


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if results is not UNSET:
            field_dict["results"] = results
        if records is not UNSET:
            field_dict["records"] = records
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_subscription import MT5Subscription
        from ..models.mt5_subscription_history import MT5SubscriptionHistory
        d = dict(src_dict)
        def _parse_results(data: object) -> list[MT5Result] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in (_results_type_0):
                    results_type_0_item = MT5Result(results_type_0_item_data)



                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Result] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))


        def _parse_records(data: object) -> list[MT5Subscription] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = []
                _records_type_0 = data
                for records_type_0_item_data in (_records_type_0):
                    records_type_0_item = MT5Subscription.from_dict(records_type_0_item_data)



                    records_type_0.append(records_type_0_item)

                return records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Subscription] | None | Unset, data)

        records = _parse_records(d.pop("records", UNSET))


        def _parse_history(data: object) -> list[MT5SubscriptionHistory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_0 = []
                _history_type_0 = data
                for history_type_0_item_data in (_history_type_0):
                    history_type_0_item = MT5SubscriptionHistory.from_dict(history_type_0_item_data)



                    history_type_0.append(history_type_0_item)

                return history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5SubscriptionHistory] | None | Unset, data)

        history = _parse_history(d.pop("history", UNSET))


        mt5_subscription_batch_result = cls(
            results=results,
            records=records,
            history=history,
        )

        return mt5_subscription_batch_result

