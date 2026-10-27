from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class DeliverOrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    delivered_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="deliveredQuantity")
    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """Optional proof-of-delivery breadcrumb — the tracking number the carrier scanned at delivery. Not validated
    against the tracking number the seller posted at ship time; both are preserved verbatim for downstream audit."""

    package_number: Optional[str] = Field(default=UNSET, alias="packageNumber")
    """Optional package identifier within a multi-package shipment. Maps to gmp-orders-mono's per-package delivery
    event."""

    delivered_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveredDate")
    """ISO-8601 timestamp at which the carrier reported delivery. Optional — if omitted, FMS defaults to server time."""


class DeliverOrderLineDict(TypedDict):
    line_number: str
    delivered_quantity: NotRequired[QuantityWithUnitDict]
    tracking_number: NotRequired[str]
    package_number: NotRequired[str]
    delivered_date: NotRequired[RFC3339DateTime]
