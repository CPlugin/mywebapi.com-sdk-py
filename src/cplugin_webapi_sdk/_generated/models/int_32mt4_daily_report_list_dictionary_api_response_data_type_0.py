from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.mt4_daily_report import MT4DailyReport





T = TypeVar("T", bound="Int32MT4DailyReportListDictionaryApiResponseDataType0")



@_attrs_define
class Int32MT4DailyReportListDictionaryApiResponseDataType0:
    """ 
     """

    additional_properties: dict[str, list[MT4DailyReport] | None] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt4_daily_report import MT4DailyReport
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for additional_property_type_0_item_data in prop:
                    additional_property_type_0_item = additional_property_type_0_item_data.to_dict()
                    field_dict[prop_name].append(additional_property_type_0_item)


            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt4_daily_report import MT4DailyReport
        d = dict(src_dict)
        int_32mt4_daily_report_list_dictionary_api_response_data_type_0 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> list[MT4DailyReport] | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_0 = []
                    _additional_property_type_0 = data
                    for additional_property_type_0_item_data in (_additional_property_type_0):
                        additional_property_type_0_item = MT4DailyReport.from_dict(additional_property_type_0_item_data)



                        additional_property_type_0.append(additional_property_type_0_item)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(list[MT4DailyReport] | None, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        int_32mt4_daily_report_list_dictionary_api_response_data_type_0.additional_properties = additional_properties
        return int_32mt4_daily_report_list_dictionary_api_response_data_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[MT4DailyReport] | None:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[MT4DailyReport] | None) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
