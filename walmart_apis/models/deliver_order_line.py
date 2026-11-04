from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class DeliverOrderLine(SdkBaseModel):
    """Delivery information for an order line."""

    line_number: str = Field(alias="lineNumber")
    """Line identifier within the purchase order."""

    delivered_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="deliveredQuantity")
    """Numeric quantity and its unit of measure."""

    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """Tracking number reported by the carrier at delivery. This value is optional and is not validated against the
    tracking number provided at shipment."""

    package_number: Optional[str] = Field(default=UNSET, alias="packageNumber")
    """Optional package identifier for a delivery that includes multiple packages."""

    delivered_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveredDate")
    """Date and time when the carrier reported delivery, in ISO 8601 format."""


class DeliverOrderLineDict(TypedDict):
    line_number: str
    delivered_quantity: NotRequired[QuantityWithUnitDict]
    tracking_number: NotRequired[str]
    package_number: NotRequired[str]
    delivered_date: NotRequired[RFC3339DateTime]
