from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.prep_instructions_error_reason import PrepInstructionsErrorReasonOrStr


class InvalidSkuDetail(SdkBaseModel):
    """A requested seller SKU that could not be resolved, with the reason."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")
    error_reason: Optional[PrepInstructionsErrorReasonOrStr] = Field(default=UNSET, alias="errorReason")
    """The reason a requested seller SKU or ASIN could not be resolved."""


class InvalidSkuDetailDict(TypedDict):
    seller_sku: NotRequired[str]
    error_reason: NotRequired[PrepInstructionsErrorReasonOrStr]
