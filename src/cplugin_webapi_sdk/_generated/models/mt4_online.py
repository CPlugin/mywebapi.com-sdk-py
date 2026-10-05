from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Online")



@_attrs_define
class MT4Online:
    """ v2 DTO describing an online user session entry. Curated subset of the
    the platform's OnlineRecord — exposes the login id and group name, which is
    what callers actually need to know who is connected. IP, Counter and
    internal Reserved fields are intentionally omitted: IP is potentially
    PII and not always meaningful (NAT, proxies), Counter/Reserved are
    platform bookkeeping.

        Attributes:
            login (int | Unset): Trading account number (login)
            group (None | str | Unset): Group name the account belongs to
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        mt4_online = cls(
            login=login,
            group=group,
        )

        return mt4_online

