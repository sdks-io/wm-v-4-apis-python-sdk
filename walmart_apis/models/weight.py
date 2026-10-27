from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.unit1 import Unit1OrStr


class Weight(SdkBaseModel):
    value: float
    unit: Unit1OrStr


class WeightDict(TypedDict):
    value: float
    unit: Unit1OrStr
