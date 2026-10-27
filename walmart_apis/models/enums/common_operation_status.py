from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonOperationStatus(str, Enum):
    """The status of an operation."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"

    __str__ = str.__str__


CommonOperationStatusOrStr: TypeAlias = Annotated[
    CommonOperationStatus | str, open_enum_validator(CommonOperationStatus)
]
