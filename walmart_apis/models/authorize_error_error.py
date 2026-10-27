from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error1 import Error1OrStr


class AuthorizeErrorError(SdkBaseModel):
    """Authorization-endpoint error (RFC 6749 §4.1.2.1) — non-redirectable case only."""

    error: Error1OrStr
    """Machine-readable error code."""

    error_description: Optional[str] = UNSET
    """Human-readable explanation."""

    error_uri: Optional[str] = UNSET
    """Optional link to error docs."""

    state: Optional[str] = UNSET
    """The ``state`` from the request, when supplied."""


class AuthorizeErrorErrorDict(TypedDict):
    error: Error1OrStr
    error_description: NotRequired[str]
    error_uri: NotRequired[str]
    state: NotRequired[str]
