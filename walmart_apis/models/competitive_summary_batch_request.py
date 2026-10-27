from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_request import CompetitiveSummaryRequest, CompetitiveSummaryRequestDict


class CompetitiveSummaryBatchRequest(SdkBaseModel):
    """The request body for the getCompetitiveSummary operation."""

    requests: Optional[list[CompetitiveSummaryRequest]] = UNSET
    """A batched list of competitive summary requests."""


class CompetitiveSummaryBatchRequestDict(TypedDict):
    requests: NotRequired[list[CompetitiveSummaryRequestDict]]
