from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancellationStatus(str, Enum):
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"

    __str__ = str.__str__


CancellationStatusOrStr: TypeAlias = Annotated[CancellationStatus | str, open_enum_validator(CancellationStatus)]
