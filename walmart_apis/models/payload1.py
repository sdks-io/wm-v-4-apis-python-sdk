from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fulfillment_shipment import FulfillmentShipment, FulfillmentShipmentDict


class Payload1(SdkBaseModel):
    fulfillment_shipments: Optional[list[FulfillmentShipment]] = Field(default=UNSET, alias="fulfillmentShipments")


class Payload1Dict(TypedDict):
    fulfillment_shipments: NotRequired[list[FulfillmentShipmentDict]]
