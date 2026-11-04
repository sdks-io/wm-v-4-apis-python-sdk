from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddressShippingManagement(SdkBaseModel):
    """A postal address. Canonical shared shape -- see com.walmart.seller.core.model.Address's Javadoc (seller-api-core)
    for the full rationale and per-field examples."""

    address_line1: Optional[str] = Field(default=UNSET, alias="addressLine1")
    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    address_line3: Optional[str] = Field(default=UNSET, alias="addressLine3")
    """Third address line."""

    city: Optional[str] = UNSET
    state_or_region: Optional[str] = Field(default=UNSET, alias="stateOrRegion")
    """State, province, or region. Free-form text to accommodate different naming conventions across countries."""

    county: Optional[str] = UNSET
    """County."""

    district: Optional[str] = UNSET
    """District."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """ISO country code."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    telephone_no: Optional[str] = Field(default=UNSET, alias="telephoneNo")
    """Contact phone number."""


class AddressShippingManagementDict(TypedDict):
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    address_line3: NotRequired[str]
    city: NotRequired[str]
    state_or_region: NotRequired[str]
    county: NotRequired[str]
    district: NotRequired[str]
    country_code: NotRequired[str]
    postal_code: NotRequired[str]
    telephone_no: NotRequired[str]
