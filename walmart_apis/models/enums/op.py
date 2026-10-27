from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Op(str, Enum):
    """Patch operation type (JSON Patch)"""

    ADD = "add"
    REPLACE = "replace"
    DELETE = "delete"

    __str__ = str.__str__


OpOrStr: TypeAlias = Annotated[Op | str, open_enum_validator(Op)]
