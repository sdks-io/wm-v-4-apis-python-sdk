from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_list import ErrorList, ErrorListDict


class CancelFulfillmentOrderResponse(SdkBaseModel):
    errors: Optional[ErrorList] = UNSET


class CancelFulfillmentOrderResponseDict(TypedDict):
    errors: NotRequired[ErrorListDict]
