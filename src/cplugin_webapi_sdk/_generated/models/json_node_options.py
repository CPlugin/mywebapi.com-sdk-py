from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="JsonNodeOptions")



@_attrs_define
class JsonNodeOptions:
    """ 
        Attributes:
            property_name_case_insensitive (bool | Unset):
     """

    property_name_case_insensitive: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        property_name_case_insensitive = self.property_name_case_insensitive


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if property_name_case_insensitive is not UNSET:
            field_dict["propertyNameCaseInsensitive"] = property_name_case_insensitive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_name_case_insensitive = d.pop("propertyNameCaseInsensitive", UNSET)

        json_node_options = cls(
            property_name_case_insensitive=property_name_case_insensitive,
        )

        return json_node_options

