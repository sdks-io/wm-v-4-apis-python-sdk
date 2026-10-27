from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShippingSpeedCategory(str, Enum):
    STANDARD = "Standard"
    EXPEDITED = "Expedited"
    PRIORITY = "Priority"
    SCHEDULED_DELIVERY = "ScheduledDelivery"

    __str__ = str.__str__


ShippingSpeedCategoryOrStr: TypeAlias = Annotated[
    ShippingSpeedCategory | str, open_enum_validator(ShippingSpeedCategory)
]
