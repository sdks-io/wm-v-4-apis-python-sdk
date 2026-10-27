from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateReportScheduleResponse(SdkBaseModel):
    report_schedule_id: str = Field(alias="reportScheduleId")


class CreateReportScheduleResponseDict(TypedDict):
    report_schedule_id: str
