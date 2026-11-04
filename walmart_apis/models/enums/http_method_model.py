from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HttpMethodModel(str, Enum):
    """HTTP method used for the individual API request in the batch."""

    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    POST = "POST"

    __str__ = str.__str__


HttpMethodModelOrStr: TypeAlias = Annotated[HttpMethodModel | str, open_enum_validator(HttpMethodModel)]
