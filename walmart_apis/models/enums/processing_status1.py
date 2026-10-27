from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessingStatus1(str, Enum):
    """Current processing status of the feed"""

    RECEIVED = "RECEIVED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    ERROR = "ERROR"

    __str__ = str.__str__


ProcessingStatus1OrStr: TypeAlias = Annotated[ProcessingStatus1 | str, open_enum_validator(ProcessingStatus1)]
