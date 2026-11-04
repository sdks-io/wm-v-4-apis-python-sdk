from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict
from .pagination import Pagination, PaginationDict
from .refinements import Refinements, RefinementsDict


class ItemSearchResults(SdkBaseModel):
    """Matching catalog items, result count, and available search navigation information."""

    number_of_results: Optional[int] = Field(default=UNSET, alias="numberOfResults")
    """Number of matching catalog items reported by the search."""

    pagination: Optional[Pagination] = UNSET
    """Pagination tokens, when available for the search operation."""

    refinements: Optional[Refinements] = UNSET
    """Department and classification information associated with search results."""

    items: Optional[list[Item]] = UNSET


class ItemSearchResultsDict(TypedDict):
    number_of_results: NotRequired[int]
    pagination: NotRequired[PaginationDict]
    refinements: NotRequired[RefinementsDict]
    items: NotRequired[list[ItemDict]]
