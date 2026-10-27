from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentType(str, Enum):
    SELLER_FULFILLED = "SellerFulfilled"
    WFS = "WFS"

    __str__ = str.__str__


FulfillmentTypeOrStr: TypeAlias = Annotated[FulfillmentType | str, open_enum_validator(FulfillmentType)]
