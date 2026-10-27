from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_ltl_tracking_detail import CommonLtlTrackingDetail, CommonLtlTrackingDetailDict
from .common_spd_tracking_detail import CommonSpdTrackingDetail, CommonSpdTrackingDetailDict


class CommonTrackingDetails(SdkBaseModel):
    """Tracking information for LTL and SPD shipments."""

    ltl_tracking_detail: Optional[CommonLtlTrackingDetail] = Field(default=UNSET, alias="ltlTrackingDetail")
    """Contains information related to Less-Than-Truckload (LTL) shipment tracking."""

    spd_tracking_detail: Optional[CommonSpdTrackingDetail] = Field(default=UNSET, alias="spdTrackingDetail")
    """Contains information related to Small Parcel Delivery (SPD) shipment tracking."""


class CommonTrackingDetailsDict(TypedDict):
    ltl_tracking_detail: NotRequired[CommonLtlTrackingDetailDict]
    spd_tracking_detail: NotRequired[CommonSpdTrackingDetailDict]
