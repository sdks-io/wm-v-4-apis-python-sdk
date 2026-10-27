from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fees_estimate_result import FeesEstimateResult, FeesEstimateResultDict


class GetMyFeesEstimateResult(SdkBaseModel):
    """Wraps the fee estimate result for a single-item endpoint."""

    fees_estimate_result: Optional[FeesEstimateResult] = Field(default=UNSET, alias="FeesEstimateResult")
    """Fee estimate result for one item. Status indicates Success, ClientError, or ServiceError. Mirrors SP-API
    FeesEstimateResult."""


class GetMyFeesEstimateResultDict(TypedDict):
    fees_estimate_result: NotRequired[FeesEstimateResultDict]
