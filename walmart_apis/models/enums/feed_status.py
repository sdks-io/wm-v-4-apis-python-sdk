from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedStatus(str, Enum):
    RECEIVED = "RECEIVED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    ERROR = "ERROR"

    __str__ = str.__str__


FeedStatusOrStr: TypeAlias = Annotated[FeedStatus | str, open_enum_validator(FeedStatus)]
