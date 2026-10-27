from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.order_item_disposition import OrderItemDispositionOrStr


class FulfillmentOrderItem(SdkBaseModel):
    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")
    seller_fulfillment_order_item_id: Optional[str] = Field(default=UNSET, alias="sellerFulfillmentOrderItemId")
    quantity: Optional[int] = UNSET
    order_item_disposition: Optional[OrderItemDispositionOrStr] = Field(default=UNSET, alias="orderItemDisposition")


class FulfillmentOrderItemDict(TypedDict):
    seller_sku: NotRequired[str]
    seller_fulfillment_order_item_id: NotRequired[str]
    quantity: NotRequired[int]
    order_item_disposition: NotRequired[OrderItemDispositionOrStr]
