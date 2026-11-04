from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TokenResponse(SdkBaseModel):
    """Optional properties are omitted when absent; they are never serialized as JSON null."""

    access_token: str
    """Opaque Bearer access token. Send this value as ``Authorization: Bearer <token>`` when calling Marketplace V4
    APIs. Treat as a secret and do not log it."""

    token_type: Literal["Bearer"] = "Bearer"
    """Token type for the access token. The value is ``Bearer``."""

    expires_in: int
    """Access token lifetime, in seconds."""

    refresh_token: Optional[str] = UNSET
    """Refresh token returned for delegated authorization when ``offline_access`` was granted. Treat as a secret and do
    not log it."""

    scope: Optional[str] = UNSET
    """Space-delimited OAuth scopes granted for delegated authorization. Present when the delegated scope is narrowed
    from the original grant."""


class TokenResponseDict(TypedDict):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    refresh_token: NotRequired[str]
    scope: NotRequired[str]
