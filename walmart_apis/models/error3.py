from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error3(SdkBaseModel):
    """Error response returned when the request is unsuccessful."""

    code: str
    message: str
    details: Optional[str] = UNSET


class Error3Dict(TypedDict):
    code: str
    message: str
    details: NotRequired[str]
