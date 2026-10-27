from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonAddress(SdkBaseModel):
    """Specific details to identify a place."""

    address_line1: str = Field(alias="addressLine1")
    """Street address information."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Additional street address information."""

    city: str
    """The city."""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """The name of the business."""

    country_code: str = Field(alias="countryCode")
    """The country code in two-character ISO 3166-1 alpha-2 format."""

    district_or_county: Optional[str] = Field(default=UNSET, alias="districtOrCounty")
    """The district or county."""

    email: Optional[str] = UNSET
    """The email address."""

    name: str
    """The name of the individual who is the primary contact."""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The phone number."""

    postal_code: str = Field(alias="postalCode")
    """The postal code."""

    state_or_province_code: Optional[str] = Field(default=UNSET, alias="stateOrProvinceCode")
    """The state or province code."""


class CommonAddressDict(TypedDict):
    address_line1: str
    address_line2: NotRequired[str]
    city: str
    company_name: NotRequired[str]
    country_code: str
    district_or_county: NotRequired[str]
    email: NotRequired[str]
    name: str
    phone_number: NotRequired[str]
    postal_code: str
    state_or_province_code: NotRequired[str]
