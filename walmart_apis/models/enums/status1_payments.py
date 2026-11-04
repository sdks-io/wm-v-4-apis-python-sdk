from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1Payments(str, Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"
    ON_HOLD = "OnHold"

    __str__ = str.__str__


Status1PaymentsOrStr: TypeAlias = Annotated[Status1Payments | str, open_enum_validator(Status1Payments)]
