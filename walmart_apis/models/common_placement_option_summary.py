from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonPlacementOptionSummary(SdkBaseModel):
    """Summary information about a placement option."""

    placement_option_id: str = Field(alias="placementOptionId")
    """The identifier of a placement option."""

    status: str
    """The status of a placement option. Possible values: ``OFFERED``, ``ACCEPTED``."""


class CommonPlacementOptionSummaryDict(TypedDict):
    placement_option_id: str
    status: str
