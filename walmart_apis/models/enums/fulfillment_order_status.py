from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentOrderStatus(str, Enum):
    RECEIVED = "RECEIVED"
    INVALID = "INVALID"
    PLANNING = "PLANNING"
    PROCESSING = "PROCESSING"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    COMPLETE_PARTIALLED = "COMPLETE_PARTIALLED"
    UNFULFILLABLE = "UNFULFILLABLE"

    __str__ = str.__str__


FulfillmentOrderStatusOrStr: TypeAlias = Annotated[
    FulfillmentOrderStatus | str, open_enum_validator(FulfillmentOrderStatus)
]
