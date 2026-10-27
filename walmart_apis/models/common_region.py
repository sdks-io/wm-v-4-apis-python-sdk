from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonRegion(SdkBaseModel):
    """Representation of a location used within the inbounding experience."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """ISO 3166 standard alpha-2 country code."""

    state: Optional[str] = UNSET
    """State."""

    warehouse_id: Optional[str] = Field(default=UNSET, alias="warehouseId")
    """An identifier for a Ship Node."""


class CommonRegionDict(TypedDict):
    country_code: NotRequired[str]
    state: NotRequired[str]
    warehouse_id: NotRequired[str]
