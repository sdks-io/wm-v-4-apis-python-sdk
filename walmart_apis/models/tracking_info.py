from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.carrier import CarrierOrStr
from .enums.method_code import MethodCodeOrStr


class TrackingInfo(SdkBaseModel):
    """Carrier, tracking number, and shipment details."""

    carrier: CarrierOrStr
    """Carrier responsible for the shipment."""

    tracking_number: str = Field(alias="trackingNumber")
    """Carrier tracking number for the shipment."""

    shipped_date: RFC3339DateTime = Field(alias="shippedDate")
    """Date and time when the shipment was shipped, in ISO 8601 format."""

    method_code: Optional[MethodCodeOrStr] = Field(default=UNSET, alias="methodCode")
    """Shipping service method for the shipment."""


class TrackingInfoDict(TypedDict):
    carrier: CarrierOrStr
    tracking_number: str
    shipped_date: RFC3339DateTime
    method_code: NotRequired[MethodCodeOrStr]
