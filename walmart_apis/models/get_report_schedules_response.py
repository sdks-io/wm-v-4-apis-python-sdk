from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report_schedule import ReportSchedule, ReportScheduleDict


class GetReportSchedulesResponse(SdkBaseModel):
    report_schedules: Optional[list[ReportSchedule]] = Field(default=UNSET, alias="reportSchedules")


class GetReportSchedulesResponseDict(TypedDict):
    report_schedules: NotRequired[list[ReportScheduleDict]]
