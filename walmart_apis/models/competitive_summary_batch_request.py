from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_request import CompetitiveSummaryRequest, CompetitiveSummaryRequestDict


class CompetitiveSummaryBatchRequest(SdkBaseModel):
    """Request body for the ``getCompetitiveSummary`` operation."""

    requests: Optional[list[CompetitiveSummaryRequest]] = UNSET
    """Competitive summary requests to process in the batch. Contains at least one request."""


class CompetitiveSummaryBatchRequestDict(TypedDict):
    requests: NotRequired[list[CompetitiveSummaryRequestDict]]
