from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .taxonomy_product_type_group import TaxonomyProductTypeGroup, TaxonomyProductTypeGroupDict


class TaxonomyCategory(SdkBaseModel):
    category: Optional[str] = UNSET
    """Canonical category name (also the ``category`` query-filter value)."""

    description: Optional[str] = UNSET
    product_type_groups: Optional[list[TaxonomyProductTypeGroup]] = Field(default=UNSET, alias="productTypeGroups")


class TaxonomyCategoryDict(TypedDict):
    category: NotRequired[str]
    description: NotRequired[str]
    product_type_groups: NotRequired[list[TaxonomyProductTypeGroupDict]]
