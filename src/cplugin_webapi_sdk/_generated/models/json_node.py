from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.json_node_options import JsonNodeOptions





T = TypeVar("T", bound="JsonNode")



@_attrs_define
class JsonNode:
    """ 
        Attributes:
            options (JsonNodeOptions | None | Unset):
            parent (JsonNode | None | Unset):
            root (JsonNode | None | Unset):
     """

    options: JsonNodeOptions | None | Unset = UNSET
    parent: JsonNode | None | Unset = UNSET
    root: JsonNode | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_node_options import JsonNodeOptions
        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, JsonNodeOptions):
            options = self.options.to_dict()
        else:
            options = self.options

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, JsonNode):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        root: dict[str, Any] | None | Unset
        if isinstance(self.root, Unset):
            root = UNSET
        elif isinstance(self.root, JsonNode):
            root = self.root.to_dict()
        else:
            root = self.root


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if options is not UNSET:
            field_dict["options"] = options
        if parent is not UNSET:
            field_dict["parent"] = parent
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node_options import JsonNodeOptions
        d = dict(src_dict)
        def _parse_options(data: object) -> JsonNodeOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_1 = JsonNodeOptions.from_dict(data)



                return options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JsonNodeOptions | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_parent(data: object) -> JsonNode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = JsonNode.from_dict(data)



                return parent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JsonNode | None | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))


        def _parse_root(data: object) -> JsonNode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                root_type_1 = JsonNode.from_dict(data)



                return root_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JsonNode | None | Unset, data)

        root = _parse_root(d.pop("root", UNSET))


        json_node = cls(
            options=options,
            parent=parent,
            root=root,
        )

        return json_node

