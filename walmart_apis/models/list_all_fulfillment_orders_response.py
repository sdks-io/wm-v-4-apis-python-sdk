from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fulfillment_order import FulfillmentOrder, FulfillmentOrderDict


class ListAllFulfillmentOrdersResponse(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    fulfillment_orders: Optional[list[FulfillmentOrder]] = Field(default=UNSET, alias="fulfillmentOrders")


class ListAllFulfillmentOrdersResponseDict(TypedDict):
    next_token: NotRequired[str]
    fulfillment_orders: NotRequired[list[FulfillmentOrderDict]]
