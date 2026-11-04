from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_channel import FulfillmentChannelOrStr
from .enums.offer_customer_type import OfferCustomerTypeOrStr
from .money_type import MoneyType, MoneyTypeDict
from .price_type import PriceType, PriceTypeDict
from .quantity_discount_price_type import QuantityDiscountPriceType, QuantityDiscountPriceTypeDict


class OfferTypeProductPricing(SdkBaseModel):
    """Pricing, fulfillment, condition, and seller SKU information for an offer."""

    offer_type: Optional[OfferCustomerTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    buying_price: PriceType = Field(alias="BuyingPrice")
    """Price information for an offer. ``LandedPrice`` is the sum of ``ListingPrice`` and ``Shipping``."""

    regular_price: MoneyType = Field(alias="RegularPrice")
    """Currency type and monetary value."""

    business_price: Optional[MoneyType] = Field(default=UNSET, alias="businessPrice")
    """Currency type and monetary value."""

    quantity_discount_prices: Optional[list[QuantityDiscountPriceType]] = Field(
        default=UNSET, alias="quantityDiscountPrices"
    )
    """Item pricing information when buying in bulk."""

    fulfillment_channel: FulfillmentChannelOrStr = Field(alias="FulfillmentChannel")
    """Fulfillment channel for the offer listing. Possible values are ``WFS`` and ``SELLER``."""

    item_condition: str = Field(alias="ItemCondition")
    """Item condition for the offer listing. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    item_sub_condition: str = Field(alias="ItemSubCondition")
    """Item subcondition for the offer listing."""

    seller_sku: str = Field(alias="SellerSKU")
    """Seller stock keeping unit (SKU) that identifies the item."""


class OfferTypeProductPricingDict(TypedDict):
    offer_type: NotRequired[OfferCustomerTypeOrStr]
    buying_price: PriceTypeDict
    regular_price: MoneyTypeDict
    business_price: NotRequired[MoneyTypeDict]
    quantity_discount_prices: NotRequired[list[QuantityDiscountPriceTypeDict]]
    fulfillment_channel: FulfillmentChannelOrStr
    item_condition: str
    item_sub_condition: str
    seller_sku: str
