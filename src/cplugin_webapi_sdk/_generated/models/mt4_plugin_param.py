from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt4_plugin import MT4Plugin
  from ..models.mt4_plugin_config import MT4PluginConfig





T = TypeVar("T", bound="MT4PluginParam")



@_attrs_define
class MT4PluginParam:
    """ v2 DTO for an MT4 plugin together with its parameter set (sidecar-only).
    Mirrors wrapper's `ConPluginParam`.

        Attributes:
            plugin (MT4Plugin | None | Unset): Plugin metadata
            params (list[MT4PluginConfig] | None | Unset): Plugin parameter array (name/value pairs)
     """

    plugin: MT4Plugin | None | Unset = UNSET
    params: list[MT4PluginConfig] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt4_plugin import MT4Plugin
        from ..models.mt4_plugin_config import MT4PluginConfig
        plugin: dict[str, Any] | None | Unset
        if isinstance(self.plugin, Unset):
            plugin = UNSET
        elif isinstance(self.plugin, MT4Plugin):
            plugin = self.plugin.to_dict()
        else:
            plugin = self.plugin

        params: list[dict[str, Any]] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, list):
            params = []
            for params_type_0_item_data in self.params:
                params_type_0_item = params_type_0_item_data.to_dict()
                params.append(params_type_0_item)


        else:
            params = self.params


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if plugin is not UNSET:
            field_dict["plugin"] = plugin
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt4_plugin import MT4Plugin
        from ..models.mt4_plugin_config import MT4PluginConfig
        d = dict(src_dict)
        def _parse_plugin(data: object) -> MT4Plugin | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plugin_type_1 = MT4Plugin.from_dict(data)



                return plugin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT4Plugin | None | Unset, data)

        plugin = _parse_plugin(d.pop("plugin", UNSET))


        def _parse_params(data: object) -> list[MT4PluginConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                params_type_0 = []
                _params_type_0 = data
                for params_type_0_item_data in (_params_type_0):
                    params_type_0_item = MT4PluginConfig.from_dict(params_type_0_item_data)



                    params_type_0.append(params_type_0_item)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT4PluginConfig] | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))


        mt4_plugin_param = cls(
            plugin=plugin,
            params=params,
        )

        return mt4_plugin_param

