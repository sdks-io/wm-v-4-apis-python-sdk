from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ShipOrderLinesResponse(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    shipped_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shippedAt")


class ShipOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipped_at: NotRequired[RFC3339DateTime]
