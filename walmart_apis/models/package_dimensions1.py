from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.common_unit_of_measurement import CommonUnitOfMeasurement, CommonUnitOfMeasurementOrStr
from .enums.weight_unit import WeightUnit, WeightUnitOrStr


class PackageDimensions1(SdkBaseModel):
    """Physical dimensions of a shipped package. All numeric values are non-negative; unit enums avoid the
    unit-ambiguity bug that bit gmp-orders-mono PayloadUtil pre-2024."""

    length: Optional[float] = UNSET
    width: Optional[float] = UNSET
    height: Optional[float] = UNSET
    dimension_unit: CommonUnitOfMeasurementOrStr = Field(default=CommonUnitOfMeasurement.IN, alias="dimensionUnit")
    weight: Optional[float] = UNSET
    weight_unit: WeightUnitOrStr = Field(default=WeightUnit.LB, alias="weightUnit")


class PackageDimensions1Dict(TypedDict):
    length: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]
    dimension_unit: NotRequired[CommonUnitOfMeasurementOrStr]
    weight: NotRequired[float]
    weight_unit: NotRequired[WeightUnitOrStr]
