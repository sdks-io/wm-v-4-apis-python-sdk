from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.offer_customer_type import OfferCustomerTypeOrStr
from .price_type import PriceType, PriceTypeDict


class CompetitivePriceType(SdkBaseModel):
    """Competitive price information for an offer."""

    competitive_price_id: str = Field(alias="CompetitivePriceId")
    """Pricing model identifier for the competitive price. Supported values are ``BUYBOX`` for the requester's buy-box
    price and ``COMPETITIVE`` for the lowest competitor price."""

    price: PriceType = Field(alias="Price")
    """Price information for an offer. ``LandedPrice`` is the sum of ``ListingPrice`` and ``Shipping``."""

    condition: Optional[str] = UNSET
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    subcondition: Optional[str] = UNSET
    """Indicates the subcondition of the item."""

    offer_type: Optional[OfferCustomerTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    quantity_tier: Optional[int] = Field(default=UNSET, alias="quantityTier")
    """Indicates the quantity at which this price becomes active."""

    seller_name: Optional[str] = Field(default=UNSET, alias="sellerName")
    """Name of the seller associated with the offer."""

    belongs_to_requester: Optional[bool] = Field(default=UNSET, alias="belongsToRequester")
    """Indicates whether the pricing information is for an offer listing that belongs to the requester."""


class CompetitivePriceTypeDict(TypedDict):
    competitive_price_id: str
    price: PriceTypeDict
    condition: NotRequired[str]
    subcondition: NotRequired[str]
    offer_type: NotRequired[OfferCustomerTypeOrStr]
    quantity_tier: NotRequired[int]
    seller_name: NotRequired[str]
    belongs_to_requester: NotRequired[bool]
