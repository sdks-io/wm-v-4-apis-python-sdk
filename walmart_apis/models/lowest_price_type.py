from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_channel1 import FulfillmentChannel1OrStr
from .enums.offer_customer_type import OfferCustomerTypeOrStr
from .money_type import MoneyType, MoneyTypeDict


class LowestPriceType(SdkBaseModel):
    """Lowest price for a condition, fulfillment channel, and applicable offer type."""

    condition: str
    """Indicates the item condition. Examples include New, Restored, and Pre-Owned."""

    fulfillment_channel: FulfillmentChannel1OrStr = Field(alias="fulfillmentChannel")
    """Indicates whether the item is fulfilled by Walmart Fulfillment Services (WFS) or by the seller."""

    offer_type: Optional[OfferCustomerTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    quantity_tier: Optional[int] = Field(default=UNSET, alias="quantityTier")
    """Indicates the quantity at which this price becomes active."""

    landed_price: Optional[MoneyType] = Field(default=UNSET, alias="LandedPrice")
    """Currency type and monetary value."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    shipping: Optional[MoneyType] = Field(default=UNSET, alias="Shipping")
    """Currency type and monetary value."""


class LowestPriceTypeDict(TypedDict):
    condition: str
    fulfillment_channel: FulfillmentChannel1OrStr
    offer_type: NotRequired[OfferCustomerTypeOrStr]
    quantity_tier: NotRequired[int]
    landed_price: NotRequired[MoneyTypeDict]
    listing_price: MoneyTypeDict
    shipping: NotRequired[MoneyTypeDict]
