from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5ProxySettings")



@_attrs_define
class MT5ProxySettings:
    """ Proxy server through which the manager connection to the trade server is established.

        Attributes:
            enabled (bool | Unset): Whether the connection goes through a proxy server.
            type_ (None | str | Unset): Proxy protocol name.<br/>One of: Socks4, Socks5, Http. Case-insensitive; the numeric
                value is accepted too. Any other value is refused with error code Validation.
            address (None | str | Unset): Address of the proxy server, up to 64 characters.
            auth (None | str | Unset): Authentication string of the proxy server, up to 64 characters.
     """

    enabled: bool | Unset = UNSET
    type_: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    auth: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        auth: None | str | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        else:
            auth = self.auth


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if type_ is not UNSET:
            field_dict["type"] = type_
        if address is not UNSET:
            field_dict["address"] = address
        if auth is not UNSET:
            field_dict["auth"] = auth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_auth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth = _parse_auth(d.pop("auth", UNSET))


        mt5_proxy_settings = cls(
            enabled=enabled,
            type_=type_,
            address=address,
            auth=auth,
        )

        return mt5_proxy_settings

