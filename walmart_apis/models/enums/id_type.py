from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdType(str, Enum):
    """Type of item identifier."""

    WALMART_ITEM_ID = "WalmartItemId"
    SELLER_SKU = "SellerSKU"

    __str__ = str.__str__


IdTypeOrStr: TypeAlias = Annotated[IdType | str, open_enum_validator(IdType)]
