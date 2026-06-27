from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_con_commission import MT5ConCommission





T = TypeVar("T", bound="MT5ConGroupCommissionsType0")



@_attrs_define
class MT5ConGroupCommissionsType0:
    """ /// <strong>Setter not yet implemented. If you want to send this value to MT5, ask vendor to implement this feature.
    Exception will be thrown if you send anything but null here.</strong><br /><br />

     """

    additional_properties: dict[str, MT5ConCommission] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_con_commission import MT5ConCommission
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_con_commission import MT5ConCommission
        d = dict(src_dict)
        mt5_con_group_commissions_type_0 = cls(
        )


        from ..models.mt5_con_comm_tier import MT5ConCommTier
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = MT5ConCommission.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        mt5_con_group_commissions_type_0.additional_properties = additional_properties
        return mt5_con_group_commissions_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> MT5ConCommission:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: MT5ConCommission) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
