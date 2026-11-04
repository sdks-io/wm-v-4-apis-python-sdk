from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessingStatusFeeds(str, Enum):
    """Current processing status of the feed"""

    RECEIVED = "RECEIVED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    ERROR = "ERROR"

    __str__ = str.__str__


ProcessingStatusFeedsOrStr: TypeAlias = Annotated[
    ProcessingStatusFeeds | str, open_enum_validator(ProcessingStatusFeeds)
]
