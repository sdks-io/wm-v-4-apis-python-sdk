from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QuantityDiscountType(str, Enum):
    """Indicates the type of quantity discount this price applies to."""

    QUANTITY_DISCOUNT = "QUANTITY_DISCOUNT"

    __str__ = str.__str__


QuantityDiscountTypeOrStr: TypeAlias = Annotated[QuantityDiscountType | str, open_enum_validator(QuantityDiscountType)]
