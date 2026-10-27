from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentShipmentStatus(str, Enum):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    CANCELLED_BY_FULFILLER = "CANCELLED_BY_FULFILLER"
    CANCELLED_BY_SELLER = "CANCELLED_BY_SELLER"

    __str__ = str.__str__


FulfillmentShipmentStatusOrStr: TypeAlias = Annotated[
    FulfillmentShipmentStatus | str, open_enum_validator(FulfillmentShipmentStatus)
]
