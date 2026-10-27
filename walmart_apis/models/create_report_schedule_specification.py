from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.period1 import Period1OrStr


class CreateReportScheduleSpecification(SdkBaseModel):
    report_type: str = Field(alias="reportType")
    period: Period1OrStr
    marketplace_ids: Optional[list[str]] = Field(default=UNSET, alias="marketplaceIds")
    report_options: Optional[dict[str, str]] = Field(default=UNSET, alias="reportOptions")
    next_report_creation_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="nextReportCreationTime")
    """When to first run the schedule (default now)"""


class CreateReportScheduleSpecificationDict(TypedDict):
    report_type: str
    period: Period1OrStr
    marketplace_ids: NotRequired[list[str]]
    report_options: NotRequired[dict[str, str]]
    next_report_creation_time: NotRequired[RFC3339DateTime]
