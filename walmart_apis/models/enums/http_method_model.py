from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HttpMethodModel(str, Enum):
    """The HTTP method associated with the individual APIs being called as part of the batch request."""

    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    POST = "POST"

    __str__ = str.__str__


HttpMethodModelOrStr: TypeAlias = Annotated[HttpMethodModel | str, open_enum_validator(HttpMethodModel)]
