from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status_product_fees import StatusProductFeesOrStr
from .fees_estimate import FeesEstimate, FeesEstimateDict
from .fees_estimate_error import FeesEstimateError, FeesEstimateErrorDict
from .fees_estimate_identifier import FeesEstimateIdentifier, FeesEstimateIdentifierDict


class FeesEstimateResult(SdkBaseModel):
    """Fee estimate result for one item, including the outcome, estimated fees, or error information."""

    status: Optional[StatusProductFeesOrStr] = Field(default=UNSET, alias="Status")
    """Outcome of the fee estimate."""

    fees_estimate_identifier: Optional[FeesEstimateIdentifier] = Field(default=UNSET, alias="FeesEstimateIdentifier")
    """Item identifier and request information associated with the fee estimate result."""

    fees_estimate: Optional[FeesEstimate] = Field(default=UNSET, alias="FeesEstimate")
    """Estimated fees for the item, including the total estimate and individual fee components."""

    error: Optional[FeesEstimateError] = Field(default=UNSET, alias="Error")
    """Error information returned when a fee estimate cannot be calculated."""


class FeesEstimateResultDict(TypedDict):
    status: NotRequired[StatusProductFeesOrStr]
    fees_estimate_identifier: NotRequired[FeesEstimateIdentifierDict]
    fees_estimate: NotRequired[FeesEstimateDict]
    error: NotRequired[FeesEstimateErrorDict]
