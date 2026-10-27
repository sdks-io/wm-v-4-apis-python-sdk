from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_list import ErrorList, ErrorListDict


class CreateFulfillmentOrderResponse(SdkBaseModel):
    errors: Optional[ErrorList] = UNSET


class CreateFulfillmentOrderResponseDict(TypedDict):
    errors: NotRequired[ErrorListDict]
