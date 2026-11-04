from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrepInstructionsError(SdkBaseModel):
    """An error encountered while processing the ``getPrepInstructions`` request."""

    code: Optional[str] = UNSET
    message: Optional[str] = UNSET
    details: Optional[str] = UNSET


class PrepInstructionsErrorDict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]
    details: NotRequired[str]
