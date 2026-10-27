from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Error(str, Enum):
    """Machine-readable error code."""

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"

    __str__ = str.__str__


ErrorOrStr: TypeAlias = Annotated[Error | str, open_enum_validator(Error)]
