from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.shipment_status1 import ShipmentStatus1OrStr


class UpdateShipmentStatusResponse(SdkBaseModel):
    """Recorded shipment status and timestamp."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    shipment_status: Optional[ShipmentStatus1OrStr] = Field(default=UNSET, alias="shipmentStatus")
    """Shipment status recorded for the specified order lines."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Date and time when the status was updated, in ISO 8601 format."""


class UpdateShipmentStatusResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipment_status: NotRequired[ShipmentStatus1OrStr]
    updated_at: NotRequired[RFC3339DateTime]
