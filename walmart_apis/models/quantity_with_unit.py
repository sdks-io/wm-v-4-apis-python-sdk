from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit2 import Unit2OrStr


class QuantityWithUnit(SdkBaseModel):
    amount: Optional[float] = UNSET
    unit: Optional[Unit2OrStr] = UNSET


class QuantityWithUnitDict(TypedDict):
    amount: NotRequired[float]
    unit: NotRequired[Unit2OrStr]
