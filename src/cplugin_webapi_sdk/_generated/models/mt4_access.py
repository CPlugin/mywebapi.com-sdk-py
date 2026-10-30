from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Access")



@_attrs_define
class MT4Access:
    """ v2 DTO for a single MT4 firewall (access) rule. Curated subset of
    the platform's ConAccess struct — drops the 17-int Reserved padding.
    IpFrom/IpTo are widened from uint to long so the JSON-serialized
    numeric value fits inside JS Number safely (no precision loss).

        Attributes:
            action (int | Unset): Firewall rule action — raw MT4 value preserved (FW_BLOCK / FW_PERMIT
                per the platform's enum encoding; surfaced as int because the platform
                itself surfaces it as int).
            ip_from (int | Unset): IP range start (uint widened to long for JSON safety)
            ip_to (int | Unset): IP range end (uint widened to long for JSON safety)
            comment (None | str | Unset): Free-form comment for the rule
     """

    action: int | Unset = UNSET
    ip_from: int | Unset = UNSET
    ip_to: int | Unset = UNSET
    comment: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        ip_from = self.ip_from

        ip_to = self.ip_to

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if ip_from is not UNSET:
            field_dict["ipFrom"] = ip_from
        if ip_to is not UNSET:
            field_dict["ipTo"] = ip_to
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        ip_from = d.pop("ipFrom", UNSET)

        ip_to = d.pop("ipTo", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        mt4_access = cls(
            action=action,
            ip_from=ip_from,
            ip_to=ip_to,
            comment=comment,
        )

        return mt4_access

