from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .weight import Weight, WeightDict


class ItemShipping(SdkBaseModel):
    quantity: int
    description: str
    unit_price: Optional[Money] = Field(default=UNSET, alias="unitPrice")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    unit_weight: Optional[Weight] = Field(default=UNSET, alias="unitWeight")
    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")


class ItemShippingDict(TypedDict):
    quantity: int
    description: str
    unit_price: NotRequired[MoneyDict]
    unit_weight: NotRequired[WeightDict]
    seller_sku: NotRequired[str]
