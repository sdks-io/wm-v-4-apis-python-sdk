from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkInventoryItem(SdkBaseModel):
    seller_sku: str = Field(alias="sellerSku")
    quantity: int
    """Declared on-hand quantity. Must be ≥ 0."""

    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    fulfillment_lag: Optional[int] = Field(default=UNSET, alias="fulfillmentLag")


class BulkInventoryItemDict(TypedDict):
    seller_sku: str
    quantity: int
    ship_node: NotRequired[str]
    fulfillment_lag: NotRequired[int]
