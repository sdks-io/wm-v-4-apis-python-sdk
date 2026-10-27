from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.offer_type import OfferTypeOrStr
from .enums.quantity_discount_type import QuantityDiscountTypeOrStr
from .money_type import MoneyType, MoneyTypeDict


class BuyBoxPriceType(SdkBaseModel):
    """Schema for an individual Buy Box price."""

    condition: str
    """Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club."""

    offer_type: Optional[OfferTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is a B2B or B2C offer."""

    quantity_tier: Optional[int] = Field(default=UNSET, alias="quantityTier")
    """Indicates at what quantity this price becomes active."""

    quantity_discount_type: Optional[QuantityDiscountTypeOrStr] = Field(default=UNSET, alias="quantityDiscountType")
    """Indicates the type of quantity discount this price applies to."""

    landed_price: MoneyType = Field(alias="LandedPrice")
    """Currency type and monetary value."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    shipping: MoneyType = Field(alias="Shipping")
    """Currency type and monetary value."""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """The seller identifier for the offer."""


class BuyBoxPriceTypeDict(TypedDict):
    condition: str
    offer_type: NotRequired[OfferTypeOrStr]
    quantity_tier: NotRequired[int]
    quantity_discount_type: NotRequired[QuantityDiscountTypeOrStr]
    landed_price: MoneyTypeDict
    listing_price: MoneyTypeDict
    shipping: MoneyTypeDict
    seller_id: NotRequired[str]
