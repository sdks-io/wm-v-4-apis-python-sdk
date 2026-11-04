from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .taxonomy_category import TaxonomyCategory, TaxonomyCategoryDict


class Taxonomy(SdkBaseModel):
    categories: Optional[list[TaxonomyCategory]] = UNSET


class TaxonomyDict(TypedDict):
    categories: NotRequired[list[TaxonomyCategoryDict]]
