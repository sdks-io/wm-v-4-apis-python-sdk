from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict


class GetOrderResponse(SdkBaseModel):
    """Details of the requested order."""

    payload: Optional[Order] = UNSET
    """Identifiers, status, fulfillment, pricing, and line details for a purchase order."""


class GetOrderResponseDict(TypedDict):
    payload: NotRequired[OrderDict]
