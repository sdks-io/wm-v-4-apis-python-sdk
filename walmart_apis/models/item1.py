from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fulfillment_availability import FulfillmentAvailability, FulfillmentAvailabilityDict
from .issue import Issue, IssueDict
from .item_offer_by_marketplace import ItemOfferByMarketplace, ItemOfferByMarketplaceDict
from .item_summary_by_marketplace import ItemSummaryByMarketplace, ItemSummaryByMarketplaceDict


class Item1(SdkBaseModel):
    sku: str
    summaries: Optional[list[ItemSummaryByMarketplace]] = UNSET
    attributes: Optional[Any] = UNSET
    """Item attribute key-value pairs for the listing"""

    issues: Optional[list[Issue]] = UNSET
    offers: Optional[list[ItemOfferByMarketplace]] = UNSET
    fulfillment_availability: Optional[list[FulfillmentAvailability]] = Field(
        default=UNSET, alias="fulfillmentAvailability"
    )


class Item1Dict(TypedDict):
    sku: str
    summaries: NotRequired[list[ItemSummaryByMarketplaceDict]]
    attributes: NotRequired[Any]
    issues: NotRequired[list[IssueDict]]
    offers: NotRequired[list[ItemOfferByMarketplaceDict]]
    fulfillment_availability: NotRequired[list[FulfillmentAvailabilityDict]]
