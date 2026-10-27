from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus1(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    __str__ = str.__str__


VerificationStatus1OrStr: TypeAlias = Annotated[VerificationStatus1 | str, open_enum_validator(VerificationStatus1)]
