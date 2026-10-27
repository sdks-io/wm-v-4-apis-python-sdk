from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item1 import Item1, Item1Dict
from .pagination import Pagination, PaginationDict


class ItemSearchResults1(SdkBaseModel):
    number_of_results: int = Field(alias="numberOfResults")
    """Total number of matching listings items"""

    pagination: Optional[Pagination] = UNSET
    items: list[Item1]


class ItemSearchResults1Dict(TypedDict):
    number_of_results: int
    pagination: NotRequired[PaginationDict]
    items: list[Item1Dict]
