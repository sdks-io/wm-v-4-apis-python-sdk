from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentChannelType(str, Enum):
    """Indicates whether the item is fulfilled by the seller or by Walmart Fulfillment Services."""

    WFS = "WFS"
    SELLER = "SELLER"

    __str__ = str.__str__


FulfillmentChannelTypeOrStr: TypeAlias = Annotated[
    FulfillmentChannelType | str, open_enum_validator(FulfillmentChannelType)
]
