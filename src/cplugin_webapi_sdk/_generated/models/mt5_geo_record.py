from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT5GeoRecord")



@_attrs_define
class MT5GeoRecord:
    """ Description of an IP address resolved by the trade server.

        Attributes:
            i_pv_4_from (None | str | Unset): Beginning of the address range the address belongs to, in dotted IPv4
                notation.
            i_pv_4_to (None | str | Unset): End of the address range the address belongs to, in dotted IPv4 notation.
            continent (None | str | Unset): Continent.
            country (None | str | Unset): Country.
            city (None | str | Unset): City.
            region (None | str | Unset): Region or state.
            province (None | str | Unset): Province or district.
            asn (int | Unset): Autonomous system number.
            asn_organization (None | str | Unset): Name of the autonomous system.
            isp (None | str | Unset): Internet service provider.
            isp_organization (None | str | Unset): Organization that owns the address.
            latitude (float | Unset): Geographical latitude.
            longitude (float | Unset): Geographical longitude.
            details (int | Unset): Additional characteristics of the address as a bit mask: proxy, VPN, data centre, host of
                attacks or spam, botnet member, search engine bot, blacklisted address, headless browser.
     """

    i_pv_4_from: None | str | Unset = UNSET
    i_pv_4_to: None | str | Unset = UNSET
    continent: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    province: None | str | Unset = UNSET
    asn: int | Unset = UNSET
    asn_organization: None | str | Unset = UNSET
    isp: None | str | Unset = UNSET
    isp_organization: None | str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    details: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        i_pv_4_from: None | str | Unset
        if isinstance(self.i_pv_4_from, Unset):
            i_pv_4_from = UNSET
        else:
            i_pv_4_from = self.i_pv_4_from

        i_pv_4_to: None | str | Unset
        if isinstance(self.i_pv_4_to, Unset):
            i_pv_4_to = UNSET
        else:
            i_pv_4_to = self.i_pv_4_to

        continent: None | str | Unset
        if isinstance(self.continent, Unset):
            continent = UNSET
        else:
            continent = self.continent

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        province: None | str | Unset
        if isinstance(self.province, Unset):
            province = UNSET
        else:
            province = self.province

        asn = self.asn

        asn_organization: None | str | Unset
        if isinstance(self.asn_organization, Unset):
            asn_organization = UNSET
        else:
            asn_organization = self.asn_organization

        isp: None | str | Unset
        if isinstance(self.isp, Unset):
            isp = UNSET
        else:
            isp = self.isp

        isp_organization: None | str | Unset
        if isinstance(self.isp_organization, Unset):
            isp_organization = UNSET
        else:
            isp_organization = self.isp_organization

        latitude = self.latitude

        longitude = self.longitude

        details = self.details


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if i_pv_4_from is not UNSET:
            field_dict["iPv4From"] = i_pv_4_from
        if i_pv_4_to is not UNSET:
            field_dict["iPv4To"] = i_pv_4_to
        if continent is not UNSET:
            field_dict["continent"] = continent
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if province is not UNSET:
            field_dict["province"] = province
        if asn is not UNSET:
            field_dict["asn"] = asn
        if asn_organization is not UNSET:
            field_dict["asnOrganization"] = asn_organization
        if isp is not UNSET:
            field_dict["isp"] = isp
        if isp_organization is not UNSET:
            field_dict["ispOrganization"] = isp_organization
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_i_pv_4_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_pv_4_from = _parse_i_pv_4_from(d.pop("iPv4From", UNSET))


        def _parse_i_pv_4_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_pv_4_to = _parse_i_pv_4_to(d.pop("iPv4To", UNSET))


        def _parse_continent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continent = _parse_continent(d.pop("continent", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))


        def _parse_province(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        province = _parse_province(d.pop("province", UNSET))


        asn = d.pop("asn", UNSET)

        def _parse_asn_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asn_organization = _parse_asn_organization(d.pop("asnOrganization", UNSET))


        def _parse_isp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isp = _parse_isp(d.pop("isp", UNSET))


        def _parse_isp_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isp_organization = _parse_isp_organization(d.pop("ispOrganization", UNSET))


        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        details = d.pop("details", UNSET)

        mt5_geo_record = cls(
            i_pv_4_from=i_pv_4_from,
            i_pv_4_to=i_pv_4_to,
            continent=continent,
            country=country,
            city=city,
            region=region,
            province=province,
            asn=asn,
            asn_organization=asn_organization,
            isp=isp,
            isp_organization=isp_organization,
            latitude=latitude,
            longitude=longitude,
            details=details,
        )

        return mt5_geo_record

