from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateFulfillmentOrderResponse(SdkBaseModel):
    seller_fulfillment_order_id: Optional[str] = Field(default=UNSET, alias="sellerFulfillmentOrderId")


class UpdateFulfillmentOrderResponseDict(TypedDict):
    seller_fulfillment_order_id: NotRequired[str]
