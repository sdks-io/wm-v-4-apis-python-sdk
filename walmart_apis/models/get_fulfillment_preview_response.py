from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_fulfillment_preview_result import GetFulfillmentPreviewResult, GetFulfillmentPreviewResultDict


class GetFulfillmentPreviewResponse(SdkBaseModel):
    payload: Optional[GetFulfillmentPreviewResult] = UNSET


class GetFulfillmentPreviewResponseDict(TypedDict):
    payload: NotRequired[GetFulfillmentPreviewResultDict]
