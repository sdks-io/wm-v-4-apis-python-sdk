from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.availability_type import AvailabilityTypeOrStr


class DetailedShippingTimeType(SdkBaseModel):
    """Estimated time range in which an item is likely to ship after an order is placed."""

    minimum_hours: Optional[int] = Field(default=UNSET, alias="minimumHours")
    """Minimum estimated time, in hours, until the item is likely to ship after the order is placed."""

    maximum_hours: Optional[int] = Field(default=UNSET, alias="maximumHours")
    """Maximum estimated time, in hours, until the item is likely to ship after the order is placed."""

    available_date: Optional[str] = Field(default=UNSET, alias="availableDate")
    """Date when the item will be available for shipping."""

    availability_type: Optional[AvailabilityTypeOrStr] = Field(default=UNSET, alias="availabilityType")
    """Indicates whether the item is available for shipping now, on a known future date, or on an unspecified future
    date."""


class DetailedShippingTimeTypeDict(TypedDict):
    minimum_hours: NotRequired[int]
    maximum_hours: NotRequired[int]
    available_date: NotRequired[str]
    availability_type: NotRequired[AvailabilityTypeOrStr]
