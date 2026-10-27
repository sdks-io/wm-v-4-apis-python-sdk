from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_spd_tracking_item import CommonSpdTrackingItem, CommonSpdTrackingItemDict


class CommonSpdTrackingDetail(SdkBaseModel):
    """Contains information related to Small Parcel Delivery (SPD) shipment tracking."""

    spd_tracking_items: Optional[list[CommonSpdTrackingItem]] = Field(default=UNSET, alias="spdTrackingItems")
    """List of Small Parcel Delivery (SPD) tracking items."""


class CommonSpdTrackingDetailDict(TypedDict):
    spd_tracking_items: NotRequired[list[CommonSpdTrackingItemDict]]
