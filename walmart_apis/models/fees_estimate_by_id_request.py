from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.id_type import IdTypeOrStr
from .fees_estimate_request import FeesEstimateRequest, FeesEstimateRequestDict


class FeesEstimateByIdRequest(SdkBaseModel):
    """Item identifier, pricing information, and fulfillment information for one fee estimate in a batch request."""

    id_type: IdTypeOrStr = Field(alias="IdType")
    """Type of item identifier provided in ``IdValue``."""

    id_value: str = Field(alias="IdValue")
    """Item identifier corresponding to ``IdType``."""

    fees_estimate_request: FeesEstimateRequest = Field(alias="FeesEstimateRequest")
    """Pricing and fulfillment information used to estimate fees for an item."""


class FeesEstimateByIdRequestDict(TypedDict):
    id_type: IdTypeOrStr
    id_value: str
    fees_estimate_request: FeesEstimateRequestDict
