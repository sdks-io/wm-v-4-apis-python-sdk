from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.report_type import ReportTypeOrStr


class CreateReportSpecification(SdkBaseModel):
    report_type: ReportTypeOrStr = Field(alias="reportType")
    """Report type — Walmart Partner Reporting Platform enum name. Runtime availability is CCM-controlled; consult PRP
    docs for current PROD-enabled types."""

    data_start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dataStartTime")
    data_end_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dataEndTime")
    report_options: Optional[dict[str, str]] = Field(default=UNSET, alias="reportOptions")
    """Additional report-type-specific options"""

    marketplace_ids: Optional[list[str]] = Field(default=UNSET, alias="marketplaceIds")


class CreateReportSpecificationDict(TypedDict):
    report_type: ReportTypeOrStr
    data_start_time: NotRequired[RFC3339DateTime]
    data_end_time: NotRequired[RFC3339DateTime]
    report_options: NotRequired[dict[str, str]]
    marketplace_ids: NotRequired[list[str]]
