from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class RefundOrderLinesResponse(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    refund_id: Optional[str] = Field(default=UNSET, alias="refundId")
    """Seller-visible refund handle, generated server-side. Stable for the lifetime of the refund; future GET endpoints
    will accept it as a path variable."""

    refunded_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="refundedAt")


class RefundOrderLinesResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    refund_id: NotRequired[str]
    refunded_at: NotRequired[RFC3339DateTime]
