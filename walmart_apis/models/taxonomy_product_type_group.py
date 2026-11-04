from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_type_summary import ProductTypeSummary, ProductTypeSummaryDict


class TaxonomyProductTypeGroup(SdkBaseModel):
    product_type_group_name: Optional[str] = Field(default=UNSET, alias="productTypeGroupName")
    description: Optional[str] = UNSET
    product_types: Optional[list[ProductTypeSummary]] = Field(default=UNSET, alias="productTypes")


class TaxonomyProductTypeGroupDict(TypedDict):
    product_type_group_name: NotRequired[str]
    description: NotRequired[str]
    product_types: NotRequired[list[ProductTypeSummaryDict]]
