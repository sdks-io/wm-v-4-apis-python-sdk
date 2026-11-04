from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error import ErrorOrStr


class OAuthErrorError(SdkBaseModel):
    """Error information returned when the token request fails. Optional properties are omitted when absent; they are
    never serialized as JSON null.
    """

    error: ErrorOrStr
    """Machine-readable code that identifies the token request error."""

    error_description: Optional[str] = UNSET
    """Human-readable description of the token request error."""

    error_uri: Optional[str] = UNSET
    """Link to additional information about the error. Omitted when no link is available."""


class OAuthErrorErrorDict(TypedDict):
    error: ErrorOrStr
    error_description: NotRequired[str]
    error_uri: NotRequired[str]
