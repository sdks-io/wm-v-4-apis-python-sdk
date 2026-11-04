from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus(str, Enum):
    """Outcome of buyer identity or age verification at pickup."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    __str__ = str.__str__


VerificationStatusOrStr: TypeAlias = Annotated[VerificationStatus | str, open_enum_validator(VerificationStatus)]
