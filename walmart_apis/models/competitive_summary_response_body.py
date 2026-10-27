from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompetitiveSummaryResponseBody(SdkBaseModel):
    """The body of a competitive summary response."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """The Walmart Item ID of the item."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """A marketplace identifier."""

    featured_buying_options: Optional[list[Any]] = Field(default=UNSET, alias="featuredBuyingOptions")
    """A list of featured buying options."""

    lowest_priced_offers: Optional[list[Any]] = Field(default=UNSET, alias="lowestPricedOffers")
    """A list of lowest priced offers by condition."""

    reference_prices: Optional[list[Any]] = Field(default=UNSET, alias="referencePrices")
    """A list of reference prices."""


class CompetitiveSummaryResponseBodyDict(TypedDict):
    walmart_item_id: NotRequired[str]
    marketplace_id: NotRequired[str]
    featured_buying_options: NotRequired[list[Any]]
    lowest_priced_offers: NotRequired[list[Any]]
    reference_prices: NotRequired[list[Any]]
