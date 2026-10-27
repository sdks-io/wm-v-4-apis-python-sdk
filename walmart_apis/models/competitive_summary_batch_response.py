from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_response import CompetitiveSummaryResponse, CompetitiveSummaryResponseDict


class CompetitiveSummaryBatchResponse(SdkBaseModel):
    """The response schema for the getCompetitiveSummary operation."""

    responses: Optional[list[CompetitiveSummaryResponse]] = UNSET
    """A batched list of competitive summary responses."""


class CompetitiveSummaryBatchResponseDict(TypedDict):
    responses: NotRequired[list[CompetitiveSummaryResponseDict]]
