from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_line import OrderLine, OrderLineDict


class Payload1Orders(SdkBaseModel):
    """Payload containing the purchase order ID and line items."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    order_items: Optional[list[OrderLine]] = Field(default=UNSET, alias="orderItems")
    """List of line items associated with the purchase order."""


class Payload1OrdersDict(TypedDict):
    purchase_order_id: NotRequired[str]
    order_items: NotRequired[list[OrderLineDict]]
