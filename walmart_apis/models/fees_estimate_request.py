from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.optional_fulfillment_program import OptionalFulfillmentProgramOrStr
from .price_to_estimate_fees import PriceToEstimateFees, PriceToEstimateFeesDict


class FeesEstimateRequest(SdkBaseModel):
    """Fee estimate parameters for a single item. Used in both single-item and batch endpoints. Mirrors SP-API
    FeesEstimateRequest."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """Marketplace identifier."""

    is_walmart_fulfilled: bool = Field(alias="IsWalmartFulfilled")
    """true if fulfilled by Walmart Fulfillment Services (WFS); false for seller-fulfilled."""

    price_to_estimate_fees: PriceToEstimateFees = Field(alias="PriceToEstimateFees")
    """Price information used to estimate fees."""

    identifier: Optional[str] = Field(default=UNSET, alias="Identifier")
    """A caller-supplied identifier echoed back in the response for correlation."""

    optional_fulfillment_program: Optional[OptionalFulfillmentProgramOrStr] = Field(
        default=UNSET, alias="OptionalFulfillmentProgram"
    )
    """Optional fulfillment program override for WFS items."""


class FeesEstimateRequestDict(TypedDict):
    marketplace_id: str
    is_walmart_fulfilled: bool
    price_to_estimate_fees: PriceToEstimateFeesDict
    identifier: NotRequired[str]
    optional_fulfillment_program: NotRequired[OptionalFulfillmentProgramOrStr]
