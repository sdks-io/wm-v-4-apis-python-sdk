from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status4 import Status4OrStr
from .fees_estimate import FeesEstimate, FeesEstimateDict
from .fees_estimate_error import FeesEstimateError, FeesEstimateErrorDict
from .fees_estimate_identifier import FeesEstimateIdentifier, FeesEstimateIdentifierDict


class FeesEstimateResult(SdkBaseModel):
    """Fee estimate result for one item. Status indicates Success, ClientError, or ServiceError. Mirrors SP-API
    FeesEstimateResult."""

    status: Optional[Status4OrStr] = Field(default=UNSET, alias="Status")
    """Outcome of the fee estimate."""

    fees_estimate_identifier: Optional[FeesEstimateIdentifier] = Field(default=UNSET, alias="FeesEstimateIdentifier")
    """Echoes back the item identifier and request parameters that produced this result. Mirrors SP-API
    FeesEstimateIdentifier."""

    fees_estimate: Optional[FeesEstimate] = Field(default=UNSET, alias="FeesEstimate")
    """The estimated fees broken down by component. Mirrors SP-API FeesEstimate."""

    error: Optional[FeesEstimateError] = Field(default=UNSET, alias="Error")
    """Error detail when a fee estimate could not be computed."""


class FeesEstimateResultDict(TypedDict):
    status: NotRequired[Status4OrStr]
    fees_estimate_identifier: NotRequired[FeesEstimateIdentifierDict]
    fees_estimate: NotRequired[FeesEstimateDict]
    error: NotRequired[FeesEstimateErrorDict]
