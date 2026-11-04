from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SellerSkuIdentifier(SdkBaseModel):
    """Walmart Marketplace, seller, and seller SKU identifiers for the item."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """Walmart Marketplace identifier associated with the item."""

    seller_id: str = Field(alias="SellerId")
    """Seller identifier associated with the item."""

    seller_sku: str = Field(alias="SellerSKU")
    """Seller stock keeping unit (SKU) that identifies the item."""


class SellerSkuIdentifierDict(TypedDict):
    marketplace_id: str
    seller_id: str
    seller_sku: str
