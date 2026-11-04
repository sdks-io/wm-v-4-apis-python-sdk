from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_list import ErrorList, ErrorListDict
from .get_my_fees_estimate_result import GetMyFeesEstimateResult, GetMyFeesEstimateResultDict


class GetMyFeesEstimateResponse(SdkBaseModel):
    """Fee estimate result and any errors returned for a single-item request."""

    payload: Optional[GetMyFeesEstimateResult] = UNSET
    """Fee estimate result returned for a single-item request."""

    errors: Optional[ErrorList] = UNSET
    """RFC 9457 problem details object returned by a failed request. Carries the RFC 9457 standard members plus an
    ``errors`` extension member listing each individual error. Clients must ignore members they don't recognise (RFC
    9457 section 3.2)."""


class GetMyFeesEstimateResponseDict(TypedDict):
    payload: NotRequired[GetMyFeesEstimateResultDict]
    errors: NotRequired[ErrorListDict]
