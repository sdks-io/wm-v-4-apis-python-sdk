from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.offer_type import OfferTypeOrStr
from .enums.quantity_discount_type import QuantityDiscountTypeOrStr
from .price_type import PriceType, PriceTypeDict


class CompetitivePriceType(SdkBaseModel):
    """Schema for competitive pricing information."""

    competitive_price_id: str = Field(alias="CompetitivePriceId")
    """The pricing model for each price that is returned. Possible values: 1 - New Buy Box Price. 2 - Used Buy Box
    Price."""

    price: PriceType = Field(alias="Price")
    """Item price information. LandedPrice = ListingPrice + Shipping. Walmart does not have a seller-configurable
    per-offer loyalty points mechanism; the Points field from the SP-API reference spec is omitted.."""

    condition: Optional[str] = UNSET
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, or Club."""

    subcondition: Optional[str] = UNSET
    """Indicates the subcondition of the item."""

    offer_type: Optional[OfferTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is a B2B or B2C offer."""

    quantity_tier: Optional[int] = Field(default=UNSET, alias="quantityTier")
    """Indicates at what quantity this price becomes active."""

    quantity_discount_type: Optional[QuantityDiscountTypeOrStr] = Field(default=UNSET, alias="quantityDiscountType")
    """Indicates the type of quantity discount this price applies to."""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """The seller identifier for the offer."""

    belongs_to_requester: Optional[bool] = Field(default=UNSET, alias="belongsToRequester")
    """Indicates whether the pricing information is for an offer listing that belongs to the requester."""


class CompetitivePriceTypeDict(TypedDict):
    competitive_price_id: str
    price: PriceTypeDict
    condition: NotRequired[str]
    subcondition: NotRequired[str]
    offer_type: NotRequired[OfferTypeOrStr]
    quantity_tier: NotRequired[int]
    quantity_discount_type: NotRequired[QuantityDiscountTypeOrStr]
    seller_id: NotRequired[str]
    belongs_to_requester: NotRequired[bool]
