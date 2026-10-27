from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status11(str, Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"
    ON_HOLD = "OnHold"

    __str__ = str.__str__


Status11OrStr: TypeAlias = Annotated[Status11 | str, open_enum_validator(Status11)]
