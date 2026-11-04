from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusProductFees(str, Enum):
    """Outcome of the fee estimate."""

    SUCCESS = "Success"
    CLIENT_ERROR = "ClientError"
    SERVICE_ERROR = "ServiceError"

    __str__ = str.__str__


StatusProductFeesOrStr: TypeAlias = Annotated[StatusProductFees | str, open_enum_validator(StatusProductFees)]
