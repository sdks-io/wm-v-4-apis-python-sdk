from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GetFulfillmentPreviewItem(SdkBaseModel):
    seller_sku: str = Field(alias="sellerSku")
    quantity: int
    seller_fulfillment_order_item_id: str = Field(alias="sellerFulfillmentOrderItemId")


class GetFulfillmentPreviewItemDict(TypedDict):
    seller_sku: str
    quantity: int
    seller_fulfillment_order_item_id: str
