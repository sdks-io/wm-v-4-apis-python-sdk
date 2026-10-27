from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status21(str, Enum):
    OPEN = "Open"
    UNDER_REVIEW = "UnderReview"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

    __str__ = str.__str__


Status21OrStr: TypeAlias = Annotated[Status21 | str, open_enum_validator(Status21)]
