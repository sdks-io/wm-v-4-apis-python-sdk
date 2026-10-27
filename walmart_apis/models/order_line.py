from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_option import FulfillmentOptionOrStr
from .enums.line_status import LineStatusOrStr
from .money import Money, MoneyDict
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class OrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    seller_sku: str = Field(alias="sellerSku")
    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    quantity: QuantityWithUnit
    item_price: Money = Field(alias="itemPrice")
    line_status: Optional[LineStatusOrStr] = Field(default=UNSET, alias="lineStatus")
    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    """Walmart Ship Node identifier for WFS orders"""

    fulfillment_option: Optional[FulfillmentOptionOrStr] = Field(default=UNSET, alias="fulfillmentOption")


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
