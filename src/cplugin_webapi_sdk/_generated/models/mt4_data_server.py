from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4DataServer")



@_attrs_define
class MT4DataServer:
    """ v2 DTO for a single MT4 access-server (DataServer) configuration entry.
    Curated subset of the wrapper's ConDataServer — drops the internal
    Reserved1/Reserved2 padding and the Next pointer chain. Loading and
    IpInternal are widened from uint to long for JSON-safe numeric
    serialization.

        Attributes:
            server (None | str | Unset): Server address as "host:port" or "host"
            ip (int | Unset): Server IP (raw wrapper int — sign-preserved; high-bit IPs may serialize as negative)
            description (None | str | Unset): Free-form server description
            is_proxy (int | Unset): Whether the server can act as a proxy (0/1; raw wrapper int preserved)
            priority (int | Unset): Connection priority: 0-7 base, 255 = idle
            loading (int | Unset): Reported server load (UINT_MAX = no information reported)
            ip_internal (int | Unset): Internal IP address (widened uint → long)
            is_witness (int | Unset): Failover-witness flag (0 / 1)
     """

    server: None | str | Unset = UNSET
    ip: int | Unset = UNSET
    description: None | str | Unset = UNSET
    is_proxy: int | Unset = UNSET
    priority: int | Unset = UNSET
    loading: int | Unset = UNSET
    ip_internal: int | Unset = UNSET
    is_witness: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        server: None | str | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        ip = self.ip

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_proxy = self.is_proxy

        priority = self.priority

        loading = self.loading

        ip_internal = self.ip_internal

        is_witness = self.is_witness


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if server is not UNSET:
            field_dict["server"] = server
        if ip is not UNSET:
            field_dict["ip"] = ip
        if description is not UNSET:
            field_dict["description"] = description
        if is_proxy is not UNSET:
            field_dict["isProxy"] = is_proxy
        if priority is not UNSET:
            field_dict["priority"] = priority
        if loading is not UNSET:
            field_dict["loading"] = loading
        if ip_internal is not UNSET:
            field_dict["ipInternal"] = ip_internal
        if is_witness is not UNSET:
            field_dict["isWitness"] = is_witness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server = _parse_server(d.pop("server", UNSET))


        ip = d.pop("ip", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        is_proxy = d.pop("isProxy", UNSET)

        priority = d.pop("priority", UNSET)

        loading = d.pop("loading", UNSET)

        ip_internal = d.pop("ipInternal", UNSET)

        is_witness = d.pop("isWitness", UNSET)

        mt4_data_server = cls(
            server=server,
            ip=ip,
            description=description,
            is_proxy=is_proxy,
            priority=priority,
            loading=loading,
            ip_internal=ip_internal,
            is_witness=is_witness,
        )

        return mt4_data_server

