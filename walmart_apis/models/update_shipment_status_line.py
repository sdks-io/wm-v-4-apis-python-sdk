from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class UpdateShipmentStatusLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    status_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="statusQuantity")


class UpdateShipmentStatusLineDict(TypedDict):
    line_number: str
    status_quantity: NotRequired[QuantityWithUnitDict]
