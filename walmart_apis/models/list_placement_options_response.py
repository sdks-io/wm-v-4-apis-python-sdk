from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .common_placement_option import CommonPlacementOption, CommonPlacementOptionDict


class ListPlacementOptionsResponse(SdkBaseModel):
    """The ``listPlacementOptions`` response."""

    placement_options: list[CommonPlacementOption] = Field(alias="placementOptions")
    """Placement options generated for the inbound plan."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListPlacementOptionsResponseDict(TypedDict):
    placement_options: list[CommonPlacementOptionDict]
    pagination: NotRequired[CommonPaginationDict]
