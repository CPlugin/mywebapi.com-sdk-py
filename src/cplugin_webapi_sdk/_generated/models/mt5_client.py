from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.client_origins import ClientOrigins
from ..models.client_statuses import ClientStatuses
from ..models.client_types import ClientTypes
from ..models.education_level import EducationLevel
from ..models.employment import Employment
from ..models.employment_industry import EmploymentIndustry
from ..models.genders import Genders
from ..models.kyc_statuses import KYCStatuses
from ..models.preferred_communication import PreferredCommunication
from ..models.trading_experience import TradingExperience
from ..models.wealth_source import WealthSource
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MT5Client")



@_attrs_define
class MT5Client:
    """ Client record interface

        Attributes:
            person_name (str): person name
            record_id (int | None | Unset): record id
            client_type (ClientTypes | None | Unset): client type
            client_status (ClientStatuses | None | Unset): client status
            assigned_manager (int | None | Unset): assigned manager
            compliance_approved_by (int | None | Unset): compliance approved by
            compliance_client_category (None | str | Unset): compliance client category
            compliance_date_approval (datetime.datetime | None | Unset): compliance date approval
            compliance_date_termination (datetime.datetime | None | Unset): compliance date termination
            lead_campaign (None | str | Unset): lead campaign
            lead_source (None | str | Unset): lead source
            introducer (None | str | Unset): introducer
            person_title (None | str | Unset): person title
            person_middle_name (None | str | Unset): person middle name
            person_last_name (None | str | Unset): person last name
            person_birth_date (datetime.datetime | None | Unset): person birth date<br />
                The date of birth is specified in the FILETIME format: the number of 100-nanosecond intervals that have elapsed
                since January 1, 1601
            person_citizenship (None | str | Unset): person citizenship
            person_gender (Genders | None | Unset): person gender
            person_tax_id (None | str | Unset): person taxid
            person_document_type (None | str | Unset): person document type
            person_document_number (None | str | Unset): person document number
            person_document_date (datetime.datetime | None | Unset): issue date of the identification document (of passport,
                driver's license, etc.).<br />
                in seconds since 01.01.1970 (UnixTime).
            person_document_extra (None | str | Unset): person document extra
            person_employment (Employment | None | Unset): person employment
            person_industry (EmploymentIndustry | None | Unset): person industry
            person_education (EducationLevel | None | Unset): person education
            person_wealth_source (None | Unset | WealthSource): person wealth source
            person_annual_income (float | None | Unset): person annual income
            person_net_worth (float | None | Unset): person net worth
            person_annual_deposit (float | None | Unset): person annual deposit
            company_name (None | str | Unset): company name
            company_reg_number (None | str | Unset): company registration number
            company_reg_date (datetime.datetime | None | Unset): Company registration date in seconds that elapsed since
                01.01.1970 (UnixTime).
            company_reg_authority (None | str | Unset): company registration authority
            company_vat (None | str | Unset): company VAT
            company_lei (None | str | Unset): company LEI
            company_license_number (None | str | Unset): company license number
            company_license_authority (None | str | Unset): company license authority
            company_country (None | str | Unset): company country
            company_address (None | str | Unset): company address
            company_website (None | str | Unset): company website
            contact_preferred (None | PreferredCommunication | Unset): contact preferred
            contact_language (None | str | Unset): contact language
            contact_email (None | str | Unset): contact email
            contact_phone (None | str | Unset): contact phone
            contact_messengers (None | str | Unset): contact messengers
            contact_social_networks (None | str | Unset): contact social networks
            contact_last_date (datetime.datetime | None | Unset): Contact last date
            address_country (None | str | Unset): address country
            address_postcode (None | str | Unset): address postcode
            address_street (None | str | Unset): address street
            address_state (None | str | Unset): address state
            address_city (None | str | Unset): address city
            experience_fx (None | TradingExperience | Unset): experience of FX
            experience_cfd (None | TradingExperience | Unset): experience of CFD
            experience_futures (None | TradingExperience | Unset): experience of Futures
            experience_stocks (None | TradingExperience | Unset): experience of Stocks
            trading_group (None | str | Unset): trading group
            client_origin (ClientOrigins | None | Unset): client origin
            client_origin_login (int | None | Unset): client origin login
            client_external_id (None | str | Unset): external ID
            person_document_expiration (datetime.datetime | None | Unset): person document expiration date
            kyc_status (KYCStatuses | None | Unset): KYC status
            date_created (datetime.datetime | None | Unset): record creation date
            date_modified (datetime.datetime | None | Unset): record modification date
     """

    person_name: str
    record_id: int | None | Unset = UNSET
    client_type: ClientTypes | None | Unset = UNSET
    client_status: ClientStatuses | None | Unset = UNSET
    assigned_manager: int | None | Unset = UNSET
    compliance_approved_by: int | None | Unset = UNSET
    compliance_client_category: None | str | Unset = UNSET
    compliance_date_approval: datetime.datetime | None | Unset = UNSET
    compliance_date_termination: datetime.datetime | None | Unset = UNSET
    lead_campaign: None | str | Unset = UNSET
    lead_source: None | str | Unset = UNSET
    introducer: None | str | Unset = UNSET
    person_title: None | str | Unset = UNSET
    person_middle_name: None | str | Unset = UNSET
    person_last_name: None | str | Unset = UNSET
    person_birth_date: datetime.datetime | None | Unset = UNSET
    person_citizenship: None | str | Unset = UNSET
    person_gender: Genders | None | Unset = UNSET
    person_tax_id: None | str | Unset = UNSET
    person_document_type: None | str | Unset = UNSET
    person_document_number: None | str | Unset = UNSET
    person_document_date: datetime.datetime | None | Unset = UNSET
    person_document_extra: None | str | Unset = UNSET
    person_employment: Employment | None | Unset = UNSET
    person_industry: EmploymentIndustry | None | Unset = UNSET
    person_education: EducationLevel | None | Unset = UNSET
    person_wealth_source: None | Unset | WealthSource = UNSET
    person_annual_income: float | None | Unset = UNSET
    person_net_worth: float | None | Unset = UNSET
    person_annual_deposit: float | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_reg_number: None | str | Unset = UNSET
    company_reg_date: datetime.datetime | None | Unset = UNSET
    company_reg_authority: None | str | Unset = UNSET
    company_vat: None | str | Unset = UNSET
    company_lei: None | str | Unset = UNSET
    company_license_number: None | str | Unset = UNSET
    company_license_authority: None | str | Unset = UNSET
    company_country: None | str | Unset = UNSET
    company_address: None | str | Unset = UNSET
    company_website: None | str | Unset = UNSET
    contact_preferred: None | PreferredCommunication | Unset = UNSET
    contact_language: None | str | Unset = UNSET
    contact_email: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    contact_messengers: None | str | Unset = UNSET
    contact_social_networks: None | str | Unset = UNSET
    contact_last_date: datetime.datetime | None | Unset = UNSET
    address_country: None | str | Unset = UNSET
    address_postcode: None | str | Unset = UNSET
    address_street: None | str | Unset = UNSET
    address_state: None | str | Unset = UNSET
    address_city: None | str | Unset = UNSET
    experience_fx: None | TradingExperience | Unset = UNSET
    experience_cfd: None | TradingExperience | Unset = UNSET
    experience_futures: None | TradingExperience | Unset = UNSET
    experience_stocks: None | TradingExperience | Unset = UNSET
    trading_group: None | str | Unset = UNSET
    client_origin: ClientOrigins | None | Unset = UNSET
    client_origin_login: int | None | Unset = UNSET
    client_external_id: None | str | Unset = UNSET
    person_document_expiration: datetime.datetime | None | Unset = UNSET
    kyc_status: KYCStatuses | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        person_name = self.person_name

        record_id: int | None | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        client_type: None | str | Unset
        if isinstance(self.client_type, Unset):
            client_type = UNSET
        elif isinstance(self.client_type, ClientTypes):
            client_type = self.client_type.value
        else:
            client_type = self.client_type

        client_status: None | str | Unset
        if isinstance(self.client_status, Unset):
            client_status = UNSET
        elif isinstance(self.client_status, ClientStatuses):
            client_status = self.client_status.value
        else:
            client_status = self.client_status

        assigned_manager: int | None | Unset
        if isinstance(self.assigned_manager, Unset):
            assigned_manager = UNSET
        else:
            assigned_manager = self.assigned_manager

        compliance_approved_by: int | None | Unset
        if isinstance(self.compliance_approved_by, Unset):
            compliance_approved_by = UNSET
        else:
            compliance_approved_by = self.compliance_approved_by

        compliance_client_category: None | str | Unset
        if isinstance(self.compliance_client_category, Unset):
            compliance_client_category = UNSET
        else:
            compliance_client_category = self.compliance_client_category

        compliance_date_approval: None | str | Unset
        if isinstance(self.compliance_date_approval, Unset):
            compliance_date_approval = UNSET
        elif isinstance(self.compliance_date_approval, datetime.datetime):
            compliance_date_approval = self.compliance_date_approval.isoformat()
        else:
            compliance_date_approval = self.compliance_date_approval

        compliance_date_termination: None | str | Unset
        if isinstance(self.compliance_date_termination, Unset):
            compliance_date_termination = UNSET
        elif isinstance(self.compliance_date_termination, datetime.datetime):
            compliance_date_termination = self.compliance_date_termination.isoformat()
        else:
            compliance_date_termination = self.compliance_date_termination

        lead_campaign: None | str | Unset
        if isinstance(self.lead_campaign, Unset):
            lead_campaign = UNSET
        else:
            lead_campaign = self.lead_campaign

        lead_source: None | str | Unset
        if isinstance(self.lead_source, Unset):
            lead_source = UNSET
        else:
            lead_source = self.lead_source

        introducer: None | str | Unset
        if isinstance(self.introducer, Unset):
            introducer = UNSET
        else:
            introducer = self.introducer

        person_title: None | str | Unset
        if isinstance(self.person_title, Unset):
            person_title = UNSET
        else:
            person_title = self.person_title

        person_middle_name: None | str | Unset
        if isinstance(self.person_middle_name, Unset):
            person_middle_name = UNSET
        else:
            person_middle_name = self.person_middle_name

        person_last_name: None | str | Unset
        if isinstance(self.person_last_name, Unset):
            person_last_name = UNSET
        else:
            person_last_name = self.person_last_name

        person_birth_date: None | str | Unset
        if isinstance(self.person_birth_date, Unset):
            person_birth_date = UNSET
        elif isinstance(self.person_birth_date, datetime.datetime):
            person_birth_date = self.person_birth_date.isoformat()
        else:
            person_birth_date = self.person_birth_date

        person_citizenship: None | str | Unset
        if isinstance(self.person_citizenship, Unset):
            person_citizenship = UNSET
        else:
            person_citizenship = self.person_citizenship

        person_gender: None | str | Unset
        if isinstance(self.person_gender, Unset):
            person_gender = UNSET
        elif isinstance(self.person_gender, Genders):
            person_gender = self.person_gender.value
        else:
            person_gender = self.person_gender

        person_tax_id: None | str | Unset
        if isinstance(self.person_tax_id, Unset):
            person_tax_id = UNSET
        else:
            person_tax_id = self.person_tax_id

        person_document_type: None | str | Unset
        if isinstance(self.person_document_type, Unset):
            person_document_type = UNSET
        else:
            person_document_type = self.person_document_type

        person_document_number: None | str | Unset
        if isinstance(self.person_document_number, Unset):
            person_document_number = UNSET
        else:
            person_document_number = self.person_document_number

        person_document_date: None | str | Unset
        if isinstance(self.person_document_date, Unset):
            person_document_date = UNSET
        elif isinstance(self.person_document_date, datetime.datetime):
            person_document_date = self.person_document_date.isoformat()
        else:
            person_document_date = self.person_document_date

        person_document_extra: None | str | Unset
        if isinstance(self.person_document_extra, Unset):
            person_document_extra = UNSET
        else:
            person_document_extra = self.person_document_extra

        person_employment: None | str | Unset
        if isinstance(self.person_employment, Unset):
            person_employment = UNSET
        elif isinstance(self.person_employment, Employment):
            person_employment = self.person_employment.value
        else:
            person_employment = self.person_employment

        person_industry: None | str | Unset
        if isinstance(self.person_industry, Unset):
            person_industry = UNSET
        elif isinstance(self.person_industry, EmploymentIndustry):
            person_industry = self.person_industry.value
        else:
            person_industry = self.person_industry

        person_education: None | str | Unset
        if isinstance(self.person_education, Unset):
            person_education = UNSET
        elif isinstance(self.person_education, EducationLevel):
            person_education = self.person_education.value
        else:
            person_education = self.person_education

        person_wealth_source: None | str | Unset
        if isinstance(self.person_wealth_source, Unset):
            person_wealth_source = UNSET
        elif isinstance(self.person_wealth_source, WealthSource):
            person_wealth_source = self.person_wealth_source.value
        else:
            person_wealth_source = self.person_wealth_source

        person_annual_income: float | None | Unset
        if isinstance(self.person_annual_income, Unset):
            person_annual_income = UNSET
        else:
            person_annual_income = self.person_annual_income

        person_net_worth: float | None | Unset
        if isinstance(self.person_net_worth, Unset):
            person_net_worth = UNSET
        else:
            person_net_worth = self.person_net_worth

        person_annual_deposit: float | None | Unset
        if isinstance(self.person_annual_deposit, Unset):
            person_annual_deposit = UNSET
        else:
            person_annual_deposit = self.person_annual_deposit

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_reg_number: None | str | Unset
        if isinstance(self.company_reg_number, Unset):
            company_reg_number = UNSET
        else:
            company_reg_number = self.company_reg_number

        company_reg_date: None | str | Unset
        if isinstance(self.company_reg_date, Unset):
            company_reg_date = UNSET
        elif isinstance(self.company_reg_date, datetime.datetime):
            company_reg_date = self.company_reg_date.isoformat()
        else:
            company_reg_date = self.company_reg_date

        company_reg_authority: None | str | Unset
        if isinstance(self.company_reg_authority, Unset):
            company_reg_authority = UNSET
        else:
            company_reg_authority = self.company_reg_authority

        company_vat: None | str | Unset
        if isinstance(self.company_vat, Unset):
            company_vat = UNSET
        else:
            company_vat = self.company_vat

        company_lei: None | str | Unset
        if isinstance(self.company_lei, Unset):
            company_lei = UNSET
        else:
            company_lei = self.company_lei

        company_license_number: None | str | Unset
        if isinstance(self.company_license_number, Unset):
            company_license_number = UNSET
        else:
            company_license_number = self.company_license_number

        company_license_authority: None | str | Unset
        if isinstance(self.company_license_authority, Unset):
            company_license_authority = UNSET
        else:
            company_license_authority = self.company_license_authority

        company_country: None | str | Unset
        if isinstance(self.company_country, Unset):
            company_country = UNSET
        else:
            company_country = self.company_country

        company_address: None | str | Unset
        if isinstance(self.company_address, Unset):
            company_address = UNSET
        else:
            company_address = self.company_address

        company_website: None | str | Unset
        if isinstance(self.company_website, Unset):
            company_website = UNSET
        else:
            company_website = self.company_website

        contact_preferred: None | str | Unset
        if isinstance(self.contact_preferred, Unset):
            contact_preferred = UNSET
        elif isinstance(self.contact_preferred, PreferredCommunication):
            contact_preferred = self.contact_preferred.value
        else:
            contact_preferred = self.contact_preferred

        contact_language: None | str | Unset
        if isinstance(self.contact_language, Unset):
            contact_language = UNSET
        else:
            contact_language = self.contact_language

        contact_email: None | str | Unset
        if isinstance(self.contact_email, Unset):
            contact_email = UNSET
        else:
            contact_email = self.contact_email

        contact_phone: None | str | Unset
        if isinstance(self.contact_phone, Unset):
            contact_phone = UNSET
        else:
            contact_phone = self.contact_phone

        contact_messengers: None | str | Unset
        if isinstance(self.contact_messengers, Unset):
            contact_messengers = UNSET
        else:
            contact_messengers = self.contact_messengers

        contact_social_networks: None | str | Unset
        if isinstance(self.contact_social_networks, Unset):
            contact_social_networks = UNSET
        else:
            contact_social_networks = self.contact_social_networks

        contact_last_date: None | str | Unset
        if isinstance(self.contact_last_date, Unset):
            contact_last_date = UNSET
        elif isinstance(self.contact_last_date, datetime.datetime):
            contact_last_date = self.contact_last_date.isoformat()
        else:
            contact_last_date = self.contact_last_date

        address_country: None | str | Unset
        if isinstance(self.address_country, Unset):
            address_country = UNSET
        else:
            address_country = self.address_country

        address_postcode: None | str | Unset
        if isinstance(self.address_postcode, Unset):
            address_postcode = UNSET
        else:
            address_postcode = self.address_postcode

        address_street: None | str | Unset
        if isinstance(self.address_street, Unset):
            address_street = UNSET
        else:
            address_street = self.address_street

        address_state: None | str | Unset
        if isinstance(self.address_state, Unset):
            address_state = UNSET
        else:
            address_state = self.address_state

        address_city: None | str | Unset
        if isinstance(self.address_city, Unset):
            address_city = UNSET
        else:
            address_city = self.address_city

        experience_fx: None | str | Unset
        if isinstance(self.experience_fx, Unset):
            experience_fx = UNSET
        elif isinstance(self.experience_fx, TradingExperience):
            experience_fx = self.experience_fx.value
        else:
            experience_fx = self.experience_fx

        experience_cfd: None | str | Unset
        if isinstance(self.experience_cfd, Unset):
            experience_cfd = UNSET
        elif isinstance(self.experience_cfd, TradingExperience):
            experience_cfd = self.experience_cfd.value
        else:
            experience_cfd = self.experience_cfd

        experience_futures: None | str | Unset
        if isinstance(self.experience_futures, Unset):
            experience_futures = UNSET
        elif isinstance(self.experience_futures, TradingExperience):
            experience_futures = self.experience_futures.value
        else:
            experience_futures = self.experience_futures

        experience_stocks: None | str | Unset
        if isinstance(self.experience_stocks, Unset):
            experience_stocks = UNSET
        elif isinstance(self.experience_stocks, TradingExperience):
            experience_stocks = self.experience_stocks.value
        else:
            experience_stocks = self.experience_stocks

        trading_group: None | str | Unset
        if isinstance(self.trading_group, Unset):
            trading_group = UNSET
        else:
            trading_group = self.trading_group

        client_origin: None | str | Unset
        if isinstance(self.client_origin, Unset):
            client_origin = UNSET
        elif isinstance(self.client_origin, ClientOrigins):
            client_origin = self.client_origin.value
        else:
            client_origin = self.client_origin

        client_origin_login: int | None | Unset
        if isinstance(self.client_origin_login, Unset):
            client_origin_login = UNSET
        else:
            client_origin_login = self.client_origin_login

        client_external_id: None | str | Unset
        if isinstance(self.client_external_id, Unset):
            client_external_id = UNSET
        else:
            client_external_id = self.client_external_id

        person_document_expiration: None | str | Unset
        if isinstance(self.person_document_expiration, Unset):
            person_document_expiration = UNSET
        elif isinstance(self.person_document_expiration, datetime.datetime):
            person_document_expiration = self.person_document_expiration.isoformat()
        else:
            person_document_expiration = self.person_document_expiration

        kyc_status: None | str | Unset
        if isinstance(self.kyc_status, Unset):
            kyc_status = UNSET
        elif isinstance(self.kyc_status, KYCStatuses):
            kyc_status = self.kyc_status.value
        else:
            kyc_status = self.kyc_status

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "personName": person_name,
        })
        if record_id is not UNSET:
            field_dict["recordID"] = record_id
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if client_status is not UNSET:
            field_dict["clientStatus"] = client_status
        if assigned_manager is not UNSET:
            field_dict["assignedManager"] = assigned_manager
        if compliance_approved_by is not UNSET:
            field_dict["complianceApprovedBy"] = compliance_approved_by
        if compliance_client_category is not UNSET:
            field_dict["complianceClientCategory"] = compliance_client_category
        if compliance_date_approval is not UNSET:
            field_dict["complianceDateApproval"] = compliance_date_approval
        if compliance_date_termination is not UNSET:
            field_dict["complianceDateTermination"] = compliance_date_termination
        if lead_campaign is not UNSET:
            field_dict["leadCampaign"] = lead_campaign
        if lead_source is not UNSET:
            field_dict["leadSource"] = lead_source
        if introducer is not UNSET:
            field_dict["introducer"] = introducer
        if person_title is not UNSET:
            field_dict["personTitle"] = person_title
        if person_middle_name is not UNSET:
            field_dict["personMiddleName"] = person_middle_name
        if person_last_name is not UNSET:
            field_dict["personLastName"] = person_last_name
        if person_birth_date is not UNSET:
            field_dict["personBirthDate"] = person_birth_date
        if person_citizenship is not UNSET:
            field_dict["personCitizenship"] = person_citizenship
        if person_gender is not UNSET:
            field_dict["personGender"] = person_gender
        if person_tax_id is not UNSET:
            field_dict["personTaxID"] = person_tax_id
        if person_document_type is not UNSET:
            field_dict["personDocumentType"] = person_document_type
        if person_document_number is not UNSET:
            field_dict["personDocumentNumber"] = person_document_number
        if person_document_date is not UNSET:
            field_dict["personDocumentDate"] = person_document_date
        if person_document_extra is not UNSET:
            field_dict["personDocumentExtra"] = person_document_extra
        if person_employment is not UNSET:
            field_dict["personEmployment"] = person_employment
        if person_industry is not UNSET:
            field_dict["personIndustry"] = person_industry
        if person_education is not UNSET:
            field_dict["personEducation"] = person_education
        if person_wealth_source is not UNSET:
            field_dict["personWealthSource"] = person_wealth_source
        if person_annual_income is not UNSET:
            field_dict["personAnnualIncome"] = person_annual_income
        if person_net_worth is not UNSET:
            field_dict["personNetWorth"] = person_net_worth
        if person_annual_deposit is not UNSET:
            field_dict["personAnnualDeposit"] = person_annual_deposit
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_reg_number is not UNSET:
            field_dict["companyRegNumber"] = company_reg_number
        if company_reg_date is not UNSET:
            field_dict["companyRegDate"] = company_reg_date
        if company_reg_authority is not UNSET:
            field_dict["companyRegAuthority"] = company_reg_authority
        if company_vat is not UNSET:
            field_dict["companyVAT"] = company_vat
        if company_lei is not UNSET:
            field_dict["companyLEI"] = company_lei
        if company_license_number is not UNSET:
            field_dict["companyLicenseNumber"] = company_license_number
        if company_license_authority is not UNSET:
            field_dict["companyLicenseAuthority"] = company_license_authority
        if company_country is not UNSET:
            field_dict["companyCountry"] = company_country
        if company_address is not UNSET:
            field_dict["companyAddress"] = company_address
        if company_website is not UNSET:
            field_dict["companyWebsite"] = company_website
        if contact_preferred is not UNSET:
            field_dict["contactPreferred"] = contact_preferred
        if contact_language is not UNSET:
            field_dict["contactLanguage"] = contact_language
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if contact_messengers is not UNSET:
            field_dict["contactMessengers"] = contact_messengers
        if contact_social_networks is not UNSET:
            field_dict["contactSocialNetworks"] = contact_social_networks
        if contact_last_date is not UNSET:
            field_dict["contactLastDate"] = contact_last_date
        if address_country is not UNSET:
            field_dict["addressCountry"] = address_country
        if address_postcode is not UNSET:
            field_dict["addressPostcode"] = address_postcode
        if address_street is not UNSET:
            field_dict["addressStreet"] = address_street
        if address_state is not UNSET:
            field_dict["addressState"] = address_state
        if address_city is not UNSET:
            field_dict["addressCity"] = address_city
        if experience_fx is not UNSET:
            field_dict["experienceFX"] = experience_fx
        if experience_cfd is not UNSET:
            field_dict["experienceCFD"] = experience_cfd
        if experience_futures is not UNSET:
            field_dict["experienceFutures"] = experience_futures
        if experience_stocks is not UNSET:
            field_dict["experienceStocks"] = experience_stocks
        if trading_group is not UNSET:
            field_dict["tradingGroup"] = trading_group
        if client_origin is not UNSET:
            field_dict["clientOrigin"] = client_origin
        if client_origin_login is not UNSET:
            field_dict["clientOriginLogin"] = client_origin_login
        if client_external_id is not UNSET:
            field_dict["clientExternalID"] = client_external_id
        if person_document_expiration is not UNSET:
            field_dict["personDocumentExpiration"] = person_document_expiration
        if kyc_status is not UNSET:
            field_dict["kycStatus"] = kyc_status
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_name = d.pop("personName")

        def _parse_record_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_id = _parse_record_id(d.pop("recordID", UNSET))


        def _parse_client_type(data: object) -> ClientTypes | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_type_type_1 = ClientTypes(data)



                return client_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClientTypes | None | Unset, data)

        client_type = _parse_client_type(d.pop("clientType", UNSET))


        def _parse_client_status(data: object) -> ClientStatuses | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_status_type_1 = ClientStatuses(data)



                return client_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClientStatuses | None | Unset, data)

        client_status = _parse_client_status(d.pop("clientStatus", UNSET))


        def _parse_assigned_manager(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assigned_manager = _parse_assigned_manager(d.pop("assignedManager", UNSET))


        def _parse_compliance_approved_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_approved_by = _parse_compliance_approved_by(d.pop("complianceApprovedBy", UNSET))


        def _parse_compliance_client_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compliance_client_category = _parse_compliance_client_category(d.pop("complianceClientCategory", UNSET))


        def _parse_compliance_date_approval(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compliance_date_approval_type_0 = datetime.datetime.fromisoformat(data)



                return compliance_date_approval_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        compliance_date_approval = _parse_compliance_date_approval(d.pop("complianceDateApproval", UNSET))


        def _parse_compliance_date_termination(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compliance_date_termination_type_0 = datetime.datetime.fromisoformat(data)



                return compliance_date_termination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        compliance_date_termination = _parse_compliance_date_termination(d.pop("complianceDateTermination", UNSET))


        def _parse_lead_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_campaign = _parse_lead_campaign(d.pop("leadCampaign", UNSET))


        def _parse_lead_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_source = _parse_lead_source(d.pop("leadSource", UNSET))


        def _parse_introducer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        introducer = _parse_introducer(d.pop("introducer", UNSET))


        def _parse_person_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_title = _parse_person_title(d.pop("personTitle", UNSET))


        def _parse_person_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_middle_name = _parse_person_middle_name(d.pop("personMiddleName", UNSET))


        def _parse_person_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_last_name = _parse_person_last_name(d.pop("personLastName", UNSET))


        def _parse_person_birth_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_birth_date_type_0 = datetime.datetime.fromisoformat(data)



                return person_birth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        person_birth_date = _parse_person_birth_date(d.pop("personBirthDate", UNSET))


        def _parse_person_citizenship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_citizenship = _parse_person_citizenship(d.pop("personCitizenship", UNSET))


        def _parse_person_gender(data: object) -> Genders | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_gender_type_1 = Genders(data)



                return person_gender_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Genders | None | Unset, data)

        person_gender = _parse_person_gender(d.pop("personGender", UNSET))


        def _parse_person_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_tax_id = _parse_person_tax_id(d.pop("personTaxID", UNSET))


        def _parse_person_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_document_type = _parse_person_document_type(d.pop("personDocumentType", UNSET))


        def _parse_person_document_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_document_number = _parse_person_document_number(d.pop("personDocumentNumber", UNSET))


        def _parse_person_document_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_document_date_type_0 = datetime.datetime.fromisoformat(data)



                return person_document_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        person_document_date = _parse_person_document_date(d.pop("personDocumentDate", UNSET))


        def _parse_person_document_extra(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_document_extra = _parse_person_document_extra(d.pop("personDocumentExtra", UNSET))


        def _parse_person_employment(data: object) -> Employment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_employment_type_1 = Employment(data)



                return person_employment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Employment | None | Unset, data)

        person_employment = _parse_person_employment(d.pop("personEmployment", UNSET))


        def _parse_person_industry(data: object) -> EmploymentIndustry | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_industry_type_1 = EmploymentIndustry(data)



                return person_industry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmploymentIndustry | None | Unset, data)

        person_industry = _parse_person_industry(d.pop("personIndustry", UNSET))


        def _parse_person_education(data: object) -> EducationLevel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_education_type_1 = EducationLevel(data)



                return person_education_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EducationLevel | None | Unset, data)

        person_education = _parse_person_education(d.pop("personEducation", UNSET))


        def _parse_person_wealth_source(data: object) -> None | Unset | WealthSource:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_wealth_source_type_1 = WealthSource(data)



                return person_wealth_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WealthSource, data)

        person_wealth_source = _parse_person_wealth_source(d.pop("personWealthSource", UNSET))


        def _parse_person_annual_income(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        person_annual_income = _parse_person_annual_income(d.pop("personAnnualIncome", UNSET))


        def _parse_person_net_worth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        person_net_worth = _parse_person_net_worth(d.pop("personNetWorth", UNSET))


        def _parse_person_annual_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        person_annual_deposit = _parse_person_annual_deposit(d.pop("personAnnualDeposit", UNSET))


        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_company_reg_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_reg_number = _parse_company_reg_number(d.pop("companyRegNumber", UNSET))


        def _parse_company_reg_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_reg_date_type_0 = datetime.datetime.fromisoformat(data)



                return company_reg_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        company_reg_date = _parse_company_reg_date(d.pop("companyRegDate", UNSET))


        def _parse_company_reg_authority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_reg_authority = _parse_company_reg_authority(d.pop("companyRegAuthority", UNSET))


        def _parse_company_vat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_vat = _parse_company_vat(d.pop("companyVAT", UNSET))


        def _parse_company_lei(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_lei = _parse_company_lei(d.pop("companyLEI", UNSET))


        def _parse_company_license_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_license_number = _parse_company_license_number(d.pop("companyLicenseNumber", UNSET))


        def _parse_company_license_authority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_license_authority = _parse_company_license_authority(d.pop("companyLicenseAuthority", UNSET))


        def _parse_company_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_country = _parse_company_country(d.pop("companyCountry", UNSET))


        def _parse_company_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address = _parse_company_address(d.pop("companyAddress", UNSET))


        def _parse_company_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_website = _parse_company_website(d.pop("companyWebsite", UNSET))


        def _parse_contact_preferred(data: object) -> None | PreferredCommunication | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_preferred_type_1 = PreferredCommunication(data)



                return contact_preferred_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PreferredCommunication | Unset, data)

        contact_preferred = _parse_contact_preferred(d.pop("contactPreferred", UNSET))


        def _parse_contact_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_language = _parse_contact_language(d.pop("contactLanguage", UNSET))


        def _parse_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_email = _parse_contact_email(d.pop("contactEmail", UNSET))


        def _parse_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone = _parse_contact_phone(d.pop("contactPhone", UNSET))


        def _parse_contact_messengers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_messengers = _parse_contact_messengers(d.pop("contactMessengers", UNSET))


        def _parse_contact_social_networks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_social_networks = _parse_contact_social_networks(d.pop("contactSocialNetworks", UNSET))


        def _parse_contact_last_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_last_date_type_0 = datetime.datetime.fromisoformat(data)



                return contact_last_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        contact_last_date = _parse_contact_last_date(d.pop("contactLastDate", UNSET))


        def _parse_address_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_country = _parse_address_country(d.pop("addressCountry", UNSET))


        def _parse_address_postcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_postcode = _parse_address_postcode(d.pop("addressPostcode", UNSET))


        def _parse_address_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_street = _parse_address_street(d.pop("addressStreet", UNSET))


        def _parse_address_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_state = _parse_address_state(d.pop("addressState", UNSET))


        def _parse_address_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_city = _parse_address_city(d.pop("addressCity", UNSET))


        def _parse_experience_fx(data: object) -> None | TradingExperience | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experience_fx_type_1 = TradingExperience(data)



                return experience_fx_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradingExperience | Unset, data)

        experience_fx = _parse_experience_fx(d.pop("experienceFX", UNSET))


        def _parse_experience_cfd(data: object) -> None | TradingExperience | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experience_cfd_type_1 = TradingExperience(data)



                return experience_cfd_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradingExperience | Unset, data)

        experience_cfd = _parse_experience_cfd(d.pop("experienceCFD", UNSET))


        def _parse_experience_futures(data: object) -> None | TradingExperience | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experience_futures_type_1 = TradingExperience(data)



                return experience_futures_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradingExperience | Unset, data)

        experience_futures = _parse_experience_futures(d.pop("experienceFutures", UNSET))


        def _parse_experience_stocks(data: object) -> None | TradingExperience | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experience_stocks_type_1 = TradingExperience(data)



                return experience_stocks_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradingExperience | Unset, data)

        experience_stocks = _parse_experience_stocks(d.pop("experienceStocks", UNSET))


        def _parse_trading_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trading_group = _parse_trading_group(d.pop("tradingGroup", UNSET))


        def _parse_client_origin(data: object) -> ClientOrigins | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_origin_type_1 = ClientOrigins(data)



                return client_origin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClientOrigins | None | Unset, data)

        client_origin = _parse_client_origin(d.pop("clientOrigin", UNSET))


        def _parse_client_origin_login(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_origin_login = _parse_client_origin_login(d.pop("clientOriginLogin", UNSET))


        def _parse_client_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_external_id = _parse_client_external_id(d.pop("clientExternalID", UNSET))


        def _parse_person_document_expiration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_document_expiration_type_0 = datetime.datetime.fromisoformat(data)



                return person_document_expiration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        person_document_expiration = _parse_person_document_expiration(d.pop("personDocumentExpiration", UNSET))


        def _parse_kyc_status(data: object) -> KYCStatuses | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kyc_status_type_1 = KYCStatuses(data)



                return kyc_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KYCStatuses | None | Unset, data)

        kyc_status = _parse_kyc_status(d.pop("kycStatus", UNSET))


        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)



                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("dateCreated", UNSET))


        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)



                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("dateModified", UNSET))


        mt5_client = cls(
            person_name=person_name,
            record_id=record_id,
            client_type=client_type,
            client_status=client_status,
            assigned_manager=assigned_manager,
            compliance_approved_by=compliance_approved_by,
            compliance_client_category=compliance_client_category,
            compliance_date_approval=compliance_date_approval,
            compliance_date_termination=compliance_date_termination,
            lead_campaign=lead_campaign,
            lead_source=lead_source,
            introducer=introducer,
            person_title=person_title,
            person_middle_name=person_middle_name,
            person_last_name=person_last_name,
            person_birth_date=person_birth_date,
            person_citizenship=person_citizenship,
            person_gender=person_gender,
            person_tax_id=person_tax_id,
            person_document_type=person_document_type,
            person_document_number=person_document_number,
            person_document_date=person_document_date,
            person_document_extra=person_document_extra,
            person_employment=person_employment,
            person_industry=person_industry,
            person_education=person_education,
            person_wealth_source=person_wealth_source,
            person_annual_income=person_annual_income,
            person_net_worth=person_net_worth,
            person_annual_deposit=person_annual_deposit,
            company_name=company_name,
            company_reg_number=company_reg_number,
            company_reg_date=company_reg_date,
            company_reg_authority=company_reg_authority,
            company_vat=company_vat,
            company_lei=company_lei,
            company_license_number=company_license_number,
            company_license_authority=company_license_authority,
            company_country=company_country,
            company_address=company_address,
            company_website=company_website,
            contact_preferred=contact_preferred,
            contact_language=contact_language,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_messengers=contact_messengers,
            contact_social_networks=contact_social_networks,
            contact_last_date=contact_last_date,
            address_country=address_country,
            address_postcode=address_postcode,
            address_street=address_street,
            address_state=address_state,
            address_city=address_city,
            experience_fx=experience_fx,
            experience_cfd=experience_cfd,
            experience_futures=experience_futures,
            experience_stocks=experience_stocks,
            trading_group=trading_group,
            client_origin=client_origin,
            client_origin_login=client_origin_login,
            client_external_id=client_external_id,
            person_document_expiration=person_document_expiration,
            kyc_status=kyc_status,
            date_created=date_created,
            date_modified=date_modified,
        )

        return mt5_client

