from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CodeChallengeMethod(str, Enum):
    S256 = "S256"

    __str__ = str.__str__


CodeChallengeMethodOrStr: TypeAlias = Annotated[CodeChallengeMethod | str, open_enum_validator(CodeChallengeMethod)]
