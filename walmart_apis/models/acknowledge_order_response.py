from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AcknowledgeOrderResponse(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    acknowledged_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="acknowledgedAt")


class AcknowledgeOrderResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    acknowledged_at: NotRequired[RFC3339DateTime]
