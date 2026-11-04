from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .buy_box_price_type import BuyBoxPriceType, BuyBoxPriceTypeDict
from .lowest_price_type import LowestPriceType, LowestPriceTypeDict
from .money_type import MoneyType, MoneyTypeDict
from .offer_count_type import OfferCountType, OfferCountTypeDict
from .sales_rank_type import SalesRankType, SalesRankTypeDict


class Summary(SdkBaseModel):
    """Price and offer summary for the item, including ``LowestPrices``, ``BuyBoxPrices``, and ``NumberOfOffers``."""

    total_offer_count: int = Field(alias="TotalOfferCount")
    """Total number of unique offers represented in ``NumberOfOffers``."""

    number_of_offers: Optional[list[OfferCountType]] = Field(default=UNSET, alias="NumberOfOffers")
    """Total number of offers, grouped by condition and fulfillment channel."""

    lowest_prices: Optional[list[LowestPriceType]] = Field(default=UNSET, alias="LowestPrices")
    """Lowest prices returned for the item."""

    buy_box_prices: Optional[list[BuyBoxPriceType]] = Field(default=UNSET, alias="BuyBoxPrices")
    """Buy Box prices returned for the item."""

    list_price: Optional[MoneyType] = Field(default=UNSET, alias="ListPrice")
    """Currency type and monetary value."""

    competitive_price_threshold: Optional[MoneyType] = Field(default=UNSET, alias="CompetitivePriceThreshold")
    """Currency type and monetary value."""

    suggested_lower_price_plus_shipping: Optional[MoneyType] = Field(
        default=UNSET, alias="SuggestedLowerPricePlusShipping"
    )
    """Currency type and monetary value."""

    sales_rankings: Optional[list[SalesRankType]] = Field(default=UNSET, alias="SalesRankings")
    """Sales rank information for the item, by category."""

    buy_box_eligible_offers: Optional[list[OfferCountType]] = Field(default=UNSET, alias="BuyBoxEligibleOffers")
    """Total number of offers eligible for the Buy Box, grouped by condition and fulfillment channel."""

    offers_available_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="OffersAvailableTime")
    """Timestamp when offers will be available for processing if ``status`` is ``ActiveButTooSoonForProcessing``."""


class SummaryDict(TypedDict):
    total_offer_count: int
    number_of_offers: NotRequired[list[OfferCountTypeDict]]
    lowest_prices: NotRequired[list[LowestPriceTypeDict]]
    buy_box_prices: NotRequired[list[BuyBoxPriceTypeDict]]
    list_price: NotRequired[MoneyTypeDict]
    competitive_price_threshold: NotRequired[MoneyTypeDict]
    suggested_lower_price_plus_shipping: NotRequired[MoneyTypeDict]
    sales_rankings: NotRequired[list[SalesRankTypeDict]]
    buy_box_eligible_offers: NotRequired[list[OfferCountTypeDict]]
    offers_available_time: NotRequired[RFC3339DateTime]
