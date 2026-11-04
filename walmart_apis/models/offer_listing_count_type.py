from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OfferListingCountType(SdkBaseModel):
    """Number of offer listings for an item condition."""

    count: int = Field(alias="Count")
    """Number of offer listings for the specified item condition."""

    condition: str
    """Item condition associated with the offer count."""


class OfferListingCountTypeDict(TypedDict):
    count: int
    condition: str
