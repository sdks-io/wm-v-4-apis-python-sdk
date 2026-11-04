from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CancelOrderLinesResponse(SdkBaseModel):
    """Order cancellation result."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    cancelled_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="cancelledAt")
    """Date and time when the cancellation was recorded, in ISO 8601 format."""


class CancelOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    cancelled_at: NotRequired[RFC3339DateTime]
