from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_channel_type import FulfillmentChannelTypeOrStr


class OfferCountType(SdkBaseModel):
    """The total number of offers for the specified condition and fulfillment channel."""

    condition: Optional[str] = UNSET
    """Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club."""

    fulfillment_channel: Optional[FulfillmentChannelTypeOrStr] = Field(default=UNSET, alias="fulfillmentChannel")
    """Indicates whether the item is fulfilled by the seller or by Walmart Fulfillment Services."""

    offer_count: Optional[int] = Field(default=UNSET, alias="OfferCount")
    """The number of offers in a fulfillment channel that meet a specific condition."""


class OfferCountTypeDict(TypedDict):
    condition: NotRequired[str]
    fulfillment_channel: NotRequired[FulfillmentChannelTypeOrStr]
    offer_count: NotRequired[int]
