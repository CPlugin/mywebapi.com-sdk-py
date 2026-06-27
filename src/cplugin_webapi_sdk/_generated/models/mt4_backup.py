from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arc_backup_execution_period import ArcBackupExecutionPeriod
from ..models.arc_backup_store_period import ArcBackupStorePeriod
from ..models.backup_execution_period import BackupExecutionPeriod
from ..models.backup_store_period import BackupStorePeriod
from ..models.export_execution_period import ExportExecutionPeriod
from ..models.server_role import ServerRole
from ..models.watchdog_failover_mode import WatchdogFailoverMode
from ..models.watchdog_state import WatchdogState
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4Backup")



@_attrs_define
class MT4Backup:
    """ v2 DTO for the MT4 server's backup configuration (wrapper's ConBackup).
    Curated subset — drops the WatchPassword field (slave-server credential)
    for security. All other wrapper public fields are preserved, enums are
    surfaced as enum types (V2JsonContext serializes them as strings via
    UseStringEnumConverter=true).

        Attributes:
            full_backup_path (None | str | Unset): Filesystem path where full backups are written
            full_backup_period (BackupExecutionPeriod | Unset):
            full_backup_store (BackupStorePeriod | Unset):
            full_backup_shift (int | Unset): Full backup time-shift in minutes
            full_backup_last_time (datetime.datetime | Unset): Last full backup completion timestamp (UTC)
            external_path (None | str | Unset): Path to external processing directory
            archive_period (ArcBackupExecutionPeriod | Unset):
            archive_store (ArcBackupStorePeriod | Unset):
            archive_shift (int | Unset): Archive backup time-shift in minutes
            archive_last_time (datetime.datetime | Unset): Last archive backup completion timestamp (UTC)
            export_securities (None | str | Unset): Comma-separated list of exported securities
            export_path (None | str | Unset): Path to export script
            export_period (ExportExecutionPeriod | Unset):
            export_last_time (datetime.datetime | Unset): Last export completion timestamp (UTC)
            watch_role (ServerRole | Unset):
            watch_opposite (None | str | Unset): Opposite server's IP:port string (not secret)
            watch_ip (int | Unset): Watchdog IP (32-bit, raw wrapper representation)
            watch_state (WatchdogState | Unset):
            watch_failover (WatchdogFailoverMode | Unset):
            watch_timeout (int | Unset): Watchdog response timeout, seconds
            watch_login (int | Unset): Watchdog login
            watch_timestamp (int | Unset): Watchdog last-seen timestamp (raw int — wrapper does not auto-convert)
     """

    full_backup_path: None | str | Unset = UNSET
    full_backup_period: BackupExecutionPeriod | Unset = UNSET
    full_backup_store: BackupStorePeriod | Unset = UNSET
    full_backup_shift: int | Unset = UNSET
    full_backup_last_time: datetime.datetime | Unset = UNSET
    external_path: None | str | Unset = UNSET
    archive_period: ArcBackupExecutionPeriod | Unset = UNSET
    archive_store: ArcBackupStorePeriod | Unset = UNSET
    archive_shift: int | Unset = UNSET
    archive_last_time: datetime.datetime | Unset = UNSET
    export_securities: None | str | Unset = UNSET
    export_path: None | str | Unset = UNSET
    export_period: ExportExecutionPeriod | Unset = UNSET
    export_last_time: datetime.datetime | Unset = UNSET
    watch_role: ServerRole | Unset = UNSET
    watch_opposite: None | str | Unset = UNSET
    watch_ip: int | Unset = UNSET
    watch_state: WatchdogState | Unset = UNSET
    watch_failover: WatchdogFailoverMode | Unset = UNSET
    watch_timeout: int | Unset = UNSET
    watch_login: int | Unset = UNSET
    watch_timestamp: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        full_backup_path: None | str | Unset
        if isinstance(self.full_backup_path, Unset):
            full_backup_path = UNSET
        else:
            full_backup_path = self.full_backup_path

        full_backup_period: str | Unset = UNSET
        if not isinstance(self.full_backup_period, Unset):
            full_backup_period = self.full_backup_period.value


        full_backup_store: str | Unset = UNSET
        if not isinstance(self.full_backup_store, Unset):
            full_backup_store = self.full_backup_store.value


        full_backup_shift = self.full_backup_shift

        full_backup_last_time: str | Unset = UNSET
        if not isinstance(self.full_backup_last_time, Unset):
            full_backup_last_time = self.full_backup_last_time.isoformat()

        external_path: None | str | Unset
        if isinstance(self.external_path, Unset):
            external_path = UNSET
        else:
            external_path = self.external_path

        archive_period: str | Unset = UNSET
        if not isinstance(self.archive_period, Unset):
            archive_period = self.archive_period.value


        archive_store: str | Unset = UNSET
        if not isinstance(self.archive_store, Unset):
            archive_store = self.archive_store.value


        archive_shift = self.archive_shift

        archive_last_time: str | Unset = UNSET
        if not isinstance(self.archive_last_time, Unset):
            archive_last_time = self.archive_last_time.isoformat()

        export_securities: None | str | Unset
        if isinstance(self.export_securities, Unset):
            export_securities = UNSET
        else:
            export_securities = self.export_securities

        export_path: None | str | Unset
        if isinstance(self.export_path, Unset):
            export_path = UNSET
        else:
            export_path = self.export_path

        export_period: str | Unset = UNSET
        if not isinstance(self.export_period, Unset):
            export_period = self.export_period.value


        export_last_time: str | Unset = UNSET
        if not isinstance(self.export_last_time, Unset):
            export_last_time = self.export_last_time.isoformat()

        watch_role: str | Unset = UNSET
        if not isinstance(self.watch_role, Unset):
            watch_role = self.watch_role.value


        watch_opposite: None | str | Unset
        if isinstance(self.watch_opposite, Unset):
            watch_opposite = UNSET
        else:
            watch_opposite = self.watch_opposite

        watch_ip = self.watch_ip

        watch_state: str | Unset = UNSET
        if not isinstance(self.watch_state, Unset):
            watch_state = self.watch_state.value


        watch_failover: str | Unset = UNSET
        if not isinstance(self.watch_failover, Unset):
            watch_failover = self.watch_failover.value


        watch_timeout = self.watch_timeout

        watch_login = self.watch_login

        watch_timestamp = self.watch_timestamp


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if full_backup_path is not UNSET:
            field_dict["fullBackupPath"] = full_backup_path
        if full_backup_period is not UNSET:
            field_dict["fullBackupPeriod"] = full_backup_period
        if full_backup_store is not UNSET:
            field_dict["fullBackupStore"] = full_backup_store
        if full_backup_shift is not UNSET:
            field_dict["fullBackupShift"] = full_backup_shift
        if full_backup_last_time is not UNSET:
            field_dict["fullBackupLastTime"] = full_backup_last_time
        if external_path is not UNSET:
            field_dict["externalPath"] = external_path
        if archive_period is not UNSET:
            field_dict["archivePeriod"] = archive_period
        if archive_store is not UNSET:
            field_dict["archiveStore"] = archive_store
        if archive_shift is not UNSET:
            field_dict["archiveShift"] = archive_shift
        if archive_last_time is not UNSET:
            field_dict["archiveLastTime"] = archive_last_time
        if export_securities is not UNSET:
            field_dict["exportSecurities"] = export_securities
        if export_path is not UNSET:
            field_dict["exportPath"] = export_path
        if export_period is not UNSET:
            field_dict["exportPeriod"] = export_period
        if export_last_time is not UNSET:
            field_dict["exportLastTime"] = export_last_time
        if watch_role is not UNSET:
            field_dict["watchRole"] = watch_role
        if watch_opposite is not UNSET:
            field_dict["watchOpposite"] = watch_opposite
        if watch_ip is not UNSET:
            field_dict["watchIp"] = watch_ip
        if watch_state is not UNSET:
            field_dict["watchState"] = watch_state
        if watch_failover is not UNSET:
            field_dict["watchFailover"] = watch_failover
        if watch_timeout is not UNSET:
            field_dict["watchTimeout"] = watch_timeout
        if watch_login is not UNSET:
            field_dict["watchLogin"] = watch_login
        if watch_timestamp is not UNSET:
            field_dict["watchTimestamp"] = watch_timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_full_backup_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_backup_path = _parse_full_backup_path(d.pop("fullBackupPath", UNSET))


        _full_backup_period = d.pop("fullBackupPeriod", UNSET)
        full_backup_period: BackupExecutionPeriod | Unset
        if isinstance(_full_backup_period,  Unset):
            full_backup_period = UNSET
        else:
            full_backup_period = BackupExecutionPeriod(_full_backup_period)




        _full_backup_store = d.pop("fullBackupStore", UNSET)
        full_backup_store: BackupStorePeriod | Unset
        if isinstance(_full_backup_store,  Unset):
            full_backup_store = UNSET
        else:
            full_backup_store = BackupStorePeriod(_full_backup_store)




        full_backup_shift = d.pop("fullBackupShift", UNSET)

        _full_backup_last_time = d.pop("fullBackupLastTime", UNSET)
        full_backup_last_time: datetime.datetime | Unset
        if isinstance(_full_backup_last_time,  Unset):
            full_backup_last_time = UNSET
        else:
            full_backup_last_time = datetime.datetime.fromisoformat(_full_backup_last_time)




        def _parse_external_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_path = _parse_external_path(d.pop("externalPath", UNSET))


        _archive_period = d.pop("archivePeriod", UNSET)
        archive_period: ArcBackupExecutionPeriod | Unset
        if isinstance(_archive_period,  Unset):
            archive_period = UNSET
        else:
            archive_period = ArcBackupExecutionPeriod(_archive_period)




        _archive_store = d.pop("archiveStore", UNSET)
        archive_store: ArcBackupStorePeriod | Unset
        if isinstance(_archive_store,  Unset):
            archive_store = UNSET
        else:
            archive_store = ArcBackupStorePeriod(_archive_store)




        archive_shift = d.pop("archiveShift", UNSET)

        _archive_last_time = d.pop("archiveLastTime", UNSET)
        archive_last_time: datetime.datetime | Unset
        if isinstance(_archive_last_time,  Unset):
            archive_last_time = UNSET
        else:
            archive_last_time = datetime.datetime.fromisoformat(_archive_last_time)




        def _parse_export_securities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_securities = _parse_export_securities(d.pop("exportSecurities", UNSET))


        def _parse_export_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_path = _parse_export_path(d.pop("exportPath", UNSET))


        _export_period = d.pop("exportPeriod", UNSET)
        export_period: ExportExecutionPeriod | Unset
        if isinstance(_export_period,  Unset):
            export_period = UNSET
        else:
            export_period = ExportExecutionPeriod(_export_period)




        _export_last_time = d.pop("exportLastTime", UNSET)
        export_last_time: datetime.datetime | Unset
        if isinstance(_export_last_time,  Unset):
            export_last_time = UNSET
        else:
            export_last_time = datetime.datetime.fromisoformat(_export_last_time)




        _watch_role = d.pop("watchRole", UNSET)
        watch_role: ServerRole | Unset
        if isinstance(_watch_role,  Unset):
            watch_role = UNSET
        else:
            watch_role = ServerRole(_watch_role)




        def _parse_watch_opposite(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        watch_opposite = _parse_watch_opposite(d.pop("watchOpposite", UNSET))


        watch_ip = d.pop("watchIp", UNSET)

        _watch_state = d.pop("watchState", UNSET)
        watch_state: WatchdogState | Unset
        if isinstance(_watch_state,  Unset):
            watch_state = UNSET
        else:
            watch_state = WatchdogState(_watch_state)




        _watch_failover = d.pop("watchFailover", UNSET)
        watch_failover: WatchdogFailoverMode | Unset
        if isinstance(_watch_failover,  Unset):
            watch_failover = UNSET
        else:
            watch_failover = WatchdogFailoverMode(_watch_failover)




        watch_timeout = d.pop("watchTimeout", UNSET)

        watch_login = d.pop("watchLogin", UNSET)

        watch_timestamp = d.pop("watchTimestamp", UNSET)

        mt4_backup = cls(
            full_backup_path=full_backup_path,
            full_backup_period=full_backup_period,
            full_backup_store=full_backup_store,
            full_backup_shift=full_backup_shift,
            full_backup_last_time=full_backup_last_time,
            external_path=external_path,
            archive_period=archive_period,
            archive_store=archive_store,
            archive_shift=archive_shift,
            archive_last_time=archive_last_time,
            export_securities=export_securities,
            export_path=export_path,
            export_period=export_period,
            export_last_time=export_last_time,
            watch_role=watch_role,
            watch_opposite=watch_opposite,
            watch_ip=watch_ip,
            watch_state=watch_state,
            watch_failover=watch_failover,
            watch_timeout=watch_timeout,
            watch_login=watch_login,
            watch_timestamp=watch_timestamp,
        )

        return mt4_backup

