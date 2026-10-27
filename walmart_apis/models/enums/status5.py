from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status5(str, Enum):
    PRE_TRANSIT = "PRE_TRANSIT"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    EXCEPTION = "EXCEPTION"
    RETURNED = "RETURNED"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


Status5OrStr: TypeAlias = Annotated[Status5 | str, open_enum_validator(Status5)]
