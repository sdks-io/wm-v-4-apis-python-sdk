from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product import Product, ProductDict


class Price(SdkBaseModel):
    """Schema for price info in getPricing response."""

    status: str
    """The status of the operation."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="SellerSKU")
    """The seller stock keeping unit (SKU) of the item."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """The Walmart Item ID of the item."""

    product: Optional[Product] = Field(default=UNSET, alias="Product")
    """An item."""


class PriceDict(TypedDict):
    status: str
    seller_sku: NotRequired[str]
    walmart_item_id: NotRequired[str]
    product: NotRequired[ProductDict]
