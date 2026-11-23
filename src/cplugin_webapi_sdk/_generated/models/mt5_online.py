from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Online")



@_attrs_define
class MT5Online:
    """ One open connection to the trade server, v2 read DTO.

        Attributes:
            session_id (int | Unset): Session identifier, unique for the trade server while the session lives.
            login (int | Unset): Login of the account the session belongs to.
            group (None | str | Unset): Group of the account at the time of the connection.
            address (None | str | Unset): Address the client connected from.
            connection_type (None | str | Unset): Kind of the connected application — a trading terminal, a mobile app, a
                manager terminal or an API client.
            build (int | Unset): Build number of the connected application.
            time (datetime.datetime | None | Unset): Connection time, as the trade server counts it. Absent when the server
                sent no time.
            computer_id (None | str | Unset): Identifier of the computer the session was opened from.
     """

    session_id: int | Unset = UNSET
    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    connection_type: None | str | Unset = UNSET
    build: int | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    computer_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        login = self.login

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        connection_type: None | str | Unset
        if isinstance(self.connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = self.connection_type

        build = self.build

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        computer_id: None | str | Unset
        if isinstance(self.computer_id, Unset):
            computer_id = UNSET
        else:
            computer_id = self.computer_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group
        if address is not UNSET:
            field_dict["address"] = address
        if connection_type is not UNSET:
            field_dict["connectionType"] = connection_type
        if build is not UNSET:
            field_dict["build"] = build
        if time is not UNSET:
            field_dict["time"] = time
        if computer_id is not UNSET:
            field_dict["computerId"] = computer_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        login = d.pop("login", UNSET)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_connection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_type = _parse_connection_type(d.pop("connectionType", UNSET))


        build = d.pop("build", UNSET)

        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)



                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        def _parse_computer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        computer_id = _parse_computer_id(d.pop("computerId", UNSET))


        mt5_online = cls(
            session_id=session_id,
            login=login,
            group=group,
            address=address,
            connection_type=connection_type,
            build=build,
            time=time,
            computer_id=computer_id,
        )

        return mt5_online

