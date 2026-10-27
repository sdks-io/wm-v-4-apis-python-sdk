from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type2 import ConditionType2OrStr


class ItemIdentifier1(SdkBaseModel):
    """Information that identifies an item."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """A marketplace identifier."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """The Walmart Item ID of the item."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="SellerSKU")
    """The seller stock keeping unit (SKU) of the item."""

    item_condition: ConditionType2OrStr = Field(alias="ItemCondition")
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""


class ItemIdentifier1Dict(TypedDict):
    marketplace_id: str
    walmart_item_id: NotRequired[str]
    seller_sku: NotRequired[str]
    item_condition: ConditionType2OrStr
