from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderStatus1(str, Enum):
    CREATED = "Created"
    ACKNOWLEDGED = "Acknowledged"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"

    __str__ = str.__str__


OrderStatus1OrStr: TypeAlias = Annotated[OrderStatus1 | str, open_enum_validator(OrderStatus1)]
