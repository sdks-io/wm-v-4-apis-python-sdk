from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.period import PeriodOrStr


class ReportSchedule(SdkBaseModel):
    report_schedule_id: str = Field(alias="reportScheduleId")
    report_type: str = Field(alias="reportType")
    period: PeriodOrStr
    """ISO 8601 duration for schedule recurrence"""

    next_report_creation_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="nextReportCreationTime")


class ReportScheduleDict(TypedDict):
    report_schedule_id: str
    report_type: str
    period: PeriodOrStr
    next_report_creation_time: NotRequired[RFC3339DateTime]
