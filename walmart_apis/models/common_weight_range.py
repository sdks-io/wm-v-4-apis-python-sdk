from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.common_unit_of_weight import CommonUnitOfWeightOrStr


class CommonWeightRange(SdkBaseModel):
    """The range of weights that are allowed for a package."""

    maximum: float
    """Maximum allowed weight."""

    minimum: float
    """Minimum allowed weight."""

    unit: CommonUnitOfWeightOrStr
    """Unit of the weight being measured."""


class CommonWeightRangeDict(TypedDict):
    maximum: float
    minimum: float
    unit: CommonUnitOfWeightOrStr
