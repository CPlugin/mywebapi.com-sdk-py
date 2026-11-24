from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Certificate")



@_attrs_define
class MT5Certificate:
    """ Certificate issued to a trading account under an extended authorization mode.

        Attributes:
            serial_number (int | Unset): Serial number of the certificate.
            valid_from (datetime.datetime | None | Unset): Start of the validity period, or `null` when the certificate is
                not opened.
            valid_to (datetime.datetime | None | Unset): End of the validity period, or `null` when the certificate is not
                opened.
            name_common (None | str | Unset): Common name (CN) of the certificate subject.
            name_issuer (None | str | Unset): Common name (CN) of the issuing authority.
            name_organization (None | str | Unset): Organization (O) of the certificate subject.
            name_organization_unit (None | str | Unset): Organizational unit (OU) of the certificate subject.
            name_given (None | str | Unset): Given name of the certificate subject.
            is_root (bool | Unset): Whether the certificate is a root certificate of a certification authority.
            is_ca (bool | Unset): Whether the certificate belongs to a certification authority.
            is_opened (bool | Unset): Whether the stored blob could be parsed as a certificate.
            raw_size (int | Unset): Size of the stored certificate blob in bytes.
     """

    serial_number: int | Unset = UNSET
    valid_from: datetime.datetime | None | Unset = UNSET
    valid_to: datetime.datetime | None | Unset = UNSET
    name_common: None | str | Unset = UNSET
    name_issuer: None | str | Unset = UNSET
    name_organization: None | str | Unset = UNSET
    name_organization_unit: None | str | Unset = UNSET
    name_given: None | str | Unset = UNSET
    is_root: bool | Unset = UNSET
    is_ca: bool | Unset = UNSET
    is_opened: bool | Unset = UNSET
    raw_size: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        serial_number = self.serial_number

        valid_from: None | str | Unset
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        elif isinstance(self.valid_from, datetime.datetime):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from

        valid_to: None | str | Unset
        if isinstance(self.valid_to, Unset):
            valid_to = UNSET
        elif isinstance(self.valid_to, datetime.datetime):
            valid_to = self.valid_to.isoformat()
        else:
            valid_to = self.valid_to

        name_common: None | str | Unset
        if isinstance(self.name_common, Unset):
            name_common = UNSET
        else:
            name_common = self.name_common

        name_issuer: None | str | Unset
        if isinstance(self.name_issuer, Unset):
            name_issuer = UNSET
        else:
            name_issuer = self.name_issuer

        name_organization: None | str | Unset
        if isinstance(self.name_organization, Unset):
            name_organization = UNSET
        else:
            name_organization = self.name_organization

        name_organization_unit: None | str | Unset
        if isinstance(self.name_organization_unit, Unset):
            name_organization_unit = UNSET
        else:
            name_organization_unit = self.name_organization_unit

        name_given: None | str | Unset
        if isinstance(self.name_given, Unset):
            name_given = UNSET
        else:
            name_given = self.name_given

        is_root = self.is_root

        is_ca = self.is_ca

        is_opened = self.is_opened

        raw_size = self.raw_size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if name_common is not UNSET:
            field_dict["nameCommon"] = name_common
        if name_issuer is not UNSET:
            field_dict["nameIssuer"] = name_issuer
        if name_organization is not UNSET:
            field_dict["nameOrganization"] = name_organization
        if name_organization_unit is not UNSET:
            field_dict["nameOrganizationUnit"] = name_organization_unit
        if name_given is not UNSET:
            field_dict["nameGiven"] = name_given
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root
        if is_ca is not UNSET:
            field_dict["isCA"] = is_ca
        if is_opened is not UNSET:
            field_dict["isOpened"] = is_opened
        if raw_size is not UNSET:
            field_dict["rawSize"] = raw_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        serial_number = d.pop("serialNumber", UNSET)

        def _parse_valid_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = datetime.datetime.fromisoformat(data)



                return valid_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_from = _parse_valid_from(d.pop("validFrom", UNSET))


        def _parse_valid_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_to_type_0 = datetime.datetime.fromisoformat(data)



                return valid_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_to = _parse_valid_to(d.pop("validTo", UNSET))


        def _parse_name_common(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_common = _parse_name_common(d.pop("nameCommon", UNSET))


        def _parse_name_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_issuer = _parse_name_issuer(d.pop("nameIssuer", UNSET))


        def _parse_name_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_organization = _parse_name_organization(d.pop("nameOrganization", UNSET))


        def _parse_name_organization_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_organization_unit = _parse_name_organization_unit(d.pop("nameOrganizationUnit", UNSET))


        def _parse_name_given(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_given = _parse_name_given(d.pop("nameGiven", UNSET))


        is_root = d.pop("isRoot", UNSET)

        is_ca = d.pop("isCA", UNSET)

        is_opened = d.pop("isOpened", UNSET)

        raw_size = d.pop("rawSize", UNSET)

        mt5_certificate = cls(
            serial_number=serial_number,
            valid_from=valid_from,
            valid_to=valid_to,
            name_common=name_common,
            name_issuer=name_issuer,
            name_organization=name_organization,
            name_organization_unit=name_organization_unit,
            name_given=name_given,
            is_root=is_root,
            is_ca=is_ca,
            is_opened=is_opened,
            raw_size=raw_size,
        )

        return mt5_certificate

