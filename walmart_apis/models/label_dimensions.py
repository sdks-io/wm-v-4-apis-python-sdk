from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit import UnitOrStr


class LabelDimensions(SdkBaseModel):
    length: Optional[float] = UNSET
    width: Optional[float] = UNSET
    unit: Optional[UnitOrStr] = UNSET


class LabelDimensionsDict(TypedDict):
    length: NotRequired[float]
    width: NotRequired[float]
    unit: NotRequired[UnitOrStr]
