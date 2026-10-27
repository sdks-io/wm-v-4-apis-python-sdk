from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Error2(str, Enum):
    """Machine-readable error code."""

    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_CLIENT_METADATA = "invalid_client_metadata"
    INVALID_SOFTWARE_STATEMENT = "invalid_software_statement"
    UNAPPROVED_SOFTWARE_STATEMENT = "unapproved_software_statement"

    __str__ = str.__str__


Error2OrStr: TypeAlias = Annotated[Error2 | str, open_enum_validator(Error2)]
