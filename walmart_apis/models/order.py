from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address2 import Address2, Address2Dict
from .enums.fulfillment_type import FulfillmentTypeOrStr
from .enums.order_status import OrderStatusOrStr
from .money import Money, MoneyDict
from .order_line import OrderLine, OrderLineDict


class Order(SdkBaseModel):
    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Walmart-assigned Purchase Order ID"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """Customer-facing order reference"""

    seller_id: str = Field(alias="sellerId")
    order_status: OrderStatusOrStr = Field(alias="orderStatus")
    fulfillment_type: Optional[FulfillmentTypeOrStr] = Field(default=UNSET, alias="fulfillmentType")
    purchase_date: RFC3339DateTime = Field(alias="purchaseDate")
    last_updated_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdatedDate")
    order_total: Optional[Money] = Field(default=UNSET, alias="orderTotal")
    shipping_address: Optional[Address2] = Field(default=UNSET, alias="shippingAddress")
    order_lines: Optional[list[OrderLine]] = Field(default=UNSET, alias="orderLines")


class OrderDict(TypedDict):
    purchase_order_id: str
    customer_order_id: NotRequired[str]
    seller_id: str
    order_status: OrderStatusOrStr
    fulfillment_type: NotRequired[FulfillmentTypeOrStr]
    purchase_date: RFC3339DateTime
    last_updated_date: NotRequired[RFC3339DateTime]
    order_total: NotRequired[MoneyDict]
    shipping_address: NotRequired[Address2Dict]
    order_lines: NotRequired[list[OrderLineDict]]
