from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload_orders import PayloadOrders, PayloadOrdersDict


class GetOrdersResponse(SdkBaseModel):
    """Orders returned for the current page, with pagination information when available."""

    payload: Optional[PayloadOrders] = UNSET
    """Page of orders and a continuation token when returned."""


class GetOrdersResponseDict(TypedDict):
    payload: NotRequired[PayloadOrdersDict]
