from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5MessengerSendRequest")



@_attrs_define
class MT5MessengerSendRequest:
    """ An SMS to send through the messenger integration of the trade server.

        Attributes:
            destination (None | str | Unset): Recipient phone number in international format, for example `+74951113594`.
            group (None | str | Unset): Group whose provider serves the message; optional.
            sender (None | str | Unset): Sender name, where the provider supports one; optional.
            text (None | str | Unset): Message text.
     """

    destination: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    sender: None | str | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        destination: None | str | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        sender: None | str | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        else:
            sender = self.sender

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if destination is not UNSET:
            field_dict["destination"] = destination
        if group is not UNSET:
            field_dict["group"] = group
        if sender is not UNSET:
            field_dict["sender"] = sender
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination = _parse_destination(d.pop("destination", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_sender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        mt5_messenger_send_request = cls(
            destination=destination,
            group=group,
            sender=sender,
            text=text,
        )

        return mt5_messenger_send_request

