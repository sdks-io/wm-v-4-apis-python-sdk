from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .researching_quantity_entry import ResearchingQuantityEntry, ResearchingQuantityEntryDict


class ResearchingQuantity(SdkBaseModel):
    """Units under investigation for inventory discrepancies."""

    total_researching_quantity: OptionalNullable[int] = Field(default=UNSET, alias="totalResearchingQuantity")
    """Total units currently under investigation."""

    researching_quantity_breakdown: Optional[list[ResearchingQuantityEntry]] = Field(
        default=UNSET, alias="researchingQuantityBreakdown"
    )
    """Breakdown of researching units by investigation duration."""


class ResearchingQuantityDict(TypedDict):
    total_researching_quantity: NotRequired[int | None]
    researching_quantity_breakdown: NotRequired[list[ResearchingQuantityEntryDict]]
