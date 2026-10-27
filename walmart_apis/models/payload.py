from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fulfillment_order import FulfillmentOrder, FulfillmentOrderDict
from .fulfillment_order_item import FulfillmentOrderItem, FulfillmentOrderItemDict
from .fulfillment_shipment import FulfillmentShipment, FulfillmentShipmentDict


class Payload(SdkBaseModel):
    fulfillment_order: Optional[FulfillmentOrder] = Field(default=UNSET, alias="fulfillmentOrder")
    fulfillment_order_items: Optional[list[FulfillmentOrderItem]] = Field(default=UNSET, alias="fulfillmentOrderItems")
    fulfillment_shipments: Optional[list[FulfillmentShipment]] = Field(default=UNSET, alias="fulfillmentShipments")


class PayloadDict(TypedDict):
    fulfillment_order: NotRequired[FulfillmentOrderDict]
    fulfillment_order_items: NotRequired[list[FulfillmentOrderItemDict]]
    fulfillment_shipments: NotRequired[list[FulfillmentShipmentDict]]
