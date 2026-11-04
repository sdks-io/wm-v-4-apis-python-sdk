from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dimension_unit import DimensionUnit, DimensionUnitOrStr
from .enums.weight_unit import WeightUnit, WeightUnitOrStr


class PackageDimensionsOrders(SdkBaseModel):
    """Physical dimensions and weight of a package."""

    length: Optional[float] = UNSET
    """Length of the package, in the unit specified by ``dimensionUnit``."""

    width: Optional[float] = UNSET
    """Width of the package, in the unit specified by ``dimensionUnit``."""

    height: Optional[float] = UNSET
    """Height of the package, in the unit specified by ``dimensionUnit``."""

    dimension_unit: DimensionUnitOrStr = Field(default=DimensionUnit.IN, alias="dimensionUnit")
    """Unit used for package length, width, and height. Default: ``IN``."""

    weight: Optional[float] = UNSET
    """Weight of the package, in the unit specified by ``weightUnit``."""

    weight_unit: WeightUnitOrStr = Field(default=WeightUnit.LB, alias="weightUnit")
    """Unit used for package weight."""


class PackageDimensionsOrdersDict(TypedDict):
    length: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]
    dimension_unit: NotRequired[DimensionUnitOrStr]
    weight: NotRequired[float]
    weight_unit: NotRequired[WeightUnitOrStr]
