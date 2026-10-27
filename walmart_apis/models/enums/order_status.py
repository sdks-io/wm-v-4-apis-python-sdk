from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderStatus(str, Enum):
    CREATED = "Created"
    ACKNOWLEDGED = "Acknowledged"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"

    __str__ = str.__str__


OrderStatusOrStr: TypeAlias = Annotated[OrderStatus | str, open_enum_validator(OrderStatus)]
