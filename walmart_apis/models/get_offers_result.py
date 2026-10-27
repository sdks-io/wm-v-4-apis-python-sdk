from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type2 import ConditionType2OrStr
from .item_identifier1 import ItemIdentifier1, ItemIdentifier1Dict
from .offer_detail import OfferDetail, OfferDetailDict
from .summary import Summary, SummaryDict


class GetOffersResult(SdkBaseModel):
    """The payload for the getListingOffers and getItemOffers operations."""

    marketplace_id: str = Field(alias="marketplaceId")
    """A marketplace identifier."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """The Walmart Item ID of the item."""

    sku: Optional[str] = Field(default=UNSET, alias="SKU")
    """The stock keeping unit (SKU) of the item."""

    item_condition: ConditionType2OrStr = Field(alias="ItemCondition")
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""

    status: str
    """The status of the operation."""

    identifier: ItemIdentifier1 = Field(alias="Identifier")
    """Information that identifies an item."""

    summary: Summary = Field(alias="Summary")
    """Contains price information about the product, including LowestPrices, BuyBoxPrices, and NumberOfOffers."""

    offers: list[OfferDetail] = Field(alias="Offers")
    """A list of offer details. The list is the same length as TotalOfferCount in the Summary or 20, whichever is
    less."""


class GetOffersResultDict(TypedDict):
    marketplace_id: str
    walmart_item_id: NotRequired[str]
    sku: NotRequired[str]
    item_condition: ConditionType2OrStr
    status: str
    identifier: ItemIdentifier1Dict
    summary: SummaryDict
    offers: list[OfferDetailDict]
