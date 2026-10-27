from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_channel import FulfillmentChannelOrStr
from .enums.offer_type import OfferTypeOrStr
from .money_type import MoneyType, MoneyTypeDict
from .price_type import PriceType, PriceTypeDict
from .quantity_discount_price_type import QuantityDiscountPriceType, QuantityDiscountPriceTypeDict


class OfferType1(SdkBaseModel):
    """Schema for an individual offer."""

    offer_type: Optional[OfferTypeOrStr] = Field(default=UNSET, alias="offerType")
    """Indicates whether the offer is a B2B or B2C offer."""

    buying_price: PriceType = Field(alias="BuyingPrice")
    """Item price information. LandedPrice = ListingPrice + Shipping. Walmart does not have a seller-configurable
    per-offer loyalty points mechanism; the Points field from the SP-API reference spec is omitted.."""

    regular_price: MoneyType = Field(alias="RegularPrice")
    """Currency type and monetary value."""

    business_price: Optional[MoneyType] = Field(default=UNSET, alias="businessPrice")
    """Currency type and monetary value."""

    quantity_discount_prices: Optional[list[QuantityDiscountPriceType]] = Field(
        default=UNSET, alias="quantityDiscountPrices"
    )
    """Item pricing information when buying in bulk."""

    fulfillment_channel: FulfillmentChannelOrStr = Field(alias="FulfillmentChannel")
    """The fulfillment channel for the offer listing. Possible values: WFS, SELLER."""

    item_condition: str = Field(alias="ItemCondition")
    """The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club."""

    item_sub_condition: str = Field(alias="ItemSubCondition")
    """The item subcondition for the offer listing."""

    seller_sku: str = Field(alias="SellerSKU")
    """The seller stock keeping unit (SKU) of the item."""


class OfferType1Dict(TypedDict):
    offer_type: NotRequired[OfferTypeOrStr]
    buying_price: PriceTypeDict
    regular_price: MoneyTypeDict
    business_price: NotRequired[MoneyTypeDict]
    quantity_discount_prices: NotRequired[list[QuantityDiscountPriceTypeDict]]
    fulfillment_channel: FulfillmentChannelOrStr
    item_condition: str
    item_sub_condition: str
    seller_sku: str
