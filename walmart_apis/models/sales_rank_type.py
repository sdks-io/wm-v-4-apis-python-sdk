from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SalesRankType(SdkBaseModel):
    """Sales rank information for the item within a specific category."""

    product_category_id: str = Field(alias="ProductCategoryId")
    """Identifies the item category used to determine the sales rank."""

    rank: int = Field(alias="Rank")
    """Sales rank of the item within the specified category."""


class SalesRankTypeDict(TypedDict):
    product_category_id: str
    rank: int
