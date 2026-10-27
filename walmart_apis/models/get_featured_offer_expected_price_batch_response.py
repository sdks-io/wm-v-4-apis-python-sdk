from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .featured_offer_expected_price_response import (
    FeaturedOfferExpectedPriceResponse,
    FeaturedOfferExpectedPriceResponseDict,
)


class GetFeaturedOfferExpectedPriceBatchResponse(SdkBaseModel):
    """The response schema for the getFeaturedOfferExpectedPriceBatch operation."""

    responses: Optional[list[FeaturedOfferExpectedPriceResponse]] = UNSET
    """A batched list of FOEP responses."""


class GetFeaturedOfferExpectedPriceBatchResponseDict(TypedDict):
    responses: NotRequired[list[FeaturedOfferExpectedPriceResponseDict]]
