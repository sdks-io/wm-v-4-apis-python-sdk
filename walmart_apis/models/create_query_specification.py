from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination2 import Pagination2, Pagination2Dict


class CreateQuerySpecification(SdkBaseModel):
    query: str
    """Structured query string. Format TBD pending ADR: GraphQL vs Walmart-native query DSL (Pod 4)."""

    pagination: Optional[Pagination2] = UNSET


class CreateQuerySpecificationDict(TypedDict):
    query: str
    pagination: NotRequired[Pagination2Dict]
