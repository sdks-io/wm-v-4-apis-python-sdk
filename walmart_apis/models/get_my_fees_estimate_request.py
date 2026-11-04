from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fees_estimate_request import FeesEstimateRequest, FeesEstimateRequestDict


class GetMyFeesEstimateRequest(SdkBaseModel):
    """Pricing and fulfillment information for a single-item fee estimate request."""

    fees_estimate_request: Optional[FeesEstimateRequest] = Field(default=UNSET, alias="FeesEstimateRequest")
    """Pricing and fulfillment information used to estimate fees for an item."""


class GetMyFeesEstimateRequestDict(TypedDict):
    fees_estimate_request: NotRequired[FeesEstimateRequestDict]
