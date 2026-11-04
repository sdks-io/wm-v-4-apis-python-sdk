from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_response_body import CompetitiveSummaryResponseBody, CompetitiveSummaryResponseBodyDict
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict


class CompetitiveSummaryResponse(SdkBaseModel):
    """Competitive summary response for one item in the batch."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """HTTP status information associated with the response."""

    body: Optional[CompetitiveSummaryResponseBody] = UNSET
    """Competitive summary information returned for a Walmart item."""


class CompetitiveSummaryResponseDict(TypedDict):
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: NotRequired[CompetitiveSummaryResponseBodyDict]
