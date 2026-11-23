from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.mt5_attachment_info import MT5AttachmentInfo





T = TypeVar("T", bound="MT5Document")



@_attrs_define
class MT5Document:
    """ Client document record — input and output of the document routes.

        Attributes:
            record_id (int | None | Unset): Document identifier. Assigned by the server on creation; sent to address an
                existing document.
            related_client (int | None | Unset): Identifier of the client the document belongs to (required).
            approved_date (datetime.datetime | None | Unset): Date the document was approved.
            approved_by (int | None | Unset): Login of the manager account that approved the document.
            document_type (None | str | Unset): Document type name.<br/>One of: DOCUMENT_TYPE_OTHER, DOCUMENT_TYPE_FIRST,
                DOCUMENT_TYPE_PERSONAL_IDENTITY, DOCUMENT_TYPE_PERSONAL_ADDRESS, DOCUMENT_TYPE_REGISTERED_ADDRESS,
                DOCUMENT_TYPE_DIRECTORS_PASSPORT, DOCUMENT_TYPE_CERTIFICATE_OF_INCORPORATION,
                DOCUMENT_TYPE_CERTIFICATE_OF_DIRECTORS, DOCUMENT_TYPE_CERTIFICATE_OF_GOOD_STANDING, DOCUMENT_TYPE_LAST. Case-
                insensitive; the numeric value is accepted too. Any other value is refused with error code Validation.
            document_subtype (None | str | Unset): Document subtype name.<br/>One of: DOCUMENT_SUBTYPE_OTHER,
                DOCUMENT_SUBTYPE_FIRST, DOCUMENT_SUBTYPE_ID_CARD, DOCUMENT_SUBTYPE_PASSPORT, DOCUMENT_SUBTYPE_DRIVERS,
                DOCUMENT_SUBTYPE_BANK_CARD, DOCUMENT_SUBTYPE_UTILITY_BILL, DOCUMENT_SUBTYPE_BANK_STATEMENT,
                DOCUMENT_SUBTYPE_TAX_STATEMENT, DOCUMENT_SUBTYPE_SELFIE, DOCUMENT_SUBTYPE_PROFILE_IMAGE,
                DOCUMENT_SUBTYPE_ID_DOC_PHOTO, DOCUMENT_SUBTYPE_AGREEMENT, DOCUMENT_SUBTYPE_CONTRACT,
                DOCUMENT_SUBTYPE_RESIDENCE_PERMIT, DOCUMENT_SUBTYPE_EMPLOYMENT_CERTIFICATE,
                DOCUMENT_SUBTYPE_DRIVERS_TRANSLATION, DOCUMENT_SUBTYPE_INVESTOR_DOC, DOCUMENT_SUBTYPE_VEHICLE_REG_CERTIFICATE,
                DOCUMENT_SUBTYPE_INCOME_SOURCE, DOCUMENT_SUBTYPE_PAYMENT_METHOD, DOCUMENT_SUBTYPE_LAST. Case-insensitive; the
                numeric value is accepted too. Any other value is refused with error code Validation.
            document_status (None | str | Unset): Document status name.<br/>One of: DOCUMENT_STATUS_NEW,
                DOCUMENT_STATUS_FIRST, DOCUMENT_STATUS_APPROVED, DOCUMENT_STATUS_REJECTED, DOCUMENT_STATUS_ARCHIVED,
                DOCUMENT_STATUS_DELETED, DOCUMENT_STATUS_LAST. Case-insensitive; the numeric value is accepted too. Any other
                value is refused with error code Validation.
            date_issue (datetime.datetime | None | Unset): Date the document was issued.
            date_expiration (datetime.datetime | None | Unset): Date the document expires.
            document_name (None | str | Unset): File name of the document.
            document_comment (None | str | Unset): Comment on the document.
            attachments (list[MT5AttachmentInfo] | None | Unset): Attachments linked to the document. Read-only: a link is
                created by the attachment routes, and a value
                sent here is ignored.
     """

    record_id: int | None | Unset = UNSET
    related_client: int | None | Unset = UNSET
    approved_date: datetime.datetime | None | Unset = UNSET
    approved_by: int | None | Unset = UNSET
    document_type: None | str | Unset = UNSET
    document_subtype: None | str | Unset = UNSET
    document_status: None | str | Unset = UNSET
    date_issue: datetime.datetime | None | Unset = UNSET
    date_expiration: datetime.datetime | None | Unset = UNSET
    document_name: None | str | Unset = UNSET
    document_comment: None | str | Unset = UNSET
    attachments: list[MT5AttachmentInfo] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_attachment_info import MT5AttachmentInfo
        record_id: int | None | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        related_client: int | None | Unset
        if isinstance(self.related_client, Unset):
            related_client = UNSET
        else:
            related_client = self.related_client

        approved_date: None | str | Unset
        if isinstance(self.approved_date, Unset):
            approved_date = UNSET
        elif isinstance(self.approved_date, datetime.datetime):
            approved_date = self.approved_date.isoformat()
        else:
            approved_date = self.approved_date

        approved_by: int | None | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        document_subtype: None | str | Unset
        if isinstance(self.document_subtype, Unset):
            document_subtype = UNSET
        else:
            document_subtype = self.document_subtype

        document_status: None | str | Unset
        if isinstance(self.document_status, Unset):
            document_status = UNSET
        else:
            document_status = self.document_status

        date_issue: None | str | Unset
        if isinstance(self.date_issue, Unset):
            date_issue = UNSET
        elif isinstance(self.date_issue, datetime.datetime):
            date_issue = self.date_issue.isoformat()
        else:
            date_issue = self.date_issue

        date_expiration: None | str | Unset
        if isinstance(self.date_expiration, Unset):
            date_expiration = UNSET
        elif isinstance(self.date_expiration, datetime.datetime):
            date_expiration = self.date_expiration.isoformat()
        else:
            date_expiration = self.date_expiration

        document_name: None | str | Unset
        if isinstance(self.document_name, Unset):
            document_name = UNSET
        else:
            document_name = self.document_name

        document_comment: None | str | Unset
        if isinstance(self.document_comment, Unset):
            document_comment = UNSET
        else:
            document_comment = self.document_comment

        attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)


        else:
            attachments = self.attachments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if record_id is not UNSET:
            field_dict["recordID"] = record_id
        if related_client is not UNSET:
            field_dict["relatedClient"] = related_client
        if approved_date is not UNSET:
            field_dict["approvedDate"] = approved_date
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if document_subtype is not UNSET:
            field_dict["documentSubtype"] = document_subtype
        if document_status is not UNSET:
            field_dict["documentStatus"] = document_status
        if date_issue is not UNSET:
            field_dict["dateIssue"] = date_issue
        if date_expiration is not UNSET:
            field_dict["dateExpiration"] = date_expiration
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_comment is not UNSET:
            field_dict["documentComment"] = document_comment
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_attachment_info import MT5AttachmentInfo
        d = dict(src_dict)
        def _parse_record_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_id = _parse_record_id(d.pop("recordID", UNSET))


        def _parse_related_client(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        related_client = _parse_related_client(d.pop("relatedClient", UNSET))


        def _parse_approved_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_date_type_0 = datetime.datetime.fromisoformat(data)



                return approved_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_date = _parse_approved_date(d.pop("approvedDate", UNSET))


        def _parse_approved_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        approved_by = _parse_approved_by(d.pop("approvedBy", UNSET))


        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("documentType", UNSET))


        def _parse_document_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_subtype = _parse_document_subtype(d.pop("documentSubtype", UNSET))


        def _parse_document_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_status = _parse_document_status(d.pop("documentStatus", UNSET))


        def _parse_date_issue(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_issue_type_0 = datetime.datetime.fromisoformat(data)



                return date_issue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_issue = _parse_date_issue(d.pop("dateIssue", UNSET))


        def _parse_date_expiration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_expiration_type_0 = datetime.datetime.fromisoformat(data)



                return date_expiration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_expiration = _parse_date_expiration(d.pop("dateExpiration", UNSET))


        def _parse_document_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_name = _parse_document_name(d.pop("documentName", UNSET))


        def _parse_document_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_comment = _parse_document_comment(d.pop("documentComment", UNSET))


        def _parse_attachments(data: object) -> list[MT5AttachmentInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in (_attachments_type_0):
                    attachments_type_0_item = MT5AttachmentInfo.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5AttachmentInfo] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        mt5_document = cls(
            record_id=record_id,
            related_client=related_client,
            approved_date=approved_date,
            approved_by=approved_by,
            document_type=document_type,
            document_subtype=document_subtype,
            document_status=document_status,
            date_issue=date_issue,
            date_expiration=date_expiration,
            document_name=document_name,
            document_comment=document_comment,
            attachments=attachments,
        )

        return mt5_document

