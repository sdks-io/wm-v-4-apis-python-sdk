from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusPayments(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    TRANSFERRED = "Transferred"

    __str__ = str.__str__


StatusPaymentsOrStr: TypeAlias = Annotated[StatusPayments | str, open_enum_validator(StatusPayments)]
