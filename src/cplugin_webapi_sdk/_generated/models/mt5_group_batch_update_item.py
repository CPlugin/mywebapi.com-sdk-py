from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_group_update_request import MT5GroupUpdateRequest





T = TypeVar("T", bound="MT5GroupBatchUpdateItem")



@_attrs_define
class MT5GroupBatchUpdateItem:
    r""" One entry of a batch group update: the group to change and the fields to write.

        Attributes:
            group (None | str | Unset): Full group name including the path, e.g. `demo\demoforex`.
            update (MT5GroupUpdateRequest | None | Unset): Fields to change; fields left out keep their current server
                value.
     """

    group: None | str | Unset = UNSET
    update: MT5GroupUpdateRequest | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_group_update_request import MT5GroupUpdateRequest
        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        update: dict[str, Any] | None | Unset
        if isinstance(self.update, Unset):
            update = UNSET
        elif isinstance(self.update, MT5GroupUpdateRequest):
            update = self.update.to_dict()
        else:
            update = self.update


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_group_update_request import MT5GroupUpdateRequest
        d = dict(src_dict)
        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_update(data: object) -> MT5GroupUpdateRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_type_1 = MT5GroupUpdateRequest.from_dict(data)



                return update_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5GroupUpdateRequest | None | Unset, data)

        update = _parse_update(d.pop("update", UNSET))


        mt5_group_batch_update_item = cls(
            group=group,
            update=update,
        )

        return mt5_group_batch_update_item

