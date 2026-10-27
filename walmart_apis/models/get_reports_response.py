from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report import Report, ReportDict


class GetReportsResponse(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    reports: Optional[list[Report]] = UNSET


class GetReportsResponseDict(TypedDict):
    next_token: NotRequired[str]
    reports: NotRequired[list[ReportDict]]
