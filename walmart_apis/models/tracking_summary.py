from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status_shipping import StatusShippingOrStr


class TrackingSummary(SdkBaseModel):
    status: Optional[StatusShippingOrStr] = UNSET
    status_updated_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusUpdatedTime")


class TrackingSummaryDict(TypedDict):
    status: NotRequired[StatusShippingOrStr]
    status_updated_time: NotRequired[RFC3339DateTime]
