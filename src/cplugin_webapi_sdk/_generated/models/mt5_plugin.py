from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_plugin_mode import MT5PluginMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_plugin_parameter import MT5PluginParameter





T = TypeVar("T", bound="MT5Plugin")



@_attrs_define
class MT5Plugin:
    """ Plugin configuration: the module loaded on a trade server together with the parameters it reads on
    start.

        Attributes:
            name (None | str | Unset): Configuration name; it identifies the record on the trade server.
            server (int | None | Unset): Identifier of the trade server the module runs on.
            module (None | str | Unset): Module the configuration belongs to, as the plugin file names it.
            mode (MT5PluginMode | None | Unset): Whether the platform keeps the configuration loaded.<br/>One of: Disabled,
                Enabled. Case-insensitive; the numeric value is accepted too. Any other value is refused with error code
                Validation.
            flags (None | str | Unset): Behaviour flags of the module.
            parameters (list[MT5PluginParameter] | None | Unset): Parameters of the module, in storage order.
     """

    name: None | str | Unset = UNSET
    server: int | None | Unset = UNSET
    module: None | str | Unset = UNSET
    mode: MT5PluginMode | None | Unset = UNSET
    flags: None | str | Unset = UNSET
    parameters: list[MT5PluginParameter] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_plugin_parameter import MT5PluginParameter
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        server: int | None | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        module: None | str | Unset
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, MT5PluginMode):
            mode = self.mode.value
        else:
            mode = self.mode

        flags: None | str | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        parameters: list[dict[str, Any]] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, list):
            parameters = []
            for parameters_type_0_item_data in self.parameters:
                parameters_type_0_item = parameters_type_0_item_data.to_dict()
                parameters.append(parameters_type_0_item)


        else:
            parameters = self.parameters


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if server is not UNSET:
            field_dict["server"] = server
        if module is not UNSET:
            field_dict["module"] = module
        if mode is not UNSET:
            field_dict["mode"] = mode
        if flags is not UNSET:
            field_dict["flags"] = flags
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_plugin_parameter import MT5PluginParameter
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_server(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server = _parse_server(d.pop("server", UNSET))


        def _parse_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module = _parse_module(d.pop("module", UNSET))


        def _parse_mode(data: object) -> MT5PluginMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = MT5PluginMode(data)



                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5PluginMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        def _parse_flags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_parameters(data: object) -> list[MT5PluginParameter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parameters_type_0 = []
                _parameters_type_0 = data
                for parameters_type_0_item_data in (_parameters_type_0):
                    parameters_type_0_item = MT5PluginParameter.from_dict(parameters_type_0_item_data)



                    parameters_type_0.append(parameters_type_0_item)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5PluginParameter] | None | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))


        mt5_plugin = cls(
            name=name,
            server=server,
            module=module,
            mode=mode,
            flags=flags,
            parameters=parameters,
        )

        return mt5_plugin

