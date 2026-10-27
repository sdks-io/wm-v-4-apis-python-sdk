from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketplaceShipmentDetails(SdkBaseModel):
    """Marketplace-side shipment context. Renamed from the industry SP-API "vendor-shipment-details" block to be
    vendor-neutral."""

    seller_order_id: Optional[str] = Field(default=UNSET, alias="sellerOrderId")
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    seller_tracking_id: Optional[str] = Field(default=UNSET, alias="sellerTrackingId")


class MarketplaceShipmentDetailsDict(TypedDict):
    seller_order_id: NotRequired[str]
    purchase_order_id: NotRequired[str]
    seller_tracking_id: NotRequired[str]
