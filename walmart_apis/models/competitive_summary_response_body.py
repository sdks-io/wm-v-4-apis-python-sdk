from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompetitiveSummaryResponseBody(SdkBaseModel):
    """Competitive summary information returned for a Walmart item."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart Item ID that identifies the item."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """Walmart Marketplace identifier associated with the item."""

    featured_buying_options: Optional[list[Any]] = Field(default=UNSET, alias="featuredBuyingOptions")
    """Featured buying options returned for the item."""

    lowest_priced_offers: Optional[list[Any]] = Field(default=UNSET, alias="lowestPricedOffers")
    """Lowest-priced offers returned for the item, grouped by condition."""

    reference_prices: Optional[list[Any]] = Field(default=UNSET, alias="referencePrices")
    """Reference prices returned for the item."""


class CompetitiveSummaryResponseBodyDict(TypedDict):
    walmart_item_id: NotRequired[str]
    marketplace_id: NotRequired[str]
    featured_buying_options: NotRequired[list[Any]]
    lowest_priced_offers: NotRequired[list[Any]]
    reference_prices: NotRequired[list[Any]]
