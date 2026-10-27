from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_custom_placement_input import CommonCustomPlacementInput, CommonCustomPlacementInputDict


class GeneratePlacementOptionsRequest(SdkBaseModel):
    """The ``generatePlacementOptions`` request."""

    custom_placement: Optional[list[CommonCustomPlacementInput]] = Field(default=UNSET, alias="customPlacement")
    """Custom placement options to add to the plan."""


class GeneratePlacementOptionsRequestDict(TypedDict):
    custom_placement: NotRequired[list[CommonCustomPlacementInputDict]]
