from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_list import ErrorList, ErrorListDict


class CancelFulfillmentOrderResponse(SdkBaseModel):
    errors: Optional[ErrorList] = UNSET
    """RFC 9457 problem details object returned by a failed request. Carries the RFC 9457 standard members plus an
    ``errors`` extension member listing each individual error. Clients must ignore members they don't recognise (RFC
    9457 section 3.2)."""


class CancelFulfillmentOrderResponseDict(TypedDict):
    errors: NotRequired[ErrorListDict]
