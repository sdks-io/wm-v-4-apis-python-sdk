from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RejectedShippingService(SdkBaseModel):
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    shipping_service_id: Optional[str] = Field(default=UNSET, alias="shippingServiceId")
    rejection_reason_code: Optional[str] = Field(default=UNSET, alias="rejectionReasonCode")
    rejection_reason_message: Optional[str] = Field(default=UNSET, alias="rejectionReasonMessage")


class RejectedShippingServiceDict(TypedDict):
    carrier_name: NotRequired[str]
    shipping_service_id: NotRequired[str]
    rejection_reason_code: NotRequired[str]
    rejection_reason_message: NotRequired[str]
