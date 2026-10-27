from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address1(SdkBaseModel):
    name: str
    address_line1: str = Field(alias="addressLine1")
    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    address_line3: Optional[str] = Field(default=UNSET, alias="addressLine3")
    city: str
    county: Optional[str] = UNSET
    district: Optional[str] = UNSET
    state_or_region: str = Field(alias="stateOrRegion")
    municipality: Optional[str] = UNSET
    postal_code: str = Field(alias="postalCode")
    country_code: str = Field(default="US", alias="countryCode")
    phone: Optional[str] = UNSET
    is_commercial_address: Optional[bool] = Field(default=UNSET, alias="isCommercialAddress")


class Address1Dict(TypedDict):
    name: str
    address_line1: str
    address_line2: NotRequired[str]
    address_line3: NotRequired[str]
    city: str
    county: NotRequired[str]
    district: NotRequired[str]
    state_or_region: str
    municipality: NotRequired[str]
    postal_code: str
    country_code: str
    phone: NotRequired[str]
    is_commercial_address: NotRequired[bool]
