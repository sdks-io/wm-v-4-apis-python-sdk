from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict


class QuantityDiscountPriceType(SdkBaseModel):
    """Contains pricing information for bulk purchase discounts."""

    quantity_tier: int = Field(alias="quantityTier")
    """Indicates at what quantity this price becomes active."""

    quantity_discount_type: Literal["QUANTITY_DISCOUNT"] = Field(
        default="QUANTITY_DISCOUNT", alias="quantityDiscountType"
    )
    """Indicates the type of quantity discount this price applies to."""

    listing_price: MoneyType = Field(alias="listingPrice")
    """Currency type and monetary value."""


class QuantityDiscountPriceTypeDict(TypedDict):
    quantity_tier: int
    quantity_discount_type: Literal["QUANTITY_DISCOUNT"]
    listing_price: MoneyTypeDict
