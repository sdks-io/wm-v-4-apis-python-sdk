from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .detailed_shipping_time_type import DetailedShippingTimeType, DetailedShippingTimeTypeDict
from .enums.offer_customer_type import OfferCustomerTypeOrStr
from .money_type import MoneyType, MoneyTypeDict
from .quantity_discount_price_type import QuantityDiscountPriceType, QuantityDiscountPriceTypeDict
from .seller_feedback_type import SellerFeedbackType, SellerFeedbackTypeDict
from .ships_from_type import ShipsFromType, ShipsFromTypeDict
from .wfs_prime_details_type import WfsPrimeDetailsType, WfsPrimeDetailsTypeDict


class OfferDetail(SdkBaseModel):
    """Pricing, fulfillment, shipping, condition, and seller information for an offer."""

    my_offer: Optional[bool] = Field(default=UNSET, alias="MyOffer")
    """Indicates whether the offer belongs to the seller making the request."""

    offer_type: Optional[OfferCustomerTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    sub_condition: str = Field(alias="SubCondition")
    """Item subcondition. Possible values are ``New``, ``Mint``, ``Very Good``, ``Good``, ``Acceptable``, ``Poor``,
    ``Club``, ``OEM``, ``Warranty``, ``Refurbished Warranty``, ``Refurbished``, ``Open Box``, and ``Other``."""

    seller_name: Optional[str] = Field(default=UNSET, alias="SellerName")
    """Name of the seller associated with the offer."""

    condition_notes: Optional[str] = Field(default=UNSET, alias="ConditionNotes")
    """Information about the condition of the item."""

    seller_feedback_rating: Optional[SellerFeedbackType] = Field(default=UNSET, alias="SellerFeedbackRating")
    """Seller feedback information, including the percentage of positive feedback and total number of ratings."""

    shipping_time: DetailedShippingTimeType = Field(alias="ShippingTime")
    """Estimated time range in which an item is likely to ship after an order is placed."""

    listing_price: MoneyType = Field(alias="ListingPrice")
    """Currency type and monetary value."""

    quantity_discount_prices: Optional[list[QuantityDiscountPriceType]] = Field(
        default=UNSET, alias="quantityDiscountPrices"
    )
    """Item pricing information for bulk purchases."""

    shipping: MoneyType = Field(alias="Shipping")
    """Currency type and monetary value."""

    ships_from: Optional[ShipsFromType] = Field(default=UNSET, alias="ShipsFrom")
    """State and country from which the item ships."""

    is_fulfilled_by_wfs: bool = Field(alias="IsFulfilledByWFS")
    """Indicates whether Walmart Fulfillment Services (WFS) fulfills the offer."""

    wfs_prime_details: Optional[WfsPrimeDetailsType] = Field(default=UNSET, alias="WFSPrimeDetails")
    """Walmart Fulfillment Services (WFS) Prime eligibility information for the offer."""

    is_buy_box_winner: Optional[bool] = Field(default=UNSET, alias="IsBuyBoxWinner")
    """Indicates whether the offer is currently the Buy Box winner."""


class OfferDetailDict(TypedDict):
    my_offer: NotRequired[bool]
    offer_type: NotRequired[OfferCustomerTypeOrStr]
    sub_condition: str
    seller_name: NotRequired[str]
    condition_notes: NotRequired[str]
    seller_feedback_rating: NotRequired[SellerFeedbackTypeDict]
    shipping_time: DetailedShippingTimeTypeDict
    listing_price: MoneyTypeDict
    quantity_discount_prices: NotRequired[list[QuantityDiscountPriceTypeDict]]
    shipping: MoneyTypeDict
    ships_from: NotRequired[ShipsFromTypeDict]
    is_fulfilled_by_wfs: bool
    wfs_prime_details: NotRequired[WfsPrimeDetailsTypeDict]
    is_buy_box_winner: NotRequired[bool]
