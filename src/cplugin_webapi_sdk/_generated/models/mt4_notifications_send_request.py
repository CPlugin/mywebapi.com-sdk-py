from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4NotificationsSendRequest")



@_attrs_define
class MT4NotificationsSendRequest:
    """ Request body for the v2 `NotificationsSend` admin endpoint —
    pushes a single message to one or more MT4 clients identified by
    account login. Maps onto the platform's
    `NotificationsSend2(int[] logins, string message)`.

        Attributes:
            logins (list[int] | None | Unset): Account logins to deliver the notification to (server-side fan-out
                — the platform sends one notification per recipient in a single
                Manager-API call).
            message (None | str | Unset): Notification text. Single-line; the MT4 mobile client displays it
                as the push body. Controller enforces a length cap to keep the
                payload tractable on the unmanaged side.
     """

    logins: list[int] | None | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        logins: list[int] | None | Unset
        if isinstance(self.logins, Unset):
            logins = UNSET
        elif isinstance(self.logins, list):
            logins = self.logins


        else:
            logins = self.logins

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if logins is not UNSET:
            field_dict["logins"] = logins
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        mt4_notifications_send_request = cls(
            logins=logins,
            message=message,
        )

        return mt4_notifications_send_request

