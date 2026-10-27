from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fees_estimate_request import FeesEstimateRequest, FeesEstimateRequestDict


class GetMyFeesEstimateRequest(SdkBaseModel):
    """Request wrapper for single-item fee estimate endpoints. Mirrors SP-API GetMyFeesEstimateRequest."""

    fees_estimate_request: Optional[FeesEstimateRequest] = Field(default=UNSET, alias="FeesEstimateRequest")
    """Fee estimate parameters for a single item. Used in both single-item and batch endpoints. Mirrors SP-API
    FeesEstimateRequest."""


class GetMyFeesEstimateRequestDict(TypedDict):
    fees_estimate_request: NotRequired[FeesEstimateRequestDict]
