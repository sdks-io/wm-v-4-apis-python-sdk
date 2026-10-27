from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentifierType(str, Enum):
    WALMART_ITEM_ID = "WALMART_ITEM_ID"
    GTIN = "GTIN"
    UPC = "UPC"
    EAN = "EAN"
    ISBN = "ISBN"
    SKU = "SKU"

    __str__ = str.__str__


IdentifierTypeOrStr: TypeAlias = Annotated[IdentifierType | str, open_enum_validator(IdentifierType)]
