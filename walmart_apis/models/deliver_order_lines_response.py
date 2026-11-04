from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DeliverOrderLinesResponse(SdkBaseModel):
    """Delivery confirmation for the order."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    delivered_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveredAt")
    """Date and time when delivery was recorded, in ISO 8601 format."""


class DeliverOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    delivered_at: NotRequired[RFC3339DateTime]
