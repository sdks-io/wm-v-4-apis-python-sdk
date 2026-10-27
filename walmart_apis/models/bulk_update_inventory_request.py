from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_inventory_item import BulkInventoryItem, BulkInventoryItemDict


class BulkUpdateInventoryRequest(SdkBaseModel):
    items: list[BulkInventoryItem]


class BulkUpdateInventoryRequestDict(TypedDict):
    items: list[BulkInventoryItemDict]
