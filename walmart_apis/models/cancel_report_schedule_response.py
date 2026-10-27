from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CancelReportScheduleResponse(SdkBaseModel):
    report_schedule_id: Optional[str] = Field(default=UNSET, alias="reportScheduleId")


class CancelReportScheduleResponseDict(TypedDict):
    report_schedule_id: NotRequired[str]
