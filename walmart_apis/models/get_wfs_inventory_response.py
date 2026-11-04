from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_inventory import PaginationInventory, PaginationInventoryDict
from .wfs_item import WfsItem, WfsItemDict


class GetWfsInventoryResponse(SdkBaseModel):
    pagination: Optional[PaginationInventory] = UNSET
    inventory_summaries: Optional[list[WfsItem]] = Field(default=UNSET, alias="inventorySummaries")


class GetWfsInventoryResponseDict(TypedDict):
    pagination: NotRequired[PaginationInventoryDict]
    inventory_summaries: NotRequired[list[WfsItemDict]]
