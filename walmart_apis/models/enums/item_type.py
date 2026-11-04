from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType(str, Enum):
    """Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested items."""

    WALMART_ITEM_ID = "WalmartItemId"
    SKU = "Sku"

    __str__ = str.__str__


ItemTypeOrStr: TypeAlias = Annotated[ItemType | str, open_enum_validator(ItemType)]
