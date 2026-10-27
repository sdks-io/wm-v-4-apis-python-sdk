from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination4 import Pagination4, Pagination4Dict
from .wfs_item import WfsItem, WfsItemDict


class GetWfsInventoryResponse(SdkBaseModel):
    pagination: Optional[Pagination4] = UNSET
    inventory_summaries: Optional[list[WfsItem]] = Field(default=UNSET, alias="inventorySummaries")


class GetWfsInventoryResponseDict(TypedDict):
    pagination: NotRequired[Pagination4Dict]
    inventory_summaries: NotRequired[list[WfsItemDict]]
