from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Location(SdkBaseModel):
    city: Optional[str] = UNSET
    state_or_region: Optional[str] = Field(default=UNSET, alias="stateOrRegion")
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")


class LocationDict(TypedDict):
    city: NotRequired[str]
    state_or_region: NotRequired[str]
    country_code: NotRequired[str]
    postal_code: NotRequired[str]
