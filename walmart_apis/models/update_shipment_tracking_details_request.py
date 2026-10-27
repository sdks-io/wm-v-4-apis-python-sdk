from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_tracking_details_input import CommonTrackingDetailsInput, CommonTrackingDetailsInputDict


class UpdateShipmentTrackingDetailsRequest(SdkBaseModel):
    """The ``updateShipmentTrackingDetails`` request."""

    tracking_details: CommonTrackingDetailsInput = Field(alias="trackingDetails")
    """Tracking information input for LTL and SPD shipments."""


class UpdateShipmentTrackingDetailsRequestDict(TypedDict):
    tracking_details: CommonTrackingDetailsInputDict
