from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict
from .get_offers_response import GetOffersResponse, GetOffersResponseDict
from .http_response_headers import HttpResponseHeaders, HttpResponseHeadersDict


class BatchOffersResponse(SdkBaseModel):
    """Common schema present in ItemOffersResponse and ListingOffersResponse."""

    headers: Optional[HttpResponseHeaders] = UNSET
    """A mapping of additional HTTP headers to receive for the individual batch request."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """The HTTP status line associated with the response."""

    body: GetOffersResponse
    """The response schema for the getListingOffers and getItemOffers operations."""


class BatchOffersResponseDict(TypedDict):
    headers: NotRequired[HttpResponseHeadersDict]
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: GetOffersResponseDict
