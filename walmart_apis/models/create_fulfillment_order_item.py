from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateFulfillmentOrderItem(SdkBaseModel):
    seller_sku: str = Field(alias="sellerSku")
    seller_fulfillment_order_item_id: str = Field(alias="sellerFulfillmentOrderItemId")
    quantity: int
    gift_message: Optional[str] = Field(default=UNSET, alias="giftMessage")
    displayable_comment: Optional[str] = Field(default=UNSET, alias="displayableComment")


class CreateFulfillmentOrderItemDict(TypedDict):
    seller_sku: str
    seller_fulfillment_order_item_id: str
    quantity: int
    gift_message: NotRequired[str]
    displayable_comment: NotRequired[str]
