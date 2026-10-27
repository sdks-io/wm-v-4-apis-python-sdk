from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.unit import UnitOrStr


class PackageDimensions(SdkBaseModel):
    length: float
    width: float
    height: float
    unit: UnitOrStr


class PackageDimensionsDict(TypedDict):
    length: float
    width: float
    height: float
    unit: UnitOrStr
