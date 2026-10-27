from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_type_summary import ProductTypeSummary, ProductTypeSummaryDict


class ProductTypeList(SdkBaseModel):
    product_types: Optional[list[ProductTypeSummary]] = Field(default=UNSET, alias="productTypes")


class ProductTypeListDict(TypedDict):
    product_types: NotRequired[list[ProductTypeSummaryDict]]
