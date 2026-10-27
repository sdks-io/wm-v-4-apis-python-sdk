from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict
from .featured_offer_expected_price_result import FeaturedOfferExpectedPriceResult, FeaturedOfferExpectedPriceResultDict
from .offer_identifier import OfferIdentifier, OfferIdentifierDict


class FeaturedOfferExpectedPriceResponseBody(SdkBaseModel):
    """The body of a FOEP response."""

    offer_identifier: Optional[OfferIdentifier] = Field(default=UNSET, alias="offerIdentifier")
    """Identifies an offer."""

    featured_offer_expected_price_results: Optional[list[FeaturedOfferExpectedPriceResult]] = Field(
        default=UNSET, alias="featuredOfferExpectedPriceResults"
    )
    """A list of FOEP results for the requested offer."""

    errors: Optional[list[Error3]] = UNSET
    """A list of error responses returned when a request is unsuccessful."""


class FeaturedOfferExpectedPriceResponseBodyDict(TypedDict):
    offer_identifier: NotRequired[OfferIdentifierDict]
    featured_offer_expected_price_results: NotRequired[list[FeaturedOfferExpectedPriceResultDict]]
    errors: NotRequired[list[Error3Dict]]
