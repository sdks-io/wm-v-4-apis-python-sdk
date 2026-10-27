from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address(SdkBaseModel):
    name: str
    address_line1: str = Field(alias="addressLine1")
    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    city: str
    state_or_region: str = Field(alias="stateOrRegion")
    postal_code: str = Field(alias="postalCode")
    country_code: str = Field(default="US", alias="countryCode")
    phone: Optional[str] = UNSET


class AddressDict(TypedDict):
    name: str
    address_line1: str
    address_line2: NotRequired[str]
    city: str
    state_or_region: str
    postal_code: str
    country_code: str
    phone: NotRequired[str]
