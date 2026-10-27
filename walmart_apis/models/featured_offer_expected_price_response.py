from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .featured_offer_expected_price_response_body import (
    FeaturedOfferExpectedPriceResponseBody,
    FeaturedOfferExpectedPriceResponseBodyDict,
)
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict


class FeaturedOfferExpectedPriceResponse(SdkBaseModel):
    """An individual FOEP response."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """The HTTP status line associated with the response."""

    body: Optional[FeaturedOfferExpectedPriceResponseBody] = UNSET
    """The body of a FOEP response."""


class FeaturedOfferExpectedPriceResponseDict(TypedDict):
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: NotRequired[FeaturedOfferExpectedPriceResponseBodyDict]
