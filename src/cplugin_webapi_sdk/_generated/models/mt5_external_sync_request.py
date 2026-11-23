from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5ExternalSyncRequest")



@_attrs_define
class MT5ExternalSyncRequest:
    """ Request to synchronize an account with an external trading system through a gateway.

        Attributes:
            gateway_id (int | Unset): Identifier of the gateway configuration.
            account (None | str | Unset): Account number in the external trading system.
            sync_mode (None | str | Unset): Part of the trading state to synchronize.<br/>One of: All, Balance, Positions,
                Orders. Case-insensitive; the numeric value is accepted too. Any other value is refused with error code
                Validation.
     """

    gateway_id: int | Unset = UNSET
    account: None | str | Unset = UNSET
    sync_mode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        gateway_id = self.gateway_id

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        sync_mode: None | str | Unset
        if isinstance(self.sync_mode, Unset):
            sync_mode = UNSET
        else:
            sync_mode = self.sync_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if gateway_id is not UNSET:
            field_dict["gatewayId"] = gateway_id
        if account is not UNSET:
            field_dict["account"] = account
        if sync_mode is not UNSET:
            field_dict["syncMode"] = sync_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway_id = d.pop("gatewayId", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))


        def _parse_sync_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_mode = _parse_sync_mode(d.pop("syncMode", UNSET))


        mt5_external_sync_request = cls(
            gateway_id=gateway_id,
            account=account,
            sync_mode=sync_mode,
        )

        return mt5_external_sync_request

