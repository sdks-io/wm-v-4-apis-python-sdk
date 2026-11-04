from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fees_estimate_result import FeesEstimateResult, FeesEstimateResultDict


class GetMyFeesEstimateResult(SdkBaseModel):
    """Fee estimate result returned for a single-item request."""

    fees_estimate_result: Optional[FeesEstimateResult] = Field(default=UNSET, alias="FeesEstimateResult")
    """Fee estimate result for one item, including the outcome, estimated fees, or error information."""


class GetMyFeesEstimateResultDict(TypedDict):
    fees_estimate_result: NotRequired[FeesEstimateResultDict]
