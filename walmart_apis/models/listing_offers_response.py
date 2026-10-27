from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict
from .get_offers_response import GetOffersResponse, GetOffersResponseDict
from .http_response_headers import HttpResponseHeaders, HttpResponseHeadersDict
from .listing_offers_request import ListingOffersRequest, ListingOffersRequestDict


class ListingOffersResponse(SdkBaseModel):
    """Schema for an individual ListingOffersResponse."""

    headers: Optional[HttpResponseHeaders] = UNSET
    """A mapping of additional HTTP headers to receive for the individual batch request."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """The HTTP status line associated with the response."""

    body: GetOffersResponse
    """The response schema for the getListingOffers and getItemOffers operations."""

    request: Optional[ListingOffersRequest] = UNSET
    """List of request parameters accepted by the getListingOffers operation."""


class ListingOffersResponseDict(TypedDict):
    headers: NotRequired[HttpResponseHeadersDict]
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: GetOffersResponseDict
    request: NotRequired[ListingOffersRequestDict]
