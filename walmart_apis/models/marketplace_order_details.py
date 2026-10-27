from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class MarketplaceOrderDetails(SdkBaseModel):
    """Marketplace-side order context for orders originating on the Walmart Marketplace surface. Equivalent in shape to
    industry SP-API's order-details block; renamed to be vendor-neutral."""

    order_id: Optional[str] = Field(default=UNSET, alias="orderId")
    order_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="orderDate")
    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Walmart Purchase Order ID"""


class MarketplaceOrderDetailsDict(TypedDict):
    order_id: NotRequired[str]
    order_date: NotRequired[RFC3339DateTime]
    seller_id: NotRequired[str]
    purchase_order_id: NotRequired[str]
