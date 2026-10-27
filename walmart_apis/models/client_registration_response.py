from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClientRegistrationResponse(SdkBaseModel):
    """RFC 7591 §3.2.1 registration response."""

    client_id: str
    """Issued client identifier."""

    client_id_issued_at: Optional[int] = UNSET
    """Issue time (Unix epoch seconds)."""

    client_secret: Optional[str] = UNSET
    """Issued only for confidential clients. Treat as a secret; never log."""

    client_secret_expires_at: Optional[int] = UNSET
    """Secret expiry (Unix epoch seconds); 0 = never. Absent for public clients."""

    redirect_uris: list[str]
    """Registered callback URIs."""

    token_endpoint_auth_method: str
    """The registered client authentication method."""

    grant_types: Optional[list[str]] = UNSET
    """Registered grant types."""

    client_name: Optional[str] = UNSET
    """Registered client name."""

    scope: Optional[str] = UNSET
    """Registered scopes."""


class ClientRegistrationResponseDict(TypedDict):
    client_id: str
    client_id_issued_at: NotRequired[int]
    client_secret: NotRequired[str]
    client_secret_expires_at: NotRequired[int]
    redirect_uris: list[str]
    token_endpoint_auth_method: str
    grant_types: NotRequired[list[str]]
    client_name: NotRequired[str]
    scope: NotRequired[str]
