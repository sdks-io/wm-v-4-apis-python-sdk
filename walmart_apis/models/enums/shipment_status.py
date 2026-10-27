from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatus(str, Enum):
    PURCHASED = "PURCHASED"
    REFUNDED = "REFUNDED"
    SHIPPED = "SHIPPED"

    __str__ = str.__str__


ShipmentStatusOrStr: TypeAlias = Annotated[ShipmentStatus | str, open_enum_validator(ShipmentStatus)]
