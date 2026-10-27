from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.condition import ConditionOrStr
from .wfs_inventory_details import WfsInventoryDetails, WfsInventoryDetailsDict
from .wfs_inventory_insights import WfsInventoryInsights, WfsInventoryInsightsDict


class WfsItem(SdkBaseModel):
    seller_sku: str = Field(alias="sellerSku")
    """Seller-assigned SKU identifier."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart internal item ID."""

    gtin: Optional[str] = UNSET
    """Global Trade Item Number (14-digit)."""

    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """Walmart offer ID."""

    product_name: OptionalNullable[str] = Field(default=UNSET, alias="productName")
    """Item title as listed on Walmart.com."""

    brand: Optional[str] = UNSET
    """Item brand name."""

    condition: Optional[ConditionOrStr] = UNSET
    """Item condition."""

    last_updated: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdated")
    """Timestamp of the most recent inventory update for this item. Null if no update timestamp is available."""

    inventory_details: Optional[WfsInventoryDetails] = Field(default=UNSET, alias="inventoryDetails")
    inventory_insights: Optional[WfsInventoryInsights] = Field(default=UNSET, alias="inventoryInsights")
    """Demand intelligence and replenishment recommendations (WFS-only — no SP-API equivalent)"""


class WfsItemDict(TypedDict):
    seller_sku: str
    walmart_item_id: NotRequired[str]
    gtin: NotRequired[str]
    offer_id: NotRequired[str]
    product_name: NotRequired[str | None]
    brand: NotRequired[str]
    condition: NotRequired[ConditionOrStr]
    last_updated: NotRequired[RFC3339DateTime | None]
    inventory_details: NotRequired[WfsInventoryDetailsDict]
    inventory_insights: NotRequired[WfsInventoryInsightsDict]
