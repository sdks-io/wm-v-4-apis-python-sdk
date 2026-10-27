from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel_type import ChannelTypeOrStr
from .marketplace_order_details import MarketplaceOrderDetails, MarketplaceOrderDetailsDict
from .marketplace_shipment_details import MarketplaceShipmentDetails, MarketplaceShipmentDetailsDict


class ChannelDetails(SdkBaseModel):
    channel_type: ChannelTypeOrStr = Field(alias="channelType")
    """Sales-channel hint that lets shipping-v4 route differently for WFS-fulfilled orders, marketplace-seller-fulfilled
    orders, and external (off-Walmart) orders."""

    marketplace_order_details: Optional[MarketplaceOrderDetails] = Field(default=UNSET, alias="marketplaceOrderDetails")
    """Marketplace-side order context for orders originating on the Walmart Marketplace surface. Equivalent in shape to
    industry SP-API's order-details block; renamed to be vendor-neutral."""

    marketplace_shipment_details: Optional[MarketplaceShipmentDetails] = Field(
        default=UNSET, alias="marketplaceShipmentDetails"
    )
    """Marketplace-side shipment context. Renamed from the industry SP-API "vendor-shipment-details" block to be
    vendor-neutral."""


class ChannelDetailsDict(TypedDict):
    channel_type: ChannelTypeOrStr
    marketplace_order_details: NotRequired[MarketplaceOrderDetailsDict]
    marketplace_shipment_details: NotRequired[MarketplaceShipmentDetailsDict]
