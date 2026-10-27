from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type1 import MoneyType1, MoneyType1Dict
from .points1 import Points1, Points1Dict


class PriceToEstimateFees(SdkBaseModel):
    """Price information used to estimate fees."""

    listing_price: MoneyType1 = Field(alias="ListingPrice")
    """Currency amount."""

    shipping: Optional[MoneyType1] = Field(default=UNSET, alias="Shipping")
    """Currency amount."""

    points: Optional[Points1] = Field(default=UNSET, alias="Points")
    """Walmart Rewards points."""


class PriceToEstimateFeesDict(TypedDict):
    listing_price: MoneyType1Dict
    shipping: NotRequired[MoneyType1Dict]
    points: NotRequired[Points1Dict]
