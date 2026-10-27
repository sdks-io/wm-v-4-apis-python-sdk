from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .seller_skuidentifier import SellerSkuidentifier, SellerSkuidentifierDict
from .walmart_item_identifier import WalmartItemIdentifier, WalmartItemIdentifierDict


class IdentifierType1(SdkBaseModel):
    """Specifies the identifiers used to uniquely identify an item."""

    marketplace_item: WalmartItemIdentifier = Field(alias="MarketplaceItem")
    """Schema to identify an item by MarketPlaceId and Walmart Item ID ."""

    sku_identifier: Optional[SellerSkuidentifier] = Field(default=UNSET, alias="SKUIdentifier")
    """Schema to identify an item by MarketPlaceId, SellerId, and SellerSKU."""


class IdentifierType1Dict(TypedDict):
    marketplace_item: WalmartItemIdentifierDict
    sku_identifier: NotRequired[SellerSkuidentifierDict]
