from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type_product_pricing import ConditionTypeProductPricingOrStr


class ItemIdentifierProductPricing(SdkBaseModel):
    """Marketplace and item identifiers associated with the offer results."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """Walmart Marketplace identifier associated with the item."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart Item ID that identifies the item."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="SellerSKU")
    """Seller stock keeping unit (SKU) that identifies the item."""

    item_condition: ConditionTypeProductPricingOrStr = Field(alias="ItemCondition")
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""


class ItemIdentifierProductPricingDict(TypedDict):
    marketplace_id: str
    walmart_item_id: NotRequired[str]
    seller_sku: NotRequired[str]
    item_condition: ConditionTypeProductPricingOrStr
