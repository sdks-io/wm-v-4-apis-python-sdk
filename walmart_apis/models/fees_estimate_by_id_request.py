from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.id_type import IdTypeOrStr
from .fees_estimate_request import FeesEstimateRequest, FeesEstimateRequestDict


class FeesEstimateByIdRequest(SdkBaseModel):
    """A single fee estimate request for the batch endpoint. Combines the item identifier (IdType + IdValue) with the
    fee estimate parameters. Mirrors SP-API FeesEstimateByIdRequest."""

    id_type: IdTypeOrStr = Field(alias="IdType")
    """Type of item identifier."""

    id_value: str = Field(alias="IdValue")
    """The item identifier value (Walmart Item ID or Seller SKU)."""

    fees_estimate_request: FeesEstimateRequest = Field(alias="FeesEstimateRequest")
    """Fee estimate parameters for a single item. Used in both single-item and batch endpoints. Mirrors SP-API
    FeesEstimateRequest."""


class FeesEstimateByIdRequestDict(TypedDict):
    id_type: IdTypeOrStr
    id_value: str
    fees_estimate_request: FeesEstimateRequestDict
