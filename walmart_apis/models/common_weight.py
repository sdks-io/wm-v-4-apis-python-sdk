from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.common_unit_of_weight import CommonUnitOfWeightOrStr


class CommonWeight(SdkBaseModel):
    """The weight of a package."""

    unit: CommonUnitOfWeightOrStr
    """Unit of the weight being measured."""

    value: float
    """Value of a weight."""


class CommonWeightDict(TypedDict):
    unit: CommonUnitOfWeightOrStr
    value: float
