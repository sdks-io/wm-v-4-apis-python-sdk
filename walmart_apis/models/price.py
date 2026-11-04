from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product import Product, ProductDict


class Price(SdkBaseModel):
    """Schema for pricing information returned by the ``getPricing`` operation."""

    status: str
    """Status of the pricing request for the item."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="SellerSKU")
    """Seller stock keeping unit (SKU) that identifies the item."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart Item ID that identifies the item."""

    product: Optional[Product] = Field(default=UNSET, alias="Product")
    """Pricing, offer, identifier, relationship, and sales information for an item."""


class PriceDict(TypedDict):
    status: str
    seller_sku: NotRequired[str]
    walmart_item_id: NotRequired[str]
    product: NotRequired[ProductDict]
