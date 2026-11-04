from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .competitive_price_type import CompetitivePriceType, CompetitivePriceTypeDict
from .offer_listing_count_type import OfferListingCountType, OfferListingCountTypeDict


class CompetitivePricingType(SdkBaseModel):
    """Competitive prices and offer-listing counts for the item."""

    competitive_prices: list[CompetitivePriceType] = Field(alias="CompetitivePrices")
    """Competitive prices returned for the item."""

    number_of_offer_listings: list[OfferListingCountType] = Field(alias="NumberOfOfferListings")
    """Number of active offer listings for the item, by condition."""


class CompetitivePricingTypeDict(TypedDict):
    competitive_prices: list[CompetitivePriceTypeDict]
    number_of_offer_listings: list[OfferListingCountTypeDict]
