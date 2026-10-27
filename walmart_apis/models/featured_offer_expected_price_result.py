from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .featured_offer import FeaturedOffer, FeaturedOfferDict
from .featured_offer_expected_price import FeaturedOfferExpectedPrice, FeaturedOfferExpectedPriceDict


class FeaturedOfferExpectedPriceResult(SdkBaseModel):
    """The featured offer expected price result for a specific offer."""

    featured_offer_expected_price: Optional[FeaturedOfferExpectedPrice] = Field(
        default=UNSET, alias="featuredOfferExpectedPrice"
    )
    """The featured offer expected price for a given SKU."""

    result_status: Optional[str] = Field(default=UNSET, alias="resultStatus")
    """The status of the FOEP request."""

    competing_featured_offer: Optional[FeaturedOffer] = Field(default=UNSET, alias="competingFeaturedOffer")
    """A featured offer."""

    current_featured_offer: Optional[FeaturedOffer] = Field(default=UNSET, alias="currentFeaturedOffer")
    """A featured offer."""


class FeaturedOfferExpectedPriceResultDict(TypedDict):
    featured_offer_expected_price: NotRequired[FeaturedOfferExpectedPriceDict]
    result_status: NotRequired[str]
    competing_featured_offer: NotRequired[FeaturedOfferDict]
    current_featured_offer: NotRequired[FeaturedOfferDict]
