from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.fulfillment_shipment_status import FulfillmentShipmentStatusOrStr


class FulfillmentShipment(SdkBaseModel):
    walmart_shipment_id: Optional[str] = Field(default=UNSET, alias="walmartShipmentId")
    fulfillment_center_id: Optional[str] = Field(default=UNSET, alias="fulfillmentCenterId")
    """Walmart Ship Node ID"""

    fulfillment_shipment_status: Optional[FulfillmentShipmentStatusOrStr] = Field(
        default=UNSET, alias="fulfillmentShipmentStatus"
    )
    shipping_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shippingDate")
    estimated_arrival_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="estimatedArrivalDate")
    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    carrier: Optional[str] = UNSET


class FulfillmentShipmentDict(TypedDict):
    walmart_shipment_id: NotRequired[str]
    fulfillment_center_id: NotRequired[str]
    fulfillment_shipment_status: NotRequired[FulfillmentShipmentStatusOrStr]
    shipping_date: NotRequired[RFC3339DateTime]
    estimated_arrival_date: NotRequired[RFC3339DateTime]
    tracking_number: NotRequired[str]
    carrier: NotRequired[str]
