from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_eligibility_preview_payload import ItemEligibilityPreviewPayload, ItemEligibilityPreviewPayloadDict


class GetItemEligibilityPreviewResponse(SdkBaseModel):
    """Response containing the eligibility preview for the requested item and program."""

    payload: Optional[ItemEligibilityPreviewPayload] = UNSET
    """Eligibility result for the requested item and program."""


class GetItemEligibilityPreviewResponseDict(TypedDict):
    payload: NotRequired[ItemEligibilityPreviewPayloadDict]
