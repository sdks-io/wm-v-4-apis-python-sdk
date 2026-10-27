from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error2 import Error2OrStr


class RegistrationError(SdkBaseModel):
    """Dynamic Client Registration error (RFC 7591 §3.2.2)."""

    error: Error2OrStr
    """Machine-readable error code."""

    error_description: Optional[str] = UNSET
    """Human-readable explanation."""


class RegistrationErrorDict(TypedDict):
    error: Error2OrStr
    error_description: NotRequired[str]
