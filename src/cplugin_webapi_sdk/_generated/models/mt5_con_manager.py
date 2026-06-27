from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.en_manager_limit import EnManagerLimit
from ..models.en_manager_rights import EnManagerRights
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5ConManager")



@_attrs_define
class MT5ConManager:
    """ 
        Attributes:
            login (int | None | Unset): Get and set the login of a manager
            mailbox (None | str | Unset): Get and set the name of a manager's mailbox in the internal mail system.
            server (int | None | Unset): Get and set the ID of the trade server, to which the manager belongs.
            limit_logs (EnManagerLimit | None | Unset): Get and set the time period of system logs available to a manager.
            limit_reports (EnManagerLimit | None | Unset): Get and set the time period of reports available to a manager.
            right (list[EnManagerRights] | None | Unset): What is granted to manager.<br />
                Features not enlisted here means that such features is not permitted.<br />
     """

    login: int | None | Unset = UNSET
    mailbox: None | str | Unset = UNSET
    server: int | None | Unset = UNSET
    limit_logs: EnManagerLimit | None | Unset = UNSET
    limit_reports: EnManagerLimit | None | Unset = UNSET
    right: list[EnManagerRights] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login: int | None | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        mailbox: None | str | Unset
        if isinstance(self.mailbox, Unset):
            mailbox = UNSET
        else:
            mailbox = self.mailbox

        server: int | None | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        limit_logs: None | str | Unset
        if isinstance(self.limit_logs, Unset):
            limit_logs = UNSET
        elif isinstance(self.limit_logs, EnManagerLimit):
            limit_logs = self.limit_logs.value
        else:
            limit_logs = self.limit_logs

        limit_reports: None | str | Unset
        if isinstance(self.limit_reports, Unset):
            limit_reports = UNSET
        elif isinstance(self.limit_reports, EnManagerLimit):
            limit_reports = self.limit_reports.value
        else:
            limit_reports = self.limit_reports

        right: list[str] | None | Unset
        if isinstance(self.right, Unset):
            right = UNSET
        elif isinstance(self.right, list):
            right = []
            for right_type_0_item_data in self.right:
                right_type_0_item = right_type_0_item_data.value
                right.append(right_type_0_item)


        else:
            right = self.right


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if server is not UNSET:
            field_dict["server"] = server
        if limit_logs is not UNSET:
            field_dict["limitLogs"] = limit_logs
        if limit_reports is not UNSET:
            field_dict["limitReports"] = limit_reports
        if right is not UNSET:
            field_dict["right"] = right

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_mailbox(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mailbox = _parse_mailbox(d.pop("mailbox", UNSET))


        def _parse_server(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server = _parse_server(d.pop("server", UNSET))


        def _parse_limit_logs(data: object) -> EnManagerLimit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_logs_type_1 = EnManagerLimit(data)



                return limit_logs_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnManagerLimit | None | Unset, data)

        limit_logs = _parse_limit_logs(d.pop("limitLogs", UNSET))


        def _parse_limit_reports(data: object) -> EnManagerLimit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_reports_type_1 = EnManagerLimit(data)



                return limit_reports_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnManagerLimit | None | Unset, data)

        limit_reports = _parse_limit_reports(d.pop("limitReports", UNSET))


        def _parse_right(data: object) -> list[EnManagerRights] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                right_type_0 = []
                _right_type_0 = data
                for right_type_0_item_data in (_right_type_0):
                    right_type_0_item = EnManagerRights(right_type_0_item_data)



                    right_type_0.append(right_type_0_item)

                return right_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EnManagerRights] | None | Unset, data)

        right = _parse_right(d.pop("right", UNSET))


        mt5_con_manager = cls(
            login=login,
            mailbox=mailbox,
            server=server,
            limit_logs=limit_logs,
            limit_reports=limit_reports,
            right=right,
        )

        return mt5_con_manager

