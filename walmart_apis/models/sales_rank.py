from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SalesRank(SdkBaseModel):
    """Sales ranking information for a catalog category."""

    category_id: Optional[str] = Field(default=UNSET, alias="categoryId")
    """Identifier of the category associated with the sales rank."""

    rank: Optional[int] = UNSET
    """Sales rank of the item within the category."""

    category_name: Optional[str] = Field(default=UNSET, alias="categoryName")
    """Name of the category associated with the sales rank."""

    link: Optional[str] = UNSET
    """URL associated with the sales ranking category."""


class SalesRankDict(TypedDict):
    category_id: NotRequired[str]
    rank: NotRequired[int]
    category_name: NotRequired[str]
    link: NotRequired[str]
