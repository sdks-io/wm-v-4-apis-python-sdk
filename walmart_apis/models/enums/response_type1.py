from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResponseType1(str, Enum):
    CODE = "code"

    __str__ = str.__str__


ResponseType1OrStr: TypeAlias = Annotated[ResponseType1 | str, open_enum_validator(ResponseType1)]
