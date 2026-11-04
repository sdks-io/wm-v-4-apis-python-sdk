from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.condition import ConditionOrStr
from .inventory_details import InventoryDetails, InventoryDetailsDict


class InventorySummary(SdkBaseModel):
    """One row per seller SKU. Inventory quantities are broken out per ship-node in ``inventoryDetails[]`` — a SKU
    stocked at multiple ship-nodes has multiple entries. for the one-row-per-node -> one-row-per-SKU restructure
    rationale."""

    seller_sku: str = Field(alias="sellerSku")
    product_name: OptionalNullable[str] = Field(default=UNSET, alias="productName")
    """Item title as listed on the marketplace. Null if not available."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    condition: Optional[ConditionOrStr] = UNSET
    """Item condition."""

    inventory_details: Optional[list[InventoryDetails]] = Field(default=UNSET, alias="inventoryDetails")
    """Inventory quantity breakdown per ship-node. One entry per ship-node this SKU has an active node for. Empty array
    if the SKU is known but has no active ship-node entries."""


class InventorySummaryDict(TypedDict):
    seller_sku: str
    product_name: NotRequired[str | None]
    walmart_item_id: NotRequired[str]
    condition: NotRequired[ConditionOrStr]
    inventory_details: NotRequired[list[InventoryDetailsDict]]
