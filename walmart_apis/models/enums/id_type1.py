from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdType1(str, Enum):
    WALMART_ITEM_ID = "WalmartItemId"
    SELLER_SKU = "SellerSKU"

    __str__ = str.__str__


IdType1OrStr: TypeAlias = Annotated[IdType1 | str, open_enum_validator(IdType1)]
