from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4ExposureValue")



@_attrs_define
class MT4ExposureValue:
    """ Broker exposure in one currency — the platform's `ExposureValue`
    record. Both volumes are expressed in the base currency of the pair
    that produced them, converted to the record's currency.

        Attributes:
            currency (None | str | Unset): Currency code the exposure is reported in (e.g. USD)
            clients (float | Unset): Net client volume held by the broker in this currency
            coverage (float | Unset): Net coverage volume the broker carries in this currency
     """

    currency: None | str | Unset = UNSET
    clients: float | Unset = UNSET
    coverage: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        clients = self.clients

        coverage = self.coverage


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if clients is not UNSET:
            field_dict["clients"] = clients
        if coverage is not UNSET:
            field_dict["coverage"] = coverage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        clients = d.pop("clients", UNSET)

        coverage = d.pop("coverage", UNSET)

        mt4_exposure_value = cls(
            currency=currency,
            clients=clients,
            coverage=coverage,
        )

        return mt4_exposure_value

