from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class FasterPayoutEligibilityResponse(SdkBaseModel):
    is_eligible: Optional[bool] = Field(default=UNSET, alias="isEligible")
    ineligible_reason: Optional[str] = Field(default=UNSET, alias="ineligibleReason")
    available_amount: Optional[Money] = Field(default=UNSET, alias="availableAmount")


class FasterPayoutEligibilityResponseDict(TypedDict):
    is_eligible: NotRequired[bool]
    ineligible_reason: NotRequired[str]
    available_amount: NotRequired[MoneyDict]
