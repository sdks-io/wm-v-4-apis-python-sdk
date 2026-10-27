from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict


class FeaturedOfferExpectedPrice(SdkBaseModel):
    """The featured offer expected price for a given SKU."""

    listing_price: Optional[MoneyType] = Field(default=UNSET, alias="listingPrice")
    """Currency type and monetary value."""


class FeaturedOfferExpectedPriceDict(TypedDict):
    listing_price: NotRequired[MoneyTypeDict]
