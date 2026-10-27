from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_line import OrderLine, OrderLineDict


class Payload11(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    order_items: Optional[list[OrderLine]] = Field(default=UNSET, alias="orderItems")


class Payload11Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    order_items: NotRequired[list[OrderLineDict]]
