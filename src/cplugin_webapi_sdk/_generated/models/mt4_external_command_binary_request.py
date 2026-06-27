from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4ExternalCommandBinaryRequest")



@_attrs_define
class MT4ExternalCommandBinaryRequest:
    """ v2 DTO for binary `ExternalCommand` roundtrips (sidecar-only).
    The MT4 server's plugin API has no enforced wire-format — clients
    agree with their plugin on the binary layout and pass arbitrary
    bytes through this endpoint.

        Attributes:
            data (None | str | Unset): Binary payload to send to the plugin (base64-encoded)
     """

    data: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        mt4_external_command_binary_request = cls(
            data=data,
        )

        return mt4_external_command_binary_request

