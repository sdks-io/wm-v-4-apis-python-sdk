from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TokenEndpointAuthMethod(str, Enum):
    """``none`` for public clients (PKCE), ``client_secret_post``/``client_secret_basic`` for confidential."""

    NONE = "none"
    CLIENT_SECRET_POST = "client_secret_post"
    CLIENT_SECRET_BASIC = "client_secret_basic"

    __str__ = str.__str__


TokenEndpointAuthMethodOrStr: TypeAlias = Annotated[
    TokenEndpointAuthMethod | str, open_enum_validator(TokenEndpointAuthMethod)
]
