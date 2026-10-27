from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status5 import Status5OrStr


class TrackingSummary(SdkBaseModel):
    status: Optional[Status5OrStr] = UNSET
    status_updated_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusUpdatedTime")


class TrackingSummaryDict(TypedDict):
    status: NotRequired[Status5OrStr]
    status_updated_time: NotRequired[RFC3339DateTime]
