from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludedDatum(str, Enum):
    ATTRIBUTES = "attributes"
    DIMENSIONS = "dimensions"
    IDENTIFIERS = "identifiers"
    IMAGES = "images"
    PRODUCT_TYPES = "productTypes"
    RELATIONSHIPS = "relationships"
    SALES_RANKS = "salesRanks"

    __str__ = str.__str__


IncludedDatumOrStr: TypeAlias = Annotated[IncludedDatum | str, open_enum_validator(IncludedDatum)]
