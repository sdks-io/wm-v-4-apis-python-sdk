from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.offer_customer_type import OfferCustomerTypeOrStr
from .money_type import MoneyType, MoneyTypeDict


class BuyBoxPriceType(SdkBaseModel):
    """Buy Box price information for an item condition and applicable offer type."""

    condition: str
    """Indicates the item condition. Examples include New, Restored, and Pre-Owned."""

    offer_type: Optional[OfferCustomerTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    quantity_tier: Optional[int] = Field(default=UNSET, alias="quantityTier")
    """Indicates the quantity at which this price becomes active."""

    landed_price: MoneyType = Field(alias="LandedPrice")
    """Currency type and monetary value."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    shipping: MoneyType = Field(alias="Shipping")
    """Currency type and monetary value."""

    seller_name: Optional[str] = Field(default=UNSET, alias="sellerName")
    """Name of the seller associated with the offer."""


class BuyBoxPriceTypeDict(TypedDict):
    condition: str
    offer_type: NotRequired[OfferCustomerTypeOrStr]
    quantity_tier: NotRequired[int]
    landed_price: MoneyTypeDict
    listing_price: MoneyTypeDict
    shipping: MoneyTypeDict
    seller_name: NotRequired[str]
