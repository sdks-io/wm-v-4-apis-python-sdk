from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict
from .get_offers_response import GetOffersResponse, GetOffersResponseDict
from .http_response_headers import HttpResponseHeaders, HttpResponseHeadersDict
from .listing_offers_request import ListingOffersRequest, ListingOffersRequestDict


class ListingOffersResponse(SdkBaseModel):
    """Result for one seller SKU offer request in a batch, including the corresponding request information."""

    headers: Optional[HttpResponseHeaders] = UNSET
    """Additional HTTP headers returned for an individual batch request."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """HTTP status information associated with the response."""

    body: GetOffersResponse
    """Response schema for ``getListingOffers`` and ``getItemOffers`` operations."""

    request: Optional[ListingOffersRequest] = UNSET
    """Request parameters for one ``getListingOffers`` operation in the batch."""


class ListingOffersResponseDict(TypedDict):
    headers: NotRequired[HttpResponseHeadersDict]
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: GetOffersResponseDict
    request: NotRequired[ListingOffersRequestDict]
