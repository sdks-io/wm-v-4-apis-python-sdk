from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict


class GetOrderResponse(SdkBaseModel):
    payload: Optional[Order] = UNSET


class GetOrderResponseDict(TypedDict):
    payload: NotRequired[OrderDict]
