from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorError(SdkBaseModel):
    """Error response returned when the request is unsuccessful."""

    code: str
    """An error code that identifies the type of error that occurred."""

    message: str
    """A message that describes the error condition."""

    details: Optional[str] = UNSET
    """Additional details that can help the caller understand or fix the issue."""


class ErrorErrorDict(TypedDict):
    code: str
    message: str
    details: NotRequired[str]
