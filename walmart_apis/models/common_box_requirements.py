from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_weight_range import CommonWeightRange, CommonWeightRangeDict


class CommonBoxRequirements(SdkBaseModel):
    """The requirements for a box in the packing option."""

    weight: CommonWeightRange
    """The range of weights that are allowed for a package."""


class CommonBoxRequirementsDict(TypedDict):
    weight: CommonWeightRangeDict
