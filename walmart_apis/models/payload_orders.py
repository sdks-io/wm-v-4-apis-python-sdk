from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict


class PayloadOrders(SdkBaseModel):
    """Page of orders and a continuation token when returned."""

    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    """Pagination token for retrieving the next page of matching orders."""

    orders: Optional[list[Order]] = UNSET
    """Orders returned for the current page."""


class PayloadOrdersDict(TypedDict):
    next_token: NotRequired[str]
    orders: NotRequired[list[OrderDict]]
