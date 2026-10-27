from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_price_type import CompetitivePriceType, CompetitivePriceTypeDict
from .money_type import MoneyType, MoneyTypeDict
from .offer_listing_count_type import OfferListingCountType, OfferListingCountTypeDict


class CompetitivePricingType(SdkBaseModel):
    """Competitive pricing information for the item."""

    competitive_prices: list[CompetitivePriceType] = Field(alias="CompetitivePrices")
    """A list of competitive pricing information."""

    number_of_offer_listings: list[OfferListingCountType] = Field(alias="NumberOfOfferListings")
    """The number of active offer listings for the item, by condition."""

    trade_in_value: Optional[MoneyType] = Field(default=UNSET, alias="TradeInValue")
    """Currency type and monetary value."""


class CompetitivePricingTypeDict(TypedDict):
    competitive_prices: list[CompetitivePriceTypeDict]
    number_of_offer_listings: list[OfferListingCountTypeDict]
    trade_in_value: NotRequired[MoneyTypeDict]
