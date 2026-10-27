from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisputeEligibilityResponse(SdkBaseModel):
    is_eligible: Optional[bool] = Field(default=UNSET, alias="isEligible")
    reason: Optional[str] = UNSET


class DisputeEligibilityResponseDict(TypedDict):
    is_eligible: NotRequired[bool]
    reason: NotRequired[str]
