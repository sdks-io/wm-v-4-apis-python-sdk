from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateInventoryRequest(SdkBaseModel):
    quantity: int
    """Declared on-hand quantity (maps to PIS inputQty). Must be ≥ 0."""

    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    fulfillment_lag: Optional[int] = Field(default=UNSET, alias="fulfillmentLag")
    """Lead time in days to ship (0-4 for standard)"""


class UpdateInventoryRequestDict(TypedDict):
    quantity: int
    ship_node: NotRequired[str]
    fulfillment_lag: NotRequired[int]
