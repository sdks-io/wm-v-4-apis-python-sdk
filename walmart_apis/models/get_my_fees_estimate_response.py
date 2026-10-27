from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_list import ErrorList, ErrorListDict
from .get_my_fees_estimate_result import GetMyFeesEstimateResult, GetMyFeesEstimateResultDict


class GetMyFeesEstimateResponse(SdkBaseModel):
    """Response for single-item fee estimate endpoints. Mirrors SP-API GetMyFeesEstimateResponse."""

    payload: Optional[GetMyFeesEstimateResult] = UNSET
    """Wraps the fee estimate result for a single-item endpoint."""

    errors: Optional[ErrorList] = UNSET


class GetMyFeesEstimateResponseDict(TypedDict):
    payload: NotRequired[GetMyFeesEstimateResultDict]
    errors: NotRequired[ErrorListDict]
