from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.carrier_name import CarrierNameOrStr
from .enums.method_code import MethodCodeOrStr


class TrackingInfo(SdkBaseModel):
    carrier: CarrierNameOrStr
    tracking_number: str = Field(alias="trackingNumber")
    shipped_date: RFC3339DateTime = Field(alias="shippedDate")
    method_code: Optional[MethodCodeOrStr] = Field(default=UNSET, alias="methodCode")


class TrackingInfoDict(TypedDict):
    carrier: CarrierNameOrStr
    tracking_number: str
    shipped_date: RFC3339DateTime
    method_code: NotRequired[MethodCodeOrStr]
