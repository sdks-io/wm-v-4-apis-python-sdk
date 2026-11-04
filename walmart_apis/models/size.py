from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit import UnitOrStr


class Size(SdkBaseModel):
    width: Optional[float] = UNSET
    length: Optional[float] = UNSET
    unit: Optional[UnitOrStr] = UNSET


class SizeDict(TypedDict):
    width: NotRequired[float]
    length: NotRequired[float]
    unit: NotRequired[UnitOrStr]
