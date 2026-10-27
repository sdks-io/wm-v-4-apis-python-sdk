from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error import ErrorOrStr


class OauthErrorModel(SdkBaseModel):
    """OAuth 2.0 token-endpoint error (RFC 6749 §5.2)."""

    error: ErrorOrStr
    """Machine-readable error code."""

    error_description: Optional[str] = UNSET
    """Human-readable explanation."""

    error_uri: Optional[str] = UNSET
    """Optional link to error documentation."""


class OauthErrorModelDict(TypedDict):
    error: ErrorOrStr
    error_description: NotRequired[str]
    error_uri: NotRequired[str]
