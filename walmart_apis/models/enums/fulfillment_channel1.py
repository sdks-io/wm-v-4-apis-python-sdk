from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentChannel1(str, Enum):
    """Indicates whether the item is fulfilled by WFS or the seller."""

    WFS = "WFS"
    SELLER = "SELLER"

    __str__ = str.__str__


FulfillmentChannel1OrStr: TypeAlias = Annotated[FulfillmentChannel1 | str, open_enum_validator(FulfillmentChannel1)]
