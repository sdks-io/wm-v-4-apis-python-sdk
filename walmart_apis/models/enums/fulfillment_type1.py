from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentType1(str, Enum):
    SELLER_FULFILLED = "SellerFulfilled"
    WFS = "WFS"

    __str__ = str.__str__


FulfillmentType1OrStr: TypeAlias = Annotated[FulfillmentType1 | str, open_enum_validator(FulfillmentType1)]
