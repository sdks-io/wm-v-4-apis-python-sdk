from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_dimensions import CommonDimensions, CommonDimensionsDict
from .common_weight import CommonWeight, CommonWeightDict
from .enums.common_stackability import CommonStackabilityOrStr


class CommonPallet(SdkBaseModel):
    """Contains information about a pallet used in the inbound plan."""

    dimensions: Optional[CommonDimensions] = UNSET
    """Measurement of a package's dimensions."""

    package_id: str = Field(alias="packageId")
    """Primary key to uniquely identify a Package (Box or Pallet)."""

    quantity: Optional[int] = UNSET
    """The number of containers where all other properties like weight or dimensions are identical."""

    stackability: Optional[CommonStackabilityOrStr] = UNSET
    """Indicates whether pallets will be stacked when carrier arrives for pick-up."""

    weight: Optional[CommonWeight] = UNSET
    """The weight of a package."""


class CommonPalletDict(TypedDict):
    dimensions: NotRequired[CommonDimensionsDict]
    package_id: str
    quantity: NotRequired[int]
    stackability: NotRequired[CommonStackabilityOrStr]
    weight: NotRequired[CommonWeightDict]
