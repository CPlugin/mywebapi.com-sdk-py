from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.synchronization_mode import SynchronizationMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Sync")



@_attrs_define
class MT4Sync:
    """ v2 DTO for a single MT4 chart-history synchronization rule. Curated
    subset of the platform's ConSync — drops the Reserved padding, the
    Next pointer chain, the unused port slot, AND the `Password`
    field (replication credentials to the upstream sync source).

        Attributes:
            server (None | str | Unset): Upstream sync server address (used as cursor key)
            login (None | str | Unset): Replication login (upstream credential identifier)
            enable (int | Unset): Enable flag (0 = disabled, 1 = enabled — raw platform int)
            mode (SynchronizationMode | Unset):
            from_ (int | Unset): Sync range start (negative = whole chart)
            to (int | Unset): Sync range end (negative = whole chart)
            securities (None | str | Unset): Comma-separated list of symbols to synchronize
            time_correction (int | Unset): Time correction in minutes applied to incoming bars
     """

    server: None | str | Unset = UNSET
    login: None | str | Unset = UNSET
    enable: int | Unset = UNSET
    mode: SynchronizationMode | Unset = UNSET
    from_: int | Unset = UNSET
    to: int | Unset = UNSET
    securities: None | str | Unset = UNSET
    time_correction: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        server: None | str | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        login: None | str | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        enable = self.enable

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        from_ = self.from_

        to = self.to

        securities: None | str | Unset
        if isinstance(self.securities, Unset):
            securities = UNSET
        else:
            securities = self.securities

        time_correction = self.time_correction


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if server is not UNSET:
            field_dict["server"] = server
        if login is not UNSET:
            field_dict["login"] = login
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if securities is not UNSET:
            field_dict["securities"] = securities
        if time_correction is not UNSET:
            field_dict["timeCorrection"] = time_correction

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


        def _parse_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        enable = d.pop("enable", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: SynchronizationMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = SynchronizationMode(_mode)




        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        def _parse_securities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        securities = _parse_securities(d.pop("securities", UNSET))


        time_correction = d.pop("timeCorrection", UNSET)

        mt4_sync = cls(
            server=server,
            login=login,
            enable=enable,
            mode=mode,
            from_=from_,
            to=to,
            securities=securities,
            time_correction=time_correction,
        )

        return mt4_sync

