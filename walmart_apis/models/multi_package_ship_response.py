from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class MultiPackageShipResponse(SdkBaseModel):
    """Multi-package shipment confirmation, including the number of packages accepted."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    shipped_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shippedAt")
    """Date and time when the shipment was recorded, in ISO 8601 format."""

    packages_accepted: Optional[int] = Field(default=UNSET, alias="packagesAccepted")
    """Number of package entries accepted from the shipment request."""


class MultiPackageShipResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipped_at: NotRequired[RFC3339DateTime]
    packages_accepted: NotRequired[int]
