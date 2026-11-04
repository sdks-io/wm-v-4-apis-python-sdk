from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .inventory_summary import InventorySummary, InventorySummaryDict
from .pagination_inventory import PaginationInventory, PaginationInventoryDict


class GetInventorySummariesResponse(SdkBaseModel):
    pagination: Optional[PaginationInventory] = UNSET
    inventory_summaries: Optional[list[InventorySummary]] = Field(default=UNSET, alias="inventorySummaries")


class GetInventorySummariesResponseDict(TypedDict):
    pagination: NotRequired[PaginationInventoryDict]
    inventory_summaries: NotRequired[list[InventorySummaryDict]]
