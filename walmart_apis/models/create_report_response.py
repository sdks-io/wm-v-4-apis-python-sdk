from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateReportResponse(SdkBaseModel):
    report_id: str = Field(alias="reportId")


class CreateReportResponseDict(TypedDict):
    report_id: str
