from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4Performance")



@_attrs_define
class MT4Performance:
    """ v2 DTO for a single MT4 server performance snapshot — one row in the
    time-series that `PerformanceRequest` returns. Mirrors the wrapper's
    `PerformanceInfo` struct: a periodic resource sample (server-defined
    cadence, typically every 5 minutes) covering CPU, memory, network, socket
    count, and connected-user count at CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4Performance.Ctm. Used for capacity
    planning, dashboards, and incident timelines. The wrapper's private
    underscore-prefixed unix-time field is masked by CPlugin.SaaSWebApps.WebAPI.DTOs.MT4.v2.MT4Performance.Ctm.

        Attributes:
            ctm (datetime.datetime | Unset): Snapshot timestamp (wrapper internal: __time32_t)
            users (int | Unset): Connected-users count at the snapshot
            cpu (int | Unset): CPU load, percent (0..100)
            free_mem (int | Unset): Free memory at the snapshot, in kilobytes
            network (int | Unset): Network throughput at the snapshot, in kilobytes per second
            sockets (int | Unset): Open-sockets count at the snapshot
     """

    ctm: datetime.datetime | Unset = UNSET
    users: int | Unset = UNSET
    cpu: int | Unset = UNSET
    free_mem: int | Unset = UNSET
    network: int | Unset = UNSET
    sockets: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ctm: str | Unset = UNSET
        if not isinstance(self.ctm, Unset):
            ctm = self.ctm.isoformat()

        users = self.users

        cpu = self.cpu

        free_mem = self.free_mem

        network = self.network

        sockets = self.sockets


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ctm is not UNSET:
            field_dict["ctm"] = ctm
        if users is not UNSET:
            field_dict["users"] = users
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if free_mem is not UNSET:
            field_dict["freeMem"] = free_mem
        if network is not UNSET:
            field_dict["network"] = network
        if sockets is not UNSET:
            field_dict["sockets"] = sockets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _ctm = d.pop("ctm", UNSET)
        ctm: datetime.datetime | Unset
        if isinstance(_ctm,  Unset):
            ctm = UNSET
        else:
            ctm = datetime.datetime.fromisoformat(_ctm)




        users = d.pop("users", UNSET)

        cpu = d.pop("cpu", UNSET)

        free_mem = d.pop("freeMem", UNSET)

        network = d.pop("network", UNSET)

        sockets = d.pop("sockets", UNSET)

        mt4_performance = cls(
            ctm=ctm,
            users=users,
            cpu=cpu,
            free_mem=free_mem,
            network=network,
            sockets=sockets,
        )

        return mt4_performance

