from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.grant_type1 import GrantType1OrStr
from .enums.response_type import ResponseTypeOrStr
from .enums.token_endpoint_auth_method import TokenEndpointAuthMethod, TokenEndpointAuthMethodOrStr


class ClientRegistrationRequest(SdkBaseModel):
    """RFC 7591 §2 client metadata."""

    redirect_uris: list[str]
    """Registered callback URIs. Enforced by exact match at authorize. HTTPS (or localhost)."""

    token_endpoint_auth_method: TokenEndpointAuthMethodOrStr = TokenEndpointAuthMethod.NONE
    """``none`` for public clients (PKCE), ``client_secret_post``/``client_secret_basic`` for confidential."""

    grant_types: Optional[list[GrantType1OrStr]] = UNSET
    """Grants the client will use."""

    response_types: Optional[list[ResponseTypeOrStr]] = UNSET
    """Must be ``[code]``."""

    client_name: Optional[str] = UNSET
    """Human-readable name shown on the consent screen."""

    scope: Optional[str] = UNSET
    """Space-delimited scopes the client may request (subset of the sellerAuth catalog + ``offline_access``)."""

    client_uri: Optional[str] = UNSET
    """Homepage of the client."""

    logo_uri: Optional[str] = UNSET
    """Logo shown on the consent screen."""

    contacts: Optional[list[str]] = UNSET
    """Contact emails for the client."""


class ClientRegistrationRequestDict(TypedDict):
    redirect_uris: list[str]
    token_endpoint_auth_method: NotRequired[TokenEndpointAuthMethodOrStr]
    grant_types: NotRequired[list[GrantType1OrStr]]
    response_types: NotRequired[list[ResponseTypeOrStr]]
    client_name: NotRequired[str]
    scope: NotRequired[str]
    client_uri: NotRequired[str]
    logo_uri: NotRequired[str]
    contacts: NotRequired[list[str]]
