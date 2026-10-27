from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.common_unit_of_measurement import CommonUnitOfMeasurementOrStr


class CommonDimensions(SdkBaseModel):
    """Measurement of a package's dimensions."""

    height: float
    """The height of a package."""

    length: float
    """The length of a package."""

    width: float
    """The width of a package."""

    unit_of_measurement: CommonUnitOfMeasurementOrStr = Field(alias="unitOfMeasurement")
    """Unit of linear measure."""


class CommonDimensionsDict(TypedDict):
    height: float
    length: float
    width: float
    unit_of_measurement: CommonUnitOfMeasurementOrStr
