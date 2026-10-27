from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WfsUnavailableQuantity(SdkBaseModel):
    inventory_review_units: Optional[int] = Field(default=UNSET, alias="inventoryReviewUnits")
    """Units held pending inventory review"""

    inventory_movement_units: Optional[int] = Field(default=UNSET, alias="inventoryMovementUnits")
    """Units held during fulfillment center movement"""


class WfsUnavailableQuantityDict(TypedDict):
    inventory_review_units: NotRequired[int]
    inventory_movement_units: NotRequired[int]
