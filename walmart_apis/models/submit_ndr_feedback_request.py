from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.ndr_action import NdrActionOrStr


class SubmitNdrFeedbackRequest(SdkBaseModel):
    seller_tracking_id: str = Field(alias="sellerTrackingId")
    ndr_action: NdrActionOrStr = Field(alias="ndrAction")
    comments: Optional[str] = UNSET


class SubmitNdrFeedbackRequestDict(TypedDict):
    seller_tracking_id: str
    ndr_action: NdrActionOrStr
    comments: NotRequired[str]
