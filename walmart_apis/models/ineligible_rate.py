from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ineligibility_reason import IneligibilityReason, IneligibilityReasonDict


class IneligibleRate(SdkBaseModel):
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    service_name: Optional[str] = Field(default=UNSET, alias="serviceName")
    ineligibility_reasons: Optional[list[IneligibilityReason]] = Field(default=UNSET, alias="ineligibilityReasons")


class IneligibleRateDict(TypedDict):
    carrier_name: NotRequired[str]
    service_name: NotRequired[str]
    ineligibility_reasons: NotRequired[list[IneligibilityReasonDict]]
