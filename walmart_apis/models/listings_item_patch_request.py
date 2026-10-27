from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .patch_operation import PatchOperation, PatchOperationDict


class ListingsItemPatchRequest(SdkBaseModel):
    product_type: str = Field(alias="productType")
    patches: list[PatchOperation]


class ListingsItemPatchRequestDict(TypedDict):
    product_type: str
    patches: list[PatchOperationDict]
