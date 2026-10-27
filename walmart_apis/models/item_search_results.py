from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict
from .pagination import Pagination, PaginationDict
from .refinements import Refinements, RefinementsDict


class ItemSearchResults(SdkBaseModel):
    number_of_results: Optional[int] = Field(default=UNSET, alias="numberOfResults")
    """Total number of matching catalog items"""

    pagination: Optional[Pagination] = UNSET
    refinements: Optional[Refinements] = UNSET
    items: Optional[list[Item]] = UNSET


class ItemSearchResultsDict(TypedDict):
    number_of_results: NotRequired[int]
    pagination: NotRequired[PaginationDict]
    refinements: NotRequired[RefinementsDict]
    items: NotRequired[list[ItemDict]]
