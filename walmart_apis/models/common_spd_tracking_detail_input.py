from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_spd_tracking_item_input import CommonSpdTrackingItemInput, CommonSpdTrackingItemInputDict


class CommonSpdTrackingDetailInput(SdkBaseModel):
    """Contains input information to update SPD tracking information."""

    spd_tracking_items: list[CommonSpdTrackingItemInput] = Field(alias="spdTrackingItems")
    """List of Small Parcel Delivery (SPD) tracking items input."""


class CommonSpdTrackingDetailInputDict(TypedDict):
    spd_tracking_items: list[CommonSpdTrackingItemInputDict]
