from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mt5_plugin_parameter_type import MT5PluginParameterType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5PluginParameter")



@_attrs_define
class MT5PluginParameter:
    """ One parameter of a plugin configuration.

        Attributes:
            name (None | str | Unset): Parameter name, unique inside its configuration.
            type_ (MT5PluginParameterType | None | Unset): Type the module expects for the value.<br/>One of: String, Int,
                Float, Time, Date, DateTime, Groups, Symbols, Bool, Color, Gateway, UltencyMatchingEngine, UltencyProvider,
                UltencySymbols, Period. Case-insensitive; the numeric value is accepted too. Any other value is refused with
                error code Validation.
            value (None | str | Unset): Value in its text form: numbers as decimal strings, times as UNIX seconds.
     """

    name: None | str | Unset = UNSET
    type_: MT5PluginParameterType | None | Unset = UNSET
    value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, MT5PluginParameterType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_type_(data: object) -> MT5PluginParameterType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = MT5PluginParameterType(data)



                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5PluginParameterType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        mt5_plugin_parameter = cls(
            name=name,
            type_=type_,
            value=value,
        )

        return mt5_plugin_parameter

