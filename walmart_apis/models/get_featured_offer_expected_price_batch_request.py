from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .featured_offer_expected_price_request import (
    FeaturedOfferExpectedPriceRequest,
    FeaturedOfferExpectedPriceRequestDict,
)


class GetFeaturedOfferExpectedPriceBatchRequest(SdkBaseModel):
    """The request body for the getFeaturedOfferExpectedPriceBatch operation."""

    requests: Optional[list[FeaturedOfferExpectedPriceRequest]] = UNSET
    """A batched list of FOEP requests."""


class GetFeaturedOfferExpectedPriceBatchRequestDict(TypedDict):
    requests: NotRequired[list[FeaturedOfferExpectedPriceRequestDict]]
