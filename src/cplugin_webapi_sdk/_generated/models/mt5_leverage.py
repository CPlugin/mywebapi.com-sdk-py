from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_leverage_rule import MT5LeverageRule





T = TypeVar("T", bound="MT5Leverage")



@_attrs_define
class MT5Leverage:
    """ Floating margin configuration: a named set of rules that decides which margin rate applies to a
    position, depending on the volume or the value the account carries in the symbol.

        Attributes:
            name (None | str | Unset): Configuration name; it identifies the record on the trade server.
            rules (list[MT5LeverageRule] | None | Unset): Rules of the configuration, in the order the trade server applies
                them.
     """

    name: None | str | Unset = UNSET
    rules: list[MT5LeverageRule] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_leverage_rule import MT5LeverageRule
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)


        else:
            rules = self.rules


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_leverage_rule import MT5LeverageRule
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_rules(data: object) -> list[MT5LeverageRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in (_rules_type_0):
                    rules_type_0_item = MT5LeverageRule.from_dict(rules_type_0_item_data)



                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5LeverageRule] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))


        mt5_leverage = cls(
            name=name,
            rules=rules,
        )

        return mt5_leverage

