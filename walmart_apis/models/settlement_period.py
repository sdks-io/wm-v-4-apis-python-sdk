from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status2 import Status2OrStr


class SettlementPeriod(SdkBaseModel):
    period_id: Optional[str] = Field(default=UNSET, alias="periodId")
    start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startDate")
    end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endDate")
    status: Optional[Status2OrStr] = UNSET


class SettlementPeriodDict(TypedDict):
    period_id: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
    status: NotRequired[Status2OrStr]
