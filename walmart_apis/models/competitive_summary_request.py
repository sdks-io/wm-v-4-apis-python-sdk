from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.included_datum_product_pricing import IncludedDatumProductPricingOrStr


class CompetitiveSummaryRequest(SdkBaseModel):
    """Competitive summary request for a single Walmart item. Does not carry a marketplaceId -- the marketplace is
    resolved from the gateway-derived tenant context (x-o-tenant), same as every other pricing endpoint. See
    PricingValidation#currentMarketplaceId."""

    walmart_item_id: str = Field(alias="walmartItemId")
    """Walmart Item ID that identifies the item."""

    included_data: list[IncludedDatumProductPricingOrStr] = Field(alias="includedData")
    """Competitive pricing data to include for the item."""


class CompetitiveSummaryRequestDict(TypedDict):
    walmart_item_id: str
    included_data: list[IncludedDatumProductPricingOrStr]
