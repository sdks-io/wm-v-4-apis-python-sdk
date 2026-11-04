from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_response import CompetitiveSummaryResponse, CompetitiveSummaryResponseDict


class CompetitiveSummaryBatchResponse(SdkBaseModel):
    """Response schema for the ``getCompetitiveSummary`` operation."""

    responses: Optional[list[CompetitiveSummaryResponse]] = UNSET
    """Competitive summary responses returned for the batch."""


class CompetitiveSummaryBatchResponseDict(TypedDict):
    responses: NotRequired[list[CompetitiveSummaryResponseDict]]
