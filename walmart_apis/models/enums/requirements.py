from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Requirements(str, Enum):
    LISTING = "LISTING"
    LISTING_PRODUCT_ONLY = "LISTING_PRODUCT_ONLY"
    LISTING_OFFER_ONLY = "LISTING_OFFER_ONLY"

    __str__ = str.__str__


RequirementsOrStr: TypeAlias = Annotated[Requirements | str, open_enum_validator(Requirements)]
