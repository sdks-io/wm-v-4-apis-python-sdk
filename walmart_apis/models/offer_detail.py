from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .detailed_shipping_time_type import DetailedShippingTimeType, DetailedShippingTimeTypeDict
from .enums.offer_type import OfferTypeOrStr
from .money_type import MoneyType, MoneyTypeDict
from .quantity_discount_price_type import QuantityDiscountPriceType, QuantityDiscountPriceTypeDict
from .seller_feedback_type import SellerFeedbackType, SellerFeedbackTypeDict
from .ships_from_type import ShipsFromType, ShipsFromTypeDict
from .wfsprime_details_type import WfsprimeDetailsType, WfsprimeDetailsTypeDict


class OfferDetail(SdkBaseModel):
    """Schema for an individual offer detail."""

    my_offer: Optional[bool] = Field(default=UNSET, alias="MyOffer")
    """When true, this is the seller's offer."""

    offer_type: Optional[OfferTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is a B2B or B2C offer."""

    sub_condition: str = Field(alias="SubCondition")
    """The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM,
    Warranty, Refurbished Warranty, Refurbished, Open Box, or Other."""

    seller_id: Optional[str] = Field(default=UNSET, alias="SellerId")
    """The seller identifier for the offer."""

    condition_notes: Optional[str] = Field(default=UNSET, alias="ConditionNotes")
    """Information about the condition of the item."""

    seller_feedback_rating: Optional[SellerFeedbackType] = Field(default=UNSET, alias="SellerFeedbackRating")
    """Information about the seller's feedback, including the percentage of positive feedback and total ratings."""

    shipping_time: DetailedShippingTimeType = Field(alias="ShippingTime")
    """The time range in which an item will likely be shipped once an order has been placed."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    quantity_discount_prices: Optional[list[QuantityDiscountPriceType]] = Field(
        default=UNSET, alias="quantityDiscountPrices"
    )
    """Item pricing information when buying in bulk."""

    shipping: MoneyType = Field(alias="Shipping")
    """Currency type and monetary value."""

    ships_from: Optional[ShipsFromType] = Field(default=UNSET, alias="ShipsFrom")
    """The state and country from where the item is shipped."""

    is_fulfilled_by_wfs: bool = Field(alias="IsFulfilledByWFS")
    """When true, the offer is fulfilled by Walmart Fulfillment Services (WFS)."""

    wfs_prime_details: Optional[WfsprimeDetailsType] = Field(default=UNSET, alias="WFSPrimeDetails")
    """Walmart Fulfillment Services prime eligibility information."""

    is_buy_box_winner: Optional[bool] = Field(default=UNSET, alias="IsBuyBoxWinner")
    """When true, the offer is currently in the Buy Box."""

    is_featured_merchant: Optional[bool] = Field(default=UNSET, alias="IsFeaturedMerchant")
    """When true, the seller of the item is eligible to win the Buy Box."""


class OfferDetailDict(TypedDict):
    my_offer: NotRequired[bool]
    offer_type: NotRequired[OfferTypeOrStr]
    sub_condition: str
    seller_id: NotRequired[str]
    condition_notes: NotRequired[str]
    seller_feedback_rating: NotRequired[SellerFeedbackTypeDict]
    shipping_time: DetailedShippingTimeTypeDict
    listing_price: MoneyTypeDict
    quantity_discount_prices: NotRequired[list[QuantityDiscountPriceTypeDict]]
    shipping: MoneyTypeDict
    ships_from: NotRequired[ShipsFromTypeDict]
    is_fulfilled_by_wfs: bool
    wfs_prime_details: NotRequired[WfsprimeDetailsTypeDict]
    is_buy_box_winner: NotRequired[bool]
    is_featured_merchant: NotRequired[bool]
