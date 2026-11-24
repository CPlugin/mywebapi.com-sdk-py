from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5NotificationsSendRequest")



@_attrs_define
class MT5NotificationsSendRequest:
    """ A push notification to send to the mobile terminals of a set of accounts.

        Attributes:
            logins (list[int] | None | Unset): Logins of the accounts to notify; used instead of `MetaQuotesIds`.
            meta_quotes_ids (None | str | Unset): Comma-separated MetaQuotes identifiers of the mobile terminals; used
                instead of `Logins`.
            message (None | str | Unset): Text of the notification.
     """

    logins: list[int] | None | Unset = UNSET
    meta_quotes_ids: None | str | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        logins: list[int] | None | Unset
        if isinstance(self.logins, Unset):
            logins = UNSET
        elif isinstance(self.logins, list):
            logins = self.logins


        else:
            logins = self.logins

        meta_quotes_ids: None | str | Unset
        if isinstance(self.meta_quotes_ids, Unset):
            meta_quotes_ids = UNSET
        else:
            meta_quotes_ids = self.meta_quotes_ids

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
        if meta_quotes_ids is not UNSET:
            field_dict["metaQuotesIds"] = meta_quotes_ids
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


        def _parse_meta_quotes_ids(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meta_quotes_ids = _parse_meta_quotes_ids(d.pop("metaQuotesIds", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        mt5_notifications_send_request = cls(
            logins=logins,
            meta_quotes_ids=meta_quotes_ids,
            message=message,
        )

        return mt5_notifications_send_request

