from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TokenResponse(SdkBaseModel):
    access_token: str
    """Opaque Bearer access token. Treat as a secret; never log."""

    token_type: Literal["Bearer"] = "Bearer"
    """Always ``Bearer`` (RFC 6750)."""

    expires_in: int
    """Access-token lifetime in seconds (≈900 today)."""

    refresh_token: Optional[str] = UNSET
    """Rotated refresh token — replaces the one presented (OAuth 2.1 §4.3.1). Present only on delegated grants when
    ``offline_access`` was granted. Treat as a secret; never log."""

    scope: Optional[str] = UNSET
    """Space-delimited granted scopes; present on delegated grants when narrowed from the original grant."""


class TokenResponseDict(TypedDict):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    refresh_token: NotRequired[str]
    scope: NotRequired[str]
