from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address2(SdkBaseModel):
    name: Optional[str] = UNSET
    address_line1: Optional[str] = Field(default=UNSET, alias="addressLine1")
    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    country: str = "US"


class Address2Dict(TypedDict):
    name: NotRequired[str]
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]
