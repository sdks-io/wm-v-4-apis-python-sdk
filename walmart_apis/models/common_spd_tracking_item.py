from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonSpdTrackingItem(SdkBaseModel):
    """Contains information used to track and identify a Small Parcel Delivery (SPD) item."""

    box_id: Optional[str] = Field(default=UNSET, alias="boxId")
    """The ID provided by Walmart that identifies a given box."""

    tracking_id: Optional[str] = Field(default=UNSET, alias="trackingId")
    """The tracking ID associated with each box in a non-partnered SPD shipment."""

    tracking_number_validation_status: Optional[str] = Field(default=UNSET, alias="trackingNumberValidationStatus")
    """Indicates whether Walmart has validated the tracking number. Possible values: ``VALIDATED``, ``NOT_VALIDATED``,
    ``NOT_SUPPORTED``."""


class CommonSpdTrackingItemDict(TypedDict):
    box_id: NotRequired[str]
    tracking_id: NotRequired[str]
    tracking_number_validation_status: NotRequired[str]
