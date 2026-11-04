from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ShipOrderLinesResponse(SdkBaseModel):
    """Shipment confirmation details."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    shipped_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shippedAt")
    """Date and time when the shipment was recorded, in ISO 8601 format."""


class ShipOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipped_at: NotRequired[RFC3339DateTime]
