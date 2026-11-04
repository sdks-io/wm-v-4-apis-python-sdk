from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonDeliveryWindowOption(SdkBaseModel):
    """Contains information pertaining to a delivery window option."""

    availability_type: str = Field(alias="availabilityType")
    """The type of delivery window availability. Values: ``AVAILABLE``, ``BLOCKED``, ``CONGESTED``, ``DISCOUNTED``."""

    delivery_window_option_id: str = Field(alias="deliveryWindowOptionId")
    """Identifier of a delivery window option."""

    end_date: str = Field(alias="endDate")
    """The time at which this delivery window option ends. In ISO 8601 local datetime format with pattern
    ``yyyy-MM-ddTHH:mm``, in the local time of the destination fulfillment center, so it carries no UTC offset."""

    start_date: str = Field(alias="startDate")
    """The time at which this delivery window option starts. In ISO 8601 local datetime format with pattern
    ``yyyy-MM-ddTHH:mm``, in the local time of the destination fulfillment center, so it carries no UTC offset."""

    valid_until: str = Field(alias="validUntil")
    """The time at which this delivery window option is no longer valid. In ISO 8601 local datetime format with pattern
    ``yyyy-MM-ddTHH:mm``, in the local time of the destination fulfillment center, so it carries no UTC offset."""


class CommonDeliveryWindowOptionDict(TypedDict):
    availability_type: str
    delivery_window_option_id: str
    end_date: str
    start_date: str
    valid_until: str
