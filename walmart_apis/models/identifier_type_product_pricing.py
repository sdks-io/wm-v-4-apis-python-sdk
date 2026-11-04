from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .seller_sku_identifier import SellerSkuIdentifier, SellerSkuIdentifierDict
from .walmart_item_identifier import WalmartItemIdentifier, WalmartItemIdentifierDict


class IdentifierTypeProductPricing(SdkBaseModel):
    """Specifies the identifiers used to uniquely identify the item, including the Walmart Marketplace item identifier
    and seller SKU identifier."""

    marketplace_item: WalmartItemIdentifier = Field(alias="MarketplaceItem")
    """Walmart Marketplace and Walmart Item ID that identify the item."""

    sku_identifier: Optional[SellerSkuIdentifier] = Field(default=UNSET, alias="SKUIdentifier")
    """Walmart Marketplace, seller, and seller SKU identifiers for the item."""


class IdentifierTypeProductPricingDict(TypedDict):
    marketplace_item: WalmartItemIdentifierDict
    sku_identifier: NotRequired[SellerSkuIdentifierDict]
