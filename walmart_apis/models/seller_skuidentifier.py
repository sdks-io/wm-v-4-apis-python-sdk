from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SellerSkuidentifier(SdkBaseModel):
    """Schema to identify an item by MarketPlaceId, SellerId, and SellerSKU."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """A marketplace identifier."""

    seller_id: str = Field(alias="SellerId")
    """The seller identifier submitted for the operation."""

    seller_sku: str = Field(alias="SellerSKU")
    """The seller stock keeping unit (SKU) of the item."""


class SellerSkuidentifierDict(TypedDict):
    marketplace_id: str
    seller_id: str
    seller_sku: str
