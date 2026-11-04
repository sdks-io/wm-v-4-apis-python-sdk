from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatusMerchantFulfillmentSellerFulfilledLabels(str, Enum):
    PURCHASED = "PURCHASED"
    REFUNDED = "REFUNDED"
    SHIPPED = "SHIPPED"

    __str__ = str.__str__


ShipmentStatusMerchantFulfillmentSellerFulfilledLabelsOrStr: TypeAlias = Annotated[
    ShipmentStatusMerchantFulfillmentSellerFulfilledLabels | str,
    open_enum_validator(ShipmentStatusMerchantFulfillmentSellerFulfilledLabels),
]
