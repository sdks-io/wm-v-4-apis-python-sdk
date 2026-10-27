from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class MultiPackageShipResponse(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    shipped_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shippedAt")
    packages_accepted: Optional[int] = Field(default=UNSET, alias="packagesAccepted")
    """Number of ``packages[]`` entries successfully forwarded to FMS — echoed back so callers can sanity-check against
    what they sent."""


class MultiPackageShipResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipped_at: NotRequired[RFC3339DateTime]
    packages_accepted: NotRequired[int]
