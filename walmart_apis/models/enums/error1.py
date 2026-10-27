from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Error1(str, Enum):
    """Machine-readable error code."""

    INVALID_REQUEST = "invalid_request"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    ACCESS_DENIED = "access_denied"
    UNSUPPORTED_RESPONSE_TYPE = "unsupported_response_type"
    INVALID_SCOPE = "invalid_scope"
    SERVER_ERROR = "server_error"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"

    __str__ = str.__str__


Error1OrStr: TypeAlias = Annotated[Error1 | str, open_enum_validator(Error1)]
