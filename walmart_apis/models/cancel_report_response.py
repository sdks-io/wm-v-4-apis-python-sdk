from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CancelReportResponse(SdkBaseModel):
    report_id: Optional[str] = Field(default=UNSET, alias="reportId")


class CancelReportResponseDict(TypedDict):
    report_id: NotRequired[str]
