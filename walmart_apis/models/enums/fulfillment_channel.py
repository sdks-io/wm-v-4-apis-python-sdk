from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentChannel(str, Enum):
    """The fulfillment channel for the offer listing. Possible values: WFS, SELLER."""

    WFS = "WFS"
    SELLER = "SELLER"

    __str__ = str.__str__


FulfillmentChannelOrStr: TypeAlias = Annotated[FulfillmentChannel | str, open_enum_validator(FulfillmentChannel)]
