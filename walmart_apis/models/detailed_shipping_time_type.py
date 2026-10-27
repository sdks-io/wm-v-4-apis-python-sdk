from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.availability_type import AvailabilityTypeOrStr


class DetailedShippingTimeType(SdkBaseModel):
    """The time range in which an item will likely be shipped once an order has been placed."""

    minimum_hours: Optional[int] = Field(default=UNSET, alias="minimumHours")
    """The minimum time, in hours, that the item will likely be shipped after the order has been placed."""

    maximum_hours: Optional[int] = Field(default=UNSET, alias="maximumHours")
    """The maximum time, in hours, that the item will likely be shipped after the order has been placed."""

    available_date: Optional[str] = Field(default=UNSET, alias="availableDate")
    """The date when the item will be available for shipping."""

    availability_type: Optional[AvailabilityTypeOrStr] = Field(default=UNSET, alias="availabilityType")
    """Indicates whether the item is available for shipping now, or on a known or an unknown date in the future."""


class DetailedShippingTimeTypeDict(TypedDict):
    minimum_hours: NotRequired[int]
    maximum_hours: NotRequired[int]
    available_date: NotRequired[str]
    availability_type: NotRequired[AvailabilityTypeOrStr]
