from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.grant_type import GrantTypeOrStr


class TokenRequest(SdkBaseModel):
    """Information required to request an OAuth access token. Required properties depend on the selected ``grant_type``:
      - ``client_credentials``: Authenticate the confidential client using HTTP Basic authentication or ``client_id``
            and ``client_secret`` in the request body.
      - ``authorization_code``: Provide ``code``. Public clients must also provide a Proof Key for Code Exchange (PKCE)
            ``code_verifier``. Confidential clients can omit ``code_verifier`` when they authenticate at the token
            operation and provide ``redirect_uri``.
      - ``refresh_token``: Provide ``refresh_token``. Public clients also provide ``client_id``."""

    grant_type: GrantTypeOrStr
    """OAuth grant type used to request the access token."""

    client_id: Optional[str] = UNSET
    """Client ID for the application. Provide this property when using client credentials in the request body or when
    required for a public client. Omit it from the request body when using HTTP Basic authentication."""

    client_secret: Optional[str] = UNSET
    """Client secret used to authenticate a confidential client with credentials in the request body. Omit for public
    clients and when using HTTP Basic authentication. Treat as a secret and do not log it."""

    code: Optional[str] = UNSET
    """Authorization code returned by Walmart Account Login. Used with the ``authorization_code`` grant."""

    code_verifier: Optional[str] = UNSET
    """PKCE verifier associated with the ``code_challenge`` from the authorization request. Required for public clients
    using the ``authorization_code`` grant and recommended for all clients. Confidential clients can omit this property
    only when authenticating at the token operation and providing ``redirect_uri``."""

    refresh_token: Optional[str] = UNSET
    """Previously issued refresh token used with the ``refresh_token`` grant. Treat as a secret and do not log it."""

    redirect_uri: Optional[str] = UNSET
    """Redirect URI for the authorization flow. Required when a confidential client uses the ``authorization_code``
    grant without ``code_verifier``."""

    scope: Optional[str] = UNSET
    """Requested OAuth scope. For ``client_credentials``, this property is accepted but does not reduce the access
    provisioned for the client, and the response does not echo the value. For ``refresh_token``, the requested scope
    must not exceed the scope originally granted."""


class TokenRequestDict(TypedDict):
    grant_type: GrantTypeOrStr
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    code: NotRequired[str]
    code_verifier: NotRequired[str]
    refresh_token: NotRequired[str]
    redirect_uri: NotRequired[str]
    scope: NotRequired[str]
