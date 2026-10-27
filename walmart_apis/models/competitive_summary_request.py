from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.included_datum2 import IncludedDatum2OrStr


class CompetitiveSummaryRequest(SdkBaseModel):
    """An individual competitive summary request."""

    walmart_item_id: str = Field(alias="walmartItemId")
    """The Walmart Item ID of the item ."""

    marketplace_id: str = Field(alias="marketplaceId")
    """A marketplace identifier."""

    included_data: list[IncludedDatum2OrStr] = Field(alias="includedData")
    """The list of requested competitive pricing data for the product."""


class CompetitiveSummaryRequestDict(TypedDict):
    walmart_item_id: str
    marketplace_id: str
    included_data: list[IncludedDatum2OrStr]
