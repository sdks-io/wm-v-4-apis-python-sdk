from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.program import ProgramOrStr


class ItemEligibilityPreviewPayload(SdkBaseModel):
    """Eligibility result for the requested item and program."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart item identifier evaluated for eligibility."""

    program: Optional[ProgramOrStr] = UNSET
    """Program for which the item's eligibility is being evaluated."""

    is_eligible_for_program: Optional[bool] = Field(default=UNSET, alias="isEligibleForProgram")
    """Indicates whether the item is eligible for the specified program."""

    ineligibility_reason_list: Optional[list[str]] = Field(default=UNSET, alias="ineligibilityReasonList")
    """List of reasons why the item is not eligible for the specified program."""


class ItemEligibilityPreviewPayloadDict(TypedDict):
    item_id: NotRequired[str]
    program: NotRequired[ProgramOrStr]
    is_eligible_for_program: NotRequired[bool]
    ineligibility_reason_list: NotRequired[list[str]]
