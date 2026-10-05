from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_gateway_account_flags import EnGatewayAccountFlags
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GatewayAccount")



@_attrs_define
class MT4GatewayAccount:
    """ v2 DTO for a single MT4 STP gateway-account configuration entry.
    Curated subset of the platform's ConGatewayAccount — drops the
    23-int Reserved block AND the `Password` field (STP MT4
    credential to the external server). NotifyLogins is preserved
    as int[8] because the platform exposes a fixed-size 8-slot array.

        Attributes:
            enable (bool | Unset): Whether the gateway-account entry is active
            name (None | str | Unset): Public name of the gateway account
            id (int | Unset): Internal id (stable identifier)
            type_ (int | Unset): Gateway type (obsolete in modern MT4 builds — preserved for API completeness)
            login (int | Unset): STP MT4 login (account number on the external server)
            address (None | str | Unset): External MT4 server address (host:port string)
            notify_logins (list[int] | None | Unset): Logins of broker managers receiving internal-email gateway
                notifications (fixed-size 8 slots)
            flags (EnGatewayAccountFlags | Unset):
     """

    enable: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    id: int | Unset = UNSET
    type_: int | Unset = UNSET
    login: int | Unset = UNSET
    address: None | str | Unset = UNSET
    notify_logins: list[int] | None | Unset = UNSET
    flags: EnGatewayAccountFlags | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id = self.id

        type_ = self.type_

        login = self.login

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        notify_logins: list[int] | None | Unset
        if isinstance(self.notify_logins, Unset):
            notify_logins = UNSET
        elif isinstance(self.notify_logins, list):
            notify_logins = self.notify_logins


        else:
            notify_logins = self.notify_logins

        flags: str | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enable is not UNSET:
            field_dict["enable"] = enable
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if login is not UNSET:
            field_dict["login"] = login
        if address is not UNSET:
            field_dict["address"] = address
        if notify_logins is not UNSET:
            field_dict["notifyLogins"] = notify_logins
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        login = d.pop("login", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_notify_logins(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_logins_type_0 = cast(list[int], data)

                return notify_logins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        notify_logins = _parse_notify_logins(d.pop("notifyLogins", UNSET))


        _flags = d.pop("flags", UNSET)
        flags: EnGatewayAccountFlags | Unset
        if isinstance(_flags,  Unset):
            flags = UNSET
        else:
            flags = EnGatewayAccountFlags(_flags)




        mt4_gateway_account = cls(
            enable=enable,
            name=name,
            id=id,
            type_=type_,
            login=login,
            address=address,
            notify_logins=notify_logins,
            flags=flags,
        )

        return mt4_gateway_account

