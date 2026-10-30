from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.result_code import ResultCode
from ..models.web_api_error_code import WebApiErrorCode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ApiError")



@_attrs_define
class ApiError:
    """ v2 error body. Code is the stable transport error code; ManagerCode is the raw MT4
    ResultCode (serialized as a string for a known enum member, or as a number for an
    unrecognised value returned by MT4); Message is a human-readable description.

        Attributes:
            code (WebApiErrorCode | Unset): Transport-level error classification for v2 responses. Stable across MT4
                platform versions — clients can branch on this without knowing MT-specific
                codes. When ErrorCode == MT4Error, see ManagerCode for the underlying
                MT4 ResultCode value.
            manager_code (None | ResultCode | Unset): Raw MT4/MT5 manager result code, when the error came from the trading
                platform; otherwise null.
            message (None | str | Unset): Human-readable error description.
     """

    code: WebApiErrorCode | Unset = UNSET
    manager_code: None | ResultCode | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value


        manager_code: None | str | Unset
        if isinstance(self.manager_code, Unset):
            manager_code = UNSET
        elif isinstance(self.manager_code, ResultCode):
            manager_code = self.manager_code.value
        else:
            manager_code = self.manager_code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if manager_code is not UNSET:
            field_dict["managerCode"] = manager_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: WebApiErrorCode | Unset
        if isinstance(_code,  Unset):
            code = UNSET
        else:
            code = WebApiErrorCode(_code)




        def _parse_manager_code(data: object) -> None | ResultCode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manager_code_type_1 = ResultCode(data)



                return manager_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultCode | Unset, data)

        manager_code = _parse_manager_code(d.pop("managerCode", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        api_error = cls(
            code=code,
            manager_code=manager_code,
            message=message,
        )

        return api_error

