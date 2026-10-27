from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReportAvailabilityResponse(SdkBaseModel):
    available_dates: Optional[list[str]] = Field(default=UNSET, alias="availableDates")
    is_wfs_report_present: Optional[bool] = Field(default=UNSET, alias="isWfsReportPresent")
    is_legacy_report_present: Optional[bool] = Field(default=UNSET, alias="isLegacyReportPresent")
    is_mt_report_present: Optional[bool] = Field(default=UNSET, alias="isMtReportPresent")


class ReportAvailabilityResponseDict(TypedDict):
    available_dates: NotRequired[list[str]]
    is_wfs_report_present: NotRequired[bool]
    is_legacy_report_present: NotRequired[bool]
    is_mt_report_present: NotRequired[bool]
