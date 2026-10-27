from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_item_error import BulkItemError, BulkItemErrorDict
from .update_inventory_response import UpdateInventoryResponse, UpdateInventoryResponseDict


class BulkUpdateInventoryResponse(SdkBaseModel):
    succeeded: Optional[list[UpdateInventoryResponse]] = UNSET
    errors: Optional[list[BulkItemError]] = UNSET


class BulkUpdateInventoryResponseDict(TypedDict):
    succeeded: NotRequired[list[UpdateInventoryResponseDict]]
    errors: NotRequired[list[BulkItemErrorDict]]
