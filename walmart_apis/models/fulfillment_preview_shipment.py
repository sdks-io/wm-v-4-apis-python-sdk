from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class FulfillmentPreviewShipment(SdkBaseModel):
    earliest_ship_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="earliestShipDate")
    latest_ship_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="latestShipDate")
    earliest_arrival_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="earliestArrivalDate")
    latest_arrival_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="latestArrivalDate")
    shipping_notes: Optional[list[str]] = Field(default=UNSET, alias="shippingNotes")


class FulfillmentPreviewShipmentDict(TypedDict):
    earliest_ship_date: NotRequired[RFC3339DateTime]
    latest_ship_date: NotRequired[RFC3339DateTime]
    earliest_arrival_date: NotRequired[RFC3339DateTime]
    latest_arrival_date: NotRequired[RFC3339DateTime]
    shipping_notes: NotRequired[list[str]]
