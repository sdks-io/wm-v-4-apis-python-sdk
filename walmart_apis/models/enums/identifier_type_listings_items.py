from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentifierTypeListingsItems(str, Enum):
    PRODUCT_NAME = "productName"
    SKU = "sku"
    GTIN = "gtin"
    WPID = "wpid"
    UPC = "upc"
    ISBN = "isbn"
    EAN = "ean"
    ITEM_ID = "itemId"
    CONDITION = "condition"

    __str__ = str.__str__


IdentifierTypeListingsItemsOrStr: TypeAlias = Annotated[
    IdentifierTypeListingsItems | str, open_enum_validator(IdentifierTypeListingsItems)
]
