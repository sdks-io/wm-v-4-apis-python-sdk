from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResponseType(str, Enum):
    CODE = "code"

    __str__ = str.__str__


ResponseTypeOrStr: TypeAlias = Annotated[ResponseType | str, open_enum_validator(ResponseType)]
