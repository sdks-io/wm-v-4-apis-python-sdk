from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.prep_instructions_error_reason import PrepInstructionsErrorReasonOrStr


class InvalidAsinDetail(SdkBaseModel):
    """A requested ASIN that could not be resolved, with the reason."""

    asin: Optional[str] = UNSET
    error_reason: Optional[PrepInstructionsErrorReasonOrStr] = Field(default=UNSET, alias="errorReason")
    """The reason a requested seller SKU or ASIN could not be resolved."""


class InvalidAsinDetailDict(TypedDict):
    asin: NotRequired[str]
    error_reason: NotRequired[PrepInstructionsErrorReasonOrStr]
