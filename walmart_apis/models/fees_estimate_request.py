from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.optional_fulfillment_program import OptionalFulfillmentProgramOrStr
from .price_to_estimate_fees import PriceToEstimateFees, PriceToEstimateFeesDict


class FeesEstimateRequest(SdkBaseModel):
    """Pricing and fulfillment information used to estimate fees for an item."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """Marketplace identifier."""

    is_walmart_fulfilled: bool = Field(alias="IsWalmartFulfilled")
    """Indicates whether Walmart Fulfillment Services (WFS) fulfills the item. ``true`` indicates WFS fulfillment;
    ``false`` indicates seller fulfillment."""

    price_to_estimate_fees: PriceToEstimateFees = Field(alias="PriceToEstimateFees")
    """Price information used to estimate fees."""

    identifier: Optional[str] = Field(default=UNSET, alias="Identifier")
    """Identifier provided in the request and returned in SellerInputIdentifier to correlate the fee estimate result
    with the request."""

    optional_fulfillment_program: Optional[OptionalFulfillmentProgramOrStr] = Field(
        default=UNSET, alias="OptionalFulfillmentProgram"
    )
    """Fulfillment program used for the fee estimate."""


class FeesEstimateRequestDict(TypedDict):
    marketplace_id: str
    is_walmart_fulfilled: bool
    price_to_estimate_fees: PriceToEstimateFeesDict
    identifier: NotRequired[str]
    optional_fulfillment_program: NotRequired[OptionalFulfillmentProgramOrStr]
