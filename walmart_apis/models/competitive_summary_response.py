from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_summary_response_body import CompetitiveSummaryResponseBody, CompetitiveSummaryResponseBodyDict
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict


class CompetitiveSummaryResponse(SdkBaseModel):
    """An individual competitive summary response."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """The HTTP status line associated with the response."""

    body: Optional[CompetitiveSummaryResponseBody] = UNSET
    """The body of a competitive summary response."""


class CompetitiveSummaryResponseDict(TypedDict):
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: NotRequired[CompetitiveSummaryResponseBodyDict]
