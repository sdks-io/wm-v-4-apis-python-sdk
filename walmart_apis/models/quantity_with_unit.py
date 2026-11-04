from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit_orders import UnitOrdersOrStr


class QuantityWithUnit(SdkBaseModel):
    """Numeric quantity and its unit of measure."""

    amount: Optional[float] = UNSET
    """Numeric quantity in the specified unit."""

    unit: Optional[UnitOrdersOrStr] = UNSET
    """Unit of measure for the quantity."""


class QuantityWithUnitDict(TypedDict):
    amount: NotRequired[float]
    unit: NotRequired[UnitOrdersOrStr]
