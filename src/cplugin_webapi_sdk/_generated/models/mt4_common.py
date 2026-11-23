from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.demo_account_type import DemoAccountType
from ..models.live_update_mode import LiveUpdateMode
from ..models.monthly_statement_mode import MonthlyStatementMode
from ..models.rollover_mode import RolloverMode
from ..models.server_stop_reason import ServerStopReason
from ..models.statement_mode import StatementMode
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT4Common")



@_attrs_define
class MT4Common:
    """ Full server-wide common configuration of an MT4 trade server: identity,
    protocol version, bind and web address lists, storage paths, runtime
    counters and the operational subsystems (demo accounts, rollover,
    statements, live update).

        Attributes:
            owner (None | str | Unset): Broker / company display name
            name (None | str | Unset): Trade server name
            address (int | Unset): IP address assigned to the server
            port (int | Unset): Server port
            timeout (int | Unset): Socket timeout, seconds
            demo_account_type (DemoAccountType | Unset):
            time_of_demo (int | Unset): Demo-account lifetime, days
            daylight_correction (int | Unset): Daylight-correction setting
            time_zone_real (int | Unset): Server time zone offset from UTC, in hours (DST-adjusted)
            time_zone (int | Unset): Server time zone offset from UTC, in hours
            time_sync (None | str | Unset): Time-synchronization server address
            min_client (int | Unset): Minimal authorized client version
            min_api (int | Unset): Minimal authorized API version
            feeder_timeout (int | Unset): Data-feed switch timeout, seconds
            keep_emails (int | Unset): Internal mail keep period
            end_hour (int | Unset): End-of-day time: hour
            end_minute (int | Unset): End-of-day time: minute
            optimization_time (int | Unset): Optimization start time, minutes
            optimization_last_time (int | Unset): Optimization last run time
            optimization_counter (int | Unset): Optimization run counter
            optimization_unused (list[int] | None | Unset): Reserved for future use
            anti_flood (int | Unset): Anti-flood control enabled flag
            flood_control (int | Unset): Maximum anti-flood connections
            live_update_mode (LiveUpdateMode | Unset):
            last_order (int | Unset): Last assigned order ticket (read only)
            last_login (int | Unset): Last assigned account login (read only)
            lost_login (int | Unset): Lost-commission account login (read only)
            rollover_mode (RolloverMode | Unset):
            path_database (None | str | Unset): Path to the databases
            path_history (None | str | Unset): Path to the history bases
            path_log (None | str | Unset): Path to the logs
            overnight_last_day (int | Unset): Day of the last overnight
            overnight_last_time (int | Unset): Time of the last overnight
            overnight_prev_time (int | Unset): Time of the overnight before the last one
            overmonth_last_month (int | Unset): Month of the last generated report
            adapters (None | str | Unset): Network adapters list (read only)
            bind_adresses (list[int] | None | Unset): Available bind addresses
            server_version (int | Unset): Server version
            server_build (int | Unset): Server build number
            web_adresses (list[int] | None | Unset): Web services access list (comma separated IP addresses)
            statement_mode (StatementMode | Unset):
            monthly_statement_mode (MonthlyStatementMode | Unset):
            keep_ticks (int | Unset): Tick history keep period, days
            statement_weekend (int | Unset): Generate statements at weekends
            reserved (list[int] | None | Unset): Reserved for future use
            last_activate (datetime.datetime | Unset): Last activation date and time
            stop_last (datetime.datetime | Unset): Last stop date and time
            stop_delay (int | Unset): Last stop delay
            stop_reason (ServerStopReason | Unset):
            account_url (None | str | Unset): Account allocation URL
     """

    owner: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    address: int | Unset = UNSET
    port: int | Unset = UNSET
    timeout: int | Unset = UNSET
    demo_account_type: DemoAccountType | Unset = UNSET
    time_of_demo: int | Unset = UNSET
    daylight_correction: int | Unset = UNSET
    time_zone_real: int | Unset = UNSET
    time_zone: int | Unset = UNSET
    time_sync: None | str | Unset = UNSET
    min_client: int | Unset = UNSET
    min_api: int | Unset = UNSET
    feeder_timeout: int | Unset = UNSET
    keep_emails: int | Unset = UNSET
    end_hour: int | Unset = UNSET
    end_minute: int | Unset = UNSET
    optimization_time: int | Unset = UNSET
    optimization_last_time: int | Unset = UNSET
    optimization_counter: int | Unset = UNSET
    optimization_unused: list[int] | None | Unset = UNSET
    anti_flood: int | Unset = UNSET
    flood_control: int | Unset = UNSET
    live_update_mode: LiveUpdateMode | Unset = UNSET
    last_order: int | Unset = UNSET
    last_login: int | Unset = UNSET
    lost_login: int | Unset = UNSET
    rollover_mode: RolloverMode | Unset = UNSET
    path_database: None | str | Unset = UNSET
    path_history: None | str | Unset = UNSET
    path_log: None | str | Unset = UNSET
    overnight_last_day: int | Unset = UNSET
    overnight_last_time: int | Unset = UNSET
    overnight_prev_time: int | Unset = UNSET
    overmonth_last_month: int | Unset = UNSET
    adapters: None | str | Unset = UNSET
    bind_adresses: list[int] | None | Unset = UNSET
    server_version: int | Unset = UNSET
    server_build: int | Unset = UNSET
    web_adresses: list[int] | None | Unset = UNSET
    statement_mode: StatementMode | Unset = UNSET
    monthly_statement_mode: MonthlyStatementMode | Unset = UNSET
    keep_ticks: int | Unset = UNSET
    statement_weekend: int | Unset = UNSET
    reserved: list[int] | None | Unset = UNSET
    last_activate: datetime.datetime | Unset = UNSET
    stop_last: datetime.datetime | Unset = UNSET
    stop_delay: int | Unset = UNSET
    stop_reason: ServerStopReason | Unset = UNSET
    account_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address = self.address

        port = self.port

        timeout = self.timeout

        demo_account_type: str | Unset = UNSET
        if not isinstance(self.demo_account_type, Unset):
            demo_account_type = self.demo_account_type.value


        time_of_demo = self.time_of_demo

        daylight_correction = self.daylight_correction

        time_zone_real = self.time_zone_real

        time_zone = self.time_zone

        time_sync: None | str | Unset
        if isinstance(self.time_sync, Unset):
            time_sync = UNSET
        else:
            time_sync = self.time_sync

        min_client = self.min_client

        min_api = self.min_api

        feeder_timeout = self.feeder_timeout

        keep_emails = self.keep_emails

        end_hour = self.end_hour

        end_minute = self.end_minute

        optimization_time = self.optimization_time

        optimization_last_time = self.optimization_last_time

        optimization_counter = self.optimization_counter

        optimization_unused: list[int] | None | Unset
        if isinstance(self.optimization_unused, Unset):
            optimization_unused = UNSET
        elif isinstance(self.optimization_unused, list):
            optimization_unused = self.optimization_unused


        else:
            optimization_unused = self.optimization_unused

        anti_flood = self.anti_flood

        flood_control = self.flood_control

        live_update_mode: str | Unset = UNSET
        if not isinstance(self.live_update_mode, Unset):
            live_update_mode = self.live_update_mode.value


        last_order = self.last_order

        last_login = self.last_login

        lost_login = self.lost_login

        rollover_mode: str | Unset = UNSET
        if not isinstance(self.rollover_mode, Unset):
            rollover_mode = self.rollover_mode.value


        path_database: None | str | Unset
        if isinstance(self.path_database, Unset):
            path_database = UNSET
        else:
            path_database = self.path_database

        path_history: None | str | Unset
        if isinstance(self.path_history, Unset):
            path_history = UNSET
        else:
            path_history = self.path_history

        path_log: None | str | Unset
        if isinstance(self.path_log, Unset):
            path_log = UNSET
        else:
            path_log = self.path_log

        overnight_last_day = self.overnight_last_day

        overnight_last_time = self.overnight_last_time

        overnight_prev_time = self.overnight_prev_time

        overmonth_last_month = self.overmonth_last_month

        adapters: None | str | Unset
        if isinstance(self.adapters, Unset):
            adapters = UNSET
        else:
            adapters = self.adapters

        bind_adresses: list[int] | None | Unset
        if isinstance(self.bind_adresses, Unset):
            bind_adresses = UNSET
        elif isinstance(self.bind_adresses, list):
            bind_adresses = self.bind_adresses


        else:
            bind_adresses = self.bind_adresses

        server_version = self.server_version

        server_build = self.server_build

        web_adresses: list[int] | None | Unset
        if isinstance(self.web_adresses, Unset):
            web_adresses = UNSET
        elif isinstance(self.web_adresses, list):
            web_adresses = self.web_adresses


        else:
            web_adresses = self.web_adresses

        statement_mode: str | Unset = UNSET
        if not isinstance(self.statement_mode, Unset):
            statement_mode = self.statement_mode.value


        monthly_statement_mode: str | Unset = UNSET
        if not isinstance(self.monthly_statement_mode, Unset):
            monthly_statement_mode = self.monthly_statement_mode.value


        keep_ticks = self.keep_ticks

        statement_weekend = self.statement_weekend

        reserved: list[int] | None | Unset
        if isinstance(self.reserved, Unset):
            reserved = UNSET
        elif isinstance(self.reserved, list):
            reserved = self.reserved


        else:
            reserved = self.reserved

        last_activate: str | Unset = UNSET
        if not isinstance(self.last_activate, Unset):
            last_activate = self.last_activate.isoformat()

        stop_last: str | Unset = UNSET
        if not isinstance(self.stop_last, Unset):
            stop_last = self.stop_last.isoformat()

        stop_delay = self.stop_delay

        stop_reason: str | Unset = UNSET
        if not isinstance(self.stop_reason, Unset):
            stop_reason = self.stop_reason.value


        account_url: None | str | Unset
        if isinstance(self.account_url, Unset):
            account_url = UNSET
        else:
            account_url = self.account_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner is not UNSET:
            field_dict["owner"] = owner
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if demo_account_type is not UNSET:
            field_dict["demoAccountType"] = demo_account_type
        if time_of_demo is not UNSET:
            field_dict["timeOfDemo"] = time_of_demo
        if daylight_correction is not UNSET:
            field_dict["daylightCorrection"] = daylight_correction
        if time_zone_real is not UNSET:
            field_dict["timeZoneReal"] = time_zone_real
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if time_sync is not UNSET:
            field_dict["timeSync"] = time_sync
        if min_client is not UNSET:
            field_dict["minClient"] = min_client
        if min_api is not UNSET:
            field_dict["minApi"] = min_api
        if feeder_timeout is not UNSET:
            field_dict["feederTimeout"] = feeder_timeout
        if keep_emails is not UNSET:
            field_dict["keepEmails"] = keep_emails
        if end_hour is not UNSET:
            field_dict["endHour"] = end_hour
        if end_minute is not UNSET:
            field_dict["endMinute"] = end_minute
        if optimization_time is not UNSET:
            field_dict["optimizationTime"] = optimization_time
        if optimization_last_time is not UNSET:
            field_dict["optimizationLastTime"] = optimization_last_time
        if optimization_counter is not UNSET:
            field_dict["optimizationCounter"] = optimization_counter
        if optimization_unused is not UNSET:
            field_dict["optimizationUnused"] = optimization_unused
        if anti_flood is not UNSET:
            field_dict["antiFlood"] = anti_flood
        if flood_control is not UNSET:
            field_dict["floodControl"] = flood_control
        if live_update_mode is not UNSET:
            field_dict["liveUpdateMode"] = live_update_mode
        if last_order is not UNSET:
            field_dict["lastOrder"] = last_order
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if lost_login is not UNSET:
            field_dict["lostLogin"] = lost_login
        if rollover_mode is not UNSET:
            field_dict["rolloverMode"] = rollover_mode
        if path_database is not UNSET:
            field_dict["pathDatabase"] = path_database
        if path_history is not UNSET:
            field_dict["pathHistory"] = path_history
        if path_log is not UNSET:
            field_dict["pathLog"] = path_log
        if overnight_last_day is not UNSET:
            field_dict["overnightLastDay"] = overnight_last_day
        if overnight_last_time is not UNSET:
            field_dict["overnightLastTime"] = overnight_last_time
        if overnight_prev_time is not UNSET:
            field_dict["overnightPrevTime"] = overnight_prev_time
        if overmonth_last_month is not UNSET:
            field_dict["overmonthLastMonth"] = overmonth_last_month
        if adapters is not UNSET:
            field_dict["adapters"] = adapters
        if bind_adresses is not UNSET:
            field_dict["bindAdresses"] = bind_adresses
        if server_version is not UNSET:
            field_dict["serverVersion"] = server_version
        if server_build is not UNSET:
            field_dict["serverBuild"] = server_build
        if web_adresses is not UNSET:
            field_dict["webAdresses"] = web_adresses
        if statement_mode is not UNSET:
            field_dict["statementMode"] = statement_mode
        if monthly_statement_mode is not UNSET:
            field_dict["monthlyStatementMode"] = monthly_statement_mode
        if keep_ticks is not UNSET:
            field_dict["keepTicks"] = keep_ticks
        if statement_weekend is not UNSET:
            field_dict["statementWeekend"] = statement_weekend
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if last_activate is not UNSET:
            field_dict["lastActivate"] = last_activate
        if stop_last is not UNSET:
            field_dict["stopLast"] = stop_last
        if stop_delay is not UNSET:
            field_dict["stopDelay"] = stop_delay
        if stop_reason is not UNSET:
            field_dict["stopReason"] = stop_reason
        if account_url is not UNSET:
            field_dict["accountUrl"] = account_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        timeout = d.pop("timeout", UNSET)

        _demo_account_type = d.pop("demoAccountType", UNSET)
        demo_account_type: DemoAccountType | Unset
        if isinstance(_demo_account_type,  Unset):
            demo_account_type = UNSET
        else:
            demo_account_type = DemoAccountType(_demo_account_type)




        time_of_demo = d.pop("timeOfDemo", UNSET)

        daylight_correction = d.pop("daylightCorrection", UNSET)

        time_zone_real = d.pop("timeZoneReal", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        def _parse_time_sync(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_sync = _parse_time_sync(d.pop("timeSync", UNSET))


        min_client = d.pop("minClient", UNSET)

        min_api = d.pop("minApi", UNSET)

        feeder_timeout = d.pop("feederTimeout", UNSET)

        keep_emails = d.pop("keepEmails", UNSET)

        end_hour = d.pop("endHour", UNSET)

        end_minute = d.pop("endMinute", UNSET)

        optimization_time = d.pop("optimizationTime", UNSET)

        optimization_last_time = d.pop("optimizationLastTime", UNSET)

        optimization_counter = d.pop("optimizationCounter", UNSET)

        def _parse_optimization_unused(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                optimization_unused_type_0 = cast(list[int], data)

                return optimization_unused_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        optimization_unused = _parse_optimization_unused(d.pop("optimizationUnused", UNSET))


        anti_flood = d.pop("antiFlood", UNSET)

        flood_control = d.pop("floodControl", UNSET)

        _live_update_mode = d.pop("liveUpdateMode", UNSET)
        live_update_mode: LiveUpdateMode | Unset
        if isinstance(_live_update_mode,  Unset):
            live_update_mode = UNSET
        else:
            live_update_mode = LiveUpdateMode(_live_update_mode)




        last_order = d.pop("lastOrder", UNSET)

        last_login = d.pop("lastLogin", UNSET)

        lost_login = d.pop("lostLogin", UNSET)

        _rollover_mode = d.pop("rolloverMode", UNSET)
        rollover_mode: RolloverMode | Unset
        if isinstance(_rollover_mode,  Unset):
            rollover_mode = UNSET
        else:
            rollover_mode = RolloverMode(_rollover_mode)




        def _parse_path_database(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path_database = _parse_path_database(d.pop("pathDatabase", UNSET))


        def _parse_path_history(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path_history = _parse_path_history(d.pop("pathHistory", UNSET))


        def _parse_path_log(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path_log = _parse_path_log(d.pop("pathLog", UNSET))


        overnight_last_day = d.pop("overnightLastDay", UNSET)

        overnight_last_time = d.pop("overnightLastTime", UNSET)

        overnight_prev_time = d.pop("overnightPrevTime", UNSET)

        overmonth_last_month = d.pop("overmonthLastMonth", UNSET)

        def _parse_adapters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adapters = _parse_adapters(d.pop("adapters", UNSET))


        def _parse_bind_adresses(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bind_adresses_type_0 = cast(list[int], data)

                return bind_adresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        bind_adresses = _parse_bind_adresses(d.pop("bindAdresses", UNSET))


        server_version = d.pop("serverVersion", UNSET)

        server_build = d.pop("serverBuild", UNSET)

        def _parse_web_adresses(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                web_adresses_type_0 = cast(list[int], data)

                return web_adresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        web_adresses = _parse_web_adresses(d.pop("webAdresses", UNSET))


        _statement_mode = d.pop("statementMode", UNSET)
        statement_mode: StatementMode | Unset
        if isinstance(_statement_mode,  Unset):
            statement_mode = UNSET
        else:
            statement_mode = StatementMode(_statement_mode)




        _monthly_statement_mode = d.pop("monthlyStatementMode", UNSET)
        monthly_statement_mode: MonthlyStatementMode | Unset
        if isinstance(_monthly_statement_mode,  Unset):
            monthly_statement_mode = UNSET
        else:
            monthly_statement_mode = MonthlyStatementMode(_monthly_statement_mode)




        keep_ticks = d.pop("keepTicks", UNSET)

        statement_weekend = d.pop("statementWeekend", UNSET)

        def _parse_reserved(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reserved_type_0 = cast(list[int], data)

                return reserved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        reserved = _parse_reserved(d.pop("reserved", UNSET))


        _last_activate = d.pop("lastActivate", UNSET)
        last_activate: datetime.datetime | Unset
        if isinstance(_last_activate,  Unset):
            last_activate = UNSET
        else:
            last_activate = datetime.datetime.fromisoformat(_last_activate)




        _stop_last = d.pop("stopLast", UNSET)
        stop_last: datetime.datetime | Unset
        if isinstance(_stop_last,  Unset):
            stop_last = UNSET
        else:
            stop_last = datetime.datetime.fromisoformat(_stop_last)




        stop_delay = d.pop("stopDelay", UNSET)

        _stop_reason = d.pop("stopReason", UNSET)
        stop_reason: ServerStopReason | Unset
        if isinstance(_stop_reason,  Unset):
            stop_reason = UNSET
        else:
            stop_reason = ServerStopReason(_stop_reason)




        def _parse_account_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_url = _parse_account_url(d.pop("accountUrl", UNSET))


        mt4_common = cls(
            owner=owner,
            name=name,
            address=address,
            port=port,
            timeout=timeout,
            demo_account_type=demo_account_type,
            time_of_demo=time_of_demo,
            daylight_correction=daylight_correction,
            time_zone_real=time_zone_real,
            time_zone=time_zone,
            time_sync=time_sync,
            min_client=min_client,
            min_api=min_api,
            feeder_timeout=feeder_timeout,
            keep_emails=keep_emails,
            end_hour=end_hour,
            end_minute=end_minute,
            optimization_time=optimization_time,
            optimization_last_time=optimization_last_time,
            optimization_counter=optimization_counter,
            optimization_unused=optimization_unused,
            anti_flood=anti_flood,
            flood_control=flood_control,
            live_update_mode=live_update_mode,
            last_order=last_order,
            last_login=last_login,
            lost_login=lost_login,
            rollover_mode=rollover_mode,
            path_database=path_database,
            path_history=path_history,
            path_log=path_log,
            overnight_last_day=overnight_last_day,
            overnight_last_time=overnight_last_time,
            overnight_prev_time=overnight_prev_time,
            overmonth_last_month=overmonth_last_month,
            adapters=adapters,
            bind_adresses=bind_adresses,
            server_version=server_version,
            server_build=server_build,
            web_adresses=web_adresses,
            statement_mode=statement_mode,
            monthly_statement_mode=monthly_statement_mode,
            keep_ticks=keep_ticks,
            statement_weekend=statement_weekend,
            reserved=reserved,
            last_activate=last_activate,
            stop_last=stop_last,
            stop_delay=stop_delay,
            stop_reason=stop_reason,
            account_url=account_url,
        )

        return mt4_common

