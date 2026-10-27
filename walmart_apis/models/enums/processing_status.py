from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessingStatus(str, Enum):
    IN_QUEUE = "IN_QUEUE"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    DONE = "DONE"
    FATAL = "FATAL"

    __str__ = str.__str__


ProcessingStatusOrStr: TypeAlias = Annotated[ProcessingStatus | str, open_enum_validator(ProcessingStatus)]
