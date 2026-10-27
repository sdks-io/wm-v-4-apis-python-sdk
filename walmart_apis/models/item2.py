from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Item2(SdkBaseModel):
    order_item_id: str = Field(alias="orderItemId")
    quantity: int


class Item2Dict(TypedDict):
    order_item_id: str
    quantity: int
