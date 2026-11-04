from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict


class PriceType(SdkBaseModel):
    """Price information for an offer. ``LandedPrice`` is the sum of ``ListingPrice`` and ``Shipping``."""

    landed_price: Optional[MoneyType] = Field(default=UNSET, alias="LandedPrice")
    """Currency type and monetary value."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    shipping: Optional[MoneyType] = Field(default=UNSET, alias="Shipping")
    """Currency type and monetary value."""


class PriceTypeDict(TypedDict):
    landed_price: NotRequired[MoneyTypeDict]
    listing_price: MoneyTypeDict
    shipping: NotRequired[MoneyTypeDict]
