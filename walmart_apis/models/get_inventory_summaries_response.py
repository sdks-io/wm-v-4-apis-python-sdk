from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .inventory_summary import InventorySummary, InventorySummaryDict
from .pagination4 import Pagination4, Pagination4Dict


class GetInventorySummariesResponse(SdkBaseModel):
    pagination: Optional[Pagination4] = UNSET
    inventory_summaries: Optional[list[InventorySummary]] = Field(default=UNSET, alias="inventorySummaries")


class GetInventorySummariesResponseDict(TypedDict):
    pagination: NotRequired[Pagination4Dict]
    inventory_summaries: NotRequired[list[InventorySummaryDict]]
