from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type_product_fees import MoneyTypeProductFees, MoneyTypeProductFeesDict
from .points_product_fees import PointsProductFees, PointsProductFeesDict


class PriceToEstimateFees(SdkBaseModel):
    """Price information used to estimate fees."""

    listing_price: MoneyTypeProductFees = Field(alias="ListingPrice")
    """Monetary amount and currency."""

    shipping: Optional[MoneyTypeProductFees] = Field(default=UNSET, alias="Shipping")
    """Monetary amount and currency."""

    points: Optional[PointsProductFees] = Field(default=UNSET, alias="Points")
    """Walmart Rewards points information used in the fee estimate."""


class PriceToEstimateFeesDict(TypedDict):
    listing_price: MoneyTypeProductFeesDict
    shipping: NotRequired[MoneyTypeProductFeesDict]
    points: NotRequired[PointsProductFeesDict]
