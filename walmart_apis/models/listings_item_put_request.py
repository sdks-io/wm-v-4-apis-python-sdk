from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.requirements import Requirements, RequirementsOrStr


class ListingsItemPutRequest(SdkBaseModel):
    product_type: str = Field(alias="productType")
    """Walmart product type for the listing"""

    requirements: RequirementsOrStr = Requirements.LISTING
    attributes: Any
    """JSON object of product attributes matching the product type definition schema"""


class ListingsItemPutRequestDict(TypedDict):
    product_type: str
    requirements: NotRequired[RequirementsOrStr]
    attributes: Any
