from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4UsersGroupOp")



@_attrs_define
class MT4UsersGroupOp:
    """ v2 request body for `UsersGroupOp` — bulk group-membership / leverage /
    enable-disable / delete operation across a list of account logins.

        Attributes:
            command (None | str | Unset): Bulk operation: `"Delete"`, `"Enable"`, `"Disable"`, `"Leverage"`, or
                `"SetGroup"`.
            new_group (None | str | Unset): Target group name (max 15 chars + NUL). Only used by `SetGroup`.
            leverage (int | Unset): New leverage value (e.g. 100, 200, 500). Only used by `Leverage`.
            logins (list[int] | None | Unset): List of account logins (account numbers) to apply the operation to. Must be
                non-empty.
     """

    command: None | str | Unset = UNSET
    new_group: None | str | Unset = UNSET
    leverage: int | Unset = UNSET
    logins: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        command: None | str | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        else:
            command = self.command

        new_group: None | str | Unset
        if isinstance(self.new_group, Unset):
            new_group = UNSET
        else:
            new_group = self.new_group

        leverage = self.leverage

        logins: list[int] | None | Unset
        if isinstance(self.logins, Unset):
            logins = UNSET
        elif isinstance(self.logins, list):
            logins = self.logins


        else:
            logins = self.logins


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if command is not UNSET:
            field_dict["command"] = command
        if new_group is not UNSET:
            field_dict["newGroup"] = new_group
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if logins is not UNSET:
            field_dict["logins"] = logins

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("command", UNSET))


        def _parse_new_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_group = _parse_new_group(d.pop("newGroup", UNSET))


        leverage = d.pop("leverage", UNSET)

        def _parse_logins(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logins_type_0 = cast(list[int], data)

                return logins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        logins = _parse_logins(d.pop("logins", UNSET))


        mt4_users_group_op = cls(
            command=command,
            new_group=new_group,
            leverage=leverage,
            logins=logins,
        )

        return mt4_users_group_op

