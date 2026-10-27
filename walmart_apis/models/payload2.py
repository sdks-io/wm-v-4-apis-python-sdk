from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict


class Payload2(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    orders: Optional[list[Order]] = UNSET


class Payload2Dict(TypedDict):
    next_token: NotRequired[str]
    orders: NotRequired[list[OrderDict]]
