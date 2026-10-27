from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OfferListingCountType(SdkBaseModel):
    """The number of offer listings with the specified condition."""

    count: int = Field(alias="Count")
    """The number of offer listings."""

    condition: str
    """The condition of the item."""


class OfferListingCountTypeDict(TypedDict):
    count: int
    condition: str
