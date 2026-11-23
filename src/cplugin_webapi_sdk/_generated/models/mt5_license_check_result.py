from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_result import MT5Result
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5LicenseCheckResult")



@_attrs_define
class MT5LicenseCheckResult:
    """ Answer of the trade server to a license check.

        Attributes:
            retcode (MT5Result | Unset):
            sign (None | str | Unset): Signature of the result code, the application name and the random sequence, produced
                by the
                platform with its private key. Empty when the check failed.
     """

    retcode: MT5Result | Unset = UNSET
    sign: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        retcode: str | Unset = UNSET
        if not isinstance(self.retcode, Unset):
            retcode = self.retcode.value


        sign: None | str | Unset
        if isinstance(self.sign, Unset):
            sign = UNSET
        else:
            sign = self.sign


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if retcode is not UNSET:
            field_dict["retcode"] = retcode
        if sign is not UNSET:
            field_dict["sign"] = sign

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _retcode = d.pop("retcode", UNSET)
        retcode: MT5Result | Unset
        if isinstance(_retcode,  Unset):
            retcode = UNSET
        else:
            retcode = MT5Result(_retcode)




        def _parse_sign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sign = _parse_sign(d.pop("sign", UNSET))


        mt5_license_check_result = cls(
            retcode=retcode,
            sign=sign,
        )

        return mt5_license_check_result

