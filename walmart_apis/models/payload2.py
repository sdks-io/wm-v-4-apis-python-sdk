from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_orders import AddressOrders, AddressOrdersDict


class Payload2(SdkBaseModel):
    """Shipping address for the purchase order. Do not log response bodies containing shipping addresses."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    shipping_address: Optional[AddressOrders] = Field(default=UNSET, alias="shippingAddress")
    """Postal address associated with the order."""


class Payload2Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipping_address: NotRequired[AddressOrdersDict]
