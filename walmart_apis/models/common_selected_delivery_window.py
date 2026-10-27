from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CommonSelectedDeliveryWindow(SdkBaseModel):
    """Selected delivery window attributes."""

    availability_type: str = Field(alias="availabilityType")
    """The type of delivery window availability. Values: ``AVAILABLE``, ``BLOCKED``, ``CONGESTED``, ``DISCOUNTED``."""

    delivery_window_option_id: str = Field(alias="deliveryWindowOptionId")
    """Identifier of a delivery window option."""

    editable_until: Optional[RFC3339DateTime] = Field(default=UNSET, alias="editableUntil")
    """The timestamp at which this window can no longer be edited."""

    end_date: RFC3339DateTime = Field(alias="endDate")
    """The end timestamp of the window."""

    start_date: RFC3339DateTime = Field(alias="startDate")
    """The start timestamp of the window."""


class CommonSelectedDeliveryWindowDict(TypedDict):
    availability_type: str
    delivery_window_option_id: str
    editable_until: NotRequired[RFC3339DateTime]
    end_date: RFC3339DateTime
    start_date: RFC3339DateTime
