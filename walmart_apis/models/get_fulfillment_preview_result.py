from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fulfillment_preview import FulfillmentPreview, FulfillmentPreviewDict


class GetFulfillmentPreviewResult(SdkBaseModel):
    fulfillment_previews: Optional[list[FulfillmentPreview]] = Field(default=UNSET, alias="fulfillmentPreviews")


class GetFulfillmentPreviewResultDict(TypedDict):
    fulfillment_previews: NotRequired[list[FulfillmentPreviewDict]]
