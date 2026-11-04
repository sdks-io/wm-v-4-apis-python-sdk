from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancellationReason(str, Enum):
    """Reason for canceling the order line."""

    CUSTOMER_REQUESTED = "CUSTOMER_REQUESTED"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PRICE_ERROR = "PRICE_ERROR"
    SELLER_INITIATED = "SELLER_INITIATED"

    __str__ = str.__str__


CancellationReasonOrStr: TypeAlias = Annotated[CancellationReason | str, open_enum_validator(CancellationReason)]
