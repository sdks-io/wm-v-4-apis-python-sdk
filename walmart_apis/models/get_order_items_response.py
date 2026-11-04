from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload1_orders import Payload1Orders, Payload1OrdersDict


class GetOrderItemsResponse(SdkBaseModel):
    """Response containing the requested order's line items."""

    payload: Optional[Payload1Orders] = UNSET
    """Payload containing the purchase order ID and line items."""


class GetOrderItemsResponseDict(TypedDict):
    payload: NotRequired[Payload1OrdersDict]
