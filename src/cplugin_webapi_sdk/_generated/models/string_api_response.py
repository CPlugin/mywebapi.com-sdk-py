from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.api_error import ApiError
  from ..models.api_meta import ApiMeta





T = TypeVar("T", bound="StringApiResponse")



@_attrs_define
class StringApiResponse:
    """ Unified v2 response envelope: data is the payload (null on error); error is the
    error object (null on success, always serialised); meta contains response metadata
    (activityId and optional paging). HTTP status is always 200.

        Attributes:
            data (None | str | Unset):
            error (ApiError | None | Unset): v2 error body. Code is the stable transport error code; ManagerCode is the raw
                MT4
                ResultCode (serialized as a string for a known enum member, or as a number for an
                unrecognised value returned by MT4); Message is a human-readable description.
            meta (ApiMeta | None | Unset): Response metadata. ActivityId identifies the request — quote it when you contact
                support.
                Paging is present only on paginated list responses; otherwise it is omitted.
     """

    data: None | str | Unset = UNSET
    error: ApiError | None | Unset = UNSET
    meta: ApiMeta | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error import ApiError
        from ..models.api_meta import ApiMeta
        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ApiError):
            error = self.error.to_dict()
        else:
            error = self.error

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ApiMeta):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error import ApiError
        from ..models.api_meta import ApiMeta
        d = dict(src_dict)
        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        def _parse_error(data: object) -> ApiError | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = ApiError.from_dict(data)



                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiError | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_meta(data: object) -> ApiMeta | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_1 = ApiMeta.from_dict(data)



                return meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeta | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        string_api_response = cls(
            data=data,
            error=error,
            meta=meta,
        )

        return string_api_response

