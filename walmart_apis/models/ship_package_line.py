from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class ShipPackageLine(SdkBaseModel):
    """Order line included in a shipped package."""

    line_number: str = Field(alias="lineNumber")
    """Line identifier within the purchase order."""

    ship_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="shipQuantity")
    """Numeric quantity and its unit of measure."""


class ShipPackageLineDict(TypedDict):
    line_number: str
    ship_quantity: NotRequired[QuantityWithUnitDict]
