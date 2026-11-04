from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class RefundOrderLinesResponse(SdkBaseModel):
    """Identifiers and timestamp for the refund."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    refund_id: Optional[str] = Field(default=UNSET, alias="refundId")
    """Identifier assigned to the refund."""

    refunded_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="refundedAt")
    """Date and time when the refund was recorded, in ISO 8601 format."""


class RefundOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    refund_id: NotRequired[str]
    refunded_at: NotRequired[RFC3339DateTime]
