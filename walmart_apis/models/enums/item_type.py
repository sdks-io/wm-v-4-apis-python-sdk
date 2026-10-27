from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType(str, Enum):
    WALMART_ITEM_ID = "WalmartItemId"
    SKU = "Sku"

    __str__ = str.__str__


ItemTypeOrStr: TypeAlias = Annotated[ItemType | str, open_enum_validator(ItemType)]
