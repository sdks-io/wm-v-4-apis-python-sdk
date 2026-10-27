from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CommonDeliveryWindowOption(SdkBaseModel):
    """Contains information pertaining to a delivery window option."""

    availability_type: str = Field(alias="availabilityType")
    """The type of delivery window availability. Values: ``AVAILABLE``, ``BLOCKED``, ``CONGESTED``, ``DISCOUNTED``."""

    delivery_window_option_id: str = Field(alias="deliveryWindowOptionId")
    """Identifier of a delivery window option."""

    end_date: RFC3339DateTime = Field(alias="endDate")
    """The time at which this delivery window option ends. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mmZ``."""

    start_date: RFC3339DateTime = Field(alias="startDate")
    """The time at which this delivery window option starts. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mmZ``."""

    valid_until: RFC3339DateTime = Field(alias="validUntil")
    """The time at which this delivery window option is no longer valid. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mmZ``."""


class CommonDeliveryWindowOptionDict(TypedDict):
    availability_type: str
    delivery_window_option_id: str
    end_date: RFC3339DateTime
    start_date: RFC3339DateTime
    valid_until: RFC3339DateTime
