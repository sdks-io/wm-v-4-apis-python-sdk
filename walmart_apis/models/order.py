from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address_orders import AddressOrders, AddressOrdersDict
from .enums.fulfillment_type import FulfillmentTypeOrStr
from .enums.order_status import OrderStatusOrStr
from .money import Money, MoneyDict
from .order_line import OrderLine, OrderLineDict


class Order(SdkBaseModel):
    """Identifiers, status, fulfillment, pricing, and line details for a purchase order."""

    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """Customer-facing identifier for the order."""

    seller_id: str = Field(alias="sellerId")
    """Identifier of the seller associated with the order."""

    order_status: OrderStatusOrStr = Field(alias="orderStatus")
    """Current status of the order."""

    fulfillment_type: Optional[FulfillmentTypeOrStr] = Field(default=UNSET, alias="fulfillmentType")
    """Type of fulfillment used for the order."""

    purchase_date: RFC3339DateTime = Field(alias="purchaseDate")
    """Date and time when the order was placed, in ISO 8601 format."""

    last_updated_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdatedDate")
    """Date and time when the order was last updated, in ISO 8601 format."""

    order_total: Optional[Money] = Field(default=UNSET, alias="orderTotal")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    shipping_address: Optional[AddressOrders] = Field(default=UNSET, alias="shippingAddress")
    """Postal address associated with the order."""

    order_lines: Optional[list[OrderLine]] = Field(default=UNSET, alias="orderLines")
    """Order lines associated with the purchase order."""


class OrderDict(TypedDict):
    purchase_order_id: str
    customer_order_id: NotRequired[str]
    seller_id: str
    order_status: OrderStatusOrStr
    fulfillment_type: NotRequired[FulfillmentTypeOrStr]
    purchase_date: RFC3339DateTime
    last_updated_date: NotRequired[RFC3339DateTime]
    order_total: NotRequired[MoneyDict]
    shipping_address: NotRequired[AddressOrdersDict]
    order_lines: NotRequired[list[OrderLineDict]]
