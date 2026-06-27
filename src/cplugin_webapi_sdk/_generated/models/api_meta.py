from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paging_meta import PagingMeta





T = TypeVar("T", bound="ApiMeta")



@_attrs_define
class ApiMeta:
    """ Response metadata. ActivityId is the W3C trace-id for correlation in Seq/SigNoz.
    Paging is present only on paginated list responses; otherwise it is omitted —
    the global JSON context policy serialises null fields, so we override that here
    with System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull.

        Attributes:
            activity_id (None | str | Unset): W3C trace id for correlating this response in logs and tracing (Seq/SigNoz).
            paging (None | PagingMeta | Unset): Pagination info; present only on list responses, omitted otherwise.
     """

    activity_id: None | str | Unset = UNSET
    paging: None | PagingMeta | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.paging_meta import PagingMeta
        activity_id: None | str | Unset
        if isinstance(self.activity_id, Unset):
            activity_id = UNSET
        else:
            activity_id = self.activity_id

        paging: dict[str, Any] | None | Unset
        if isinstance(self.paging, Unset):
            paging = UNSET
        elif isinstance(self.paging, PagingMeta):
            paging = self.paging.to_dict()
        else:
            paging = self.paging


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paging_meta import PagingMeta
        d = dict(src_dict)
        def _parse_activity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activity_id = _parse_activity_id(d.pop("activityId", UNSET))


        def _parse_paging(data: object) -> None | PagingMeta | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                paging_type_1 = PagingMeta.from_dict(data)



                return paging_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PagingMeta | Unset, data)

        paging = _parse_paging(d.pop("paging", UNSET))


        api_meta = cls(
            activity_id=activity_id,
            paging=paging,
        )

        return api_meta

