from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4LogsModeRequest")



@_attrs_define
class MT4LogsModeRequest:
    """ Logging mode of the connection that serves the request.

        Attributes:
            mode (None | str | Unset): `Enabled` keeps the Manager API log of this connection, `Disabled` stops it.
                            The mode applies to the connection, not to the whole trade server, and survives only
                            for the lifetime of that connection.<br/>One of: Enabled, Disabled. Case-insensitive; the numeric
                value is accepted too. Any other value is refused with error code Validation.
     """

    mode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        mt4_logs_mode_request = cls(
            mode=mode,
        )

        return mt4_logs_mode_request

