from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict
from .get_offers_response import GetOffersResponse, GetOffersResponseDict
from .http_response_headers import HttpResponseHeaders, HttpResponseHeadersDict
from .item_offers_request import ItemOffersRequest, ItemOffersRequestDict


class ItemOffersResponse(SdkBaseModel):
    """Schema for an individual ItemOffersResponse."""

    headers: Optional[HttpResponseHeaders] = UNSET
    """A mapping of additional HTTP headers to receive for the individual batch request."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """The HTTP status line associated with the response."""

    body: GetOffersResponse
    """The response schema for the getListingOffers and getItemOffers operations."""

    request: ItemOffersRequest
    """List of request parameters accepted by the getItemOffers operation."""


class ItemOffersResponseDict(TypedDict):
    headers: NotRequired[HttpResponseHeadersDict]
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: GetOffersResponseDict
    request: ItemOffersRequestDict
