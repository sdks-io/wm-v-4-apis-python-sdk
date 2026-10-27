from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.grant_type import GrantTypeOrStr


class TokenRequest(SdkBaseModel):
    """Form-encoded token request. Fields required depend on ``grant_type``: ``client_credentials`` (client auth only),
    ``authorization_code`` (``code`` + ``code_verifier``), ``refresh_token`` (``refresh_token``)."""

    grant_type: GrantTypeOrStr
    """The OAuth grant type."""

    client_id: Optional[str] = UNSET
    """Client identifier (client_secret_post / public clients). Omit if using HTTP Basic."""

    client_secret: Optional[str] = UNSET
    """Client secret (client_secret_post). Omit for public clients or HTTP Basic."""

    code: Optional[str] = UNSET
    """Authorization code from ``/auth/v4/authorize`` (authorization_code grant)."""

    code_verifier: Optional[str] = UNSET
    """PKCE verifier whose S256 hash equals the earlier ``code_challenge`` (authorization_code grant)."""

    refresh_token: Optional[str] = UNSET
    """A previously issued refresh token (refresh_token grant). Rotated on use."""

    redirect_uri: Optional[str] = UNSET
    """Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers injection)."""

    scope: Optional[str] = UNSET
    """**client_credentials:** accepted for compatibility but **not honored**
     — no down-scoping; not echoed. **refresh_token:** optional;
    MUST NOT exceed the originally granted scope."""


class TokenRequestDict(TypedDict):
    grant_type: GrantTypeOrStr
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    code: NotRequired[str]
    code_verifier: NotRequired[str]
    refresh_token: NotRequired[str]
    redirect_uri: NotRequired[str]
    scope: NotRequired[str]
