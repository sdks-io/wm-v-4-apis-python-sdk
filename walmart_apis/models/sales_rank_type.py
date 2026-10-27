from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SalesRankType(SdkBaseModel):
    """Sales rank information for the item, by category."""

    product_category_id: str = Field(alias="ProductCategoryId")
    """Identifies the item category from which the sales rank is taken."""

    rank: int = Field(alias="Rank")
    """The sales rank of the item within the item category."""


class SalesRankTypeDict(TypedDict):
    product_category_id: str
    rank: int
