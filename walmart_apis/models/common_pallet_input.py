from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_dimensions import CommonDimensions, CommonDimensionsDict
from .common_weight import CommonWeight, CommonWeightDict
from .enums.common_stackability import CommonStackabilityOrStr


class CommonPalletInput(SdkBaseModel):
    """Contains input information about a pallet to be used in the inbound plan."""

    dimensions: Optional[CommonDimensions] = UNSET
    """Measurement of a package's dimensions."""

    quantity: int
    """The number of containers where all other properties like weight or dimensions are identical."""

    stackability: Optional[CommonStackabilityOrStr] = UNSET
    """Indicates whether pallets will be stacked when carrier arrives for pick-up."""

    weight: Optional[CommonWeight] = UNSET
    """The weight of a package."""


class CommonPalletInputDict(TypedDict):
    dimensions: NotRequired[CommonDimensionsDict]
    quantity: int
    stackability: NotRequired[CommonStackabilityOrStr]
    weight: NotRequired[CommonWeightDict]
