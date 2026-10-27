from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonSpdTrackingItemInput(SdkBaseModel):
    """Small Parcel Delivery (SPD) tracking items input information."""

    box_id: str = Field(alias="boxId")
    """The ID provided by Walmart that identifies a given box."""

    tracking_id: str = Field(alias="trackingId")
    """The tracking ID associated with each box in a non-partnered SPD shipment."""


class CommonSpdTrackingItemInputDict(TypedDict):
    box_id: str
    tracking_id: str
