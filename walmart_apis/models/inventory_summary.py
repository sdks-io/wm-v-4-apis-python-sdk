from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.condition import ConditionOrStr
from .inventory_details import InventoryDetails, InventoryDetailsDict


class InventorySummary(SdkBaseModel):
    seller_sku: str = Field(alias="sellerSku")
    product_name: OptionalNullable[str] = Field(default=UNSET, alias="productName")
    """Item title as listed on the marketplace. Null if not available."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    condition: Optional[ConditionOrStr] = UNSET
    """Item condition."""

    last_updated: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdated")
    """Timestamp of the most recent inventory update for this SKU at this ship node. Null if no update timestamp is
    available."""

    inventory_available_date: OptionalNullable[Date] = Field(default=UNSET, alias="inventoryAvailableDate")
    """Date from which this inventory is available to sell at this ship node. Null if no availability date has been
    set."""

    inventory_details: OptionalNullable[InventoryDetails] = Field(default=UNSET, alias="inventoryDetails")
    """Inventory quantity breakdown for this SKU at this ship node."""


class InventorySummaryDict(TypedDict):
    seller_sku: str
    product_name: NotRequired[str | None]
    walmart_item_id: NotRequired[str]
    ship_node: NotRequired[str]
    condition: NotRequired[ConditionOrStr]
    last_updated: NotRequired[RFC3339DateTime | None]
    inventory_available_date: NotRequired[Date | None]
    inventory_details: NotRequired[InventoryDetailsDict | None]
