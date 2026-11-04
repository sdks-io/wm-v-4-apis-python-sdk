from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type_product_pricing import ConditionTypeProductPricingOrStr
from .item_identifier_product_pricing import ItemIdentifierProductPricing, ItemIdentifierProductPricingDict
from .offer_detail import OfferDetail, OfferDetailDict
from .summary import Summary, SummaryDict


class GetOffersResult(SdkBaseModel):
    """Offer results returned by the ``getListingOffers`` and ``getItemOffers`` operations, including summary pricing
    and individual offers."""

    marketplace_id: str = Field(alias="marketplaceId")
    """Walmart Marketplace identifier associated with the offer results."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart Item ID that identifies the item."""

    sku: Optional[str] = Field(default=UNSET, alias="SKU")
    """Seller stock keeping unit (SKU) that identifies the item."""

    item_condition: ConditionTypeProductPricingOrStr = Field(alias="ItemCondition")
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    status: str
    """Status of the offer request for the item."""

    identifier: ItemIdentifierProductPricing = Field(alias="Identifier")
    """Marketplace and item identifiers associated with the offer results."""

    summary: Summary = Field(alias="Summary")
    """Price and offer summary for the item, including ``LowestPrices``, ``BuyBoxPrices``, and ``NumberOfOffers``."""

    offers: list[OfferDetail] = Field(alias="Offers")
    """Offer details returned for the item. The list contains the number of entries specified by ``TotalOfferCount`` in
    ``Summary``, or 20 entries, whichever is fewer."""


class GetOffersResultDict(TypedDict):
    marketplace_id: str
    walmart_item_id: NotRequired[str]
    sku: NotRequired[str]
    item_condition: ConditionTypeProductPricingOrStr
    status: str
    identifier: ItemIdentifierProductPricingDict
    summary: SummaryDict
    offers: list[OfferDetailDict]
