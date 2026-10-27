from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.shipment_status11 import ShipmentStatus11OrStr


class UpdateShipmentStatusResponse(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    shipment_status: Optional[ShipmentStatus11OrStr] = Field(default=UNSET, alias="shipmentStatus")
    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")


class UpdateShipmentStatusResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipment_status: NotRequired[ShipmentStatus11OrStr]
    updated_at: NotRequired[RFC3339DateTime]
