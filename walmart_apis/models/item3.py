from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .weight import Weight, WeightDict


class Item3(SdkBaseModel):
    quantity: int
    description: str
    unit_price: Optional[Money] = Field(default=UNSET, alias="unitPrice")
    unit_weight: Optional[Weight] = Field(default=UNSET, alias="unitWeight")
    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")


class Item3Dict(TypedDict):
    quantity: int
    description: str
    unit_price: NotRequired[MoneyDict]
    unit_weight: NotRequired[WeightDict]
    seller_sku: NotRequired[str]
