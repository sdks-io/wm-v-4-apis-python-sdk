from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_option import FulfillmentOptionOrStr
from .enums.line_status import LineStatusOrStr
from .money import Money, MoneyDict
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class OrderLine(SdkBaseModel):
    """Item, quantity, price, and fulfillment details for a line in a purchase order."""

    line_number: str = Field(alias="lineNumber")
    """Line identifier within the purchase order."""

    seller_sku: str = Field(alias="sellerSku")
    """Seller SKU identifying the item."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart item identifier."""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """Name of the ordered product."""

    quantity: QuantityWithUnit
    """Quantity ordered for this line."""

    item_price: Money = Field(alias="itemPrice")
    """Price of the item on the order line."""

    line_status: Optional[LineStatusOrStr] = Field(default=UNSET, alias="lineStatus")
    """Current status of the order line."""

    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    """Walmart ship node identifier for Walmart Fulfillment Services (WFS) orders."""

    fulfillment_option: Optional[FulfillmentOptionOrStr] = Field(default=UNSET, alias="fulfillmentOption")
    """Fulfillment option associated with the order line."""


class OrderLineDict(TypedDict):
    line_number: str
    seller_sku: str
    walmart_item_id: NotRequired[str]
    product_name: NotRequired[str]
    quantity: QuantityWithUnitDict
    item_price: MoneyDict
    line_status: NotRequired[LineStatusOrStr]
    ship_node: NotRequired[str]
    fulfillment_option: NotRequired[FulfillmentOptionOrStr]
