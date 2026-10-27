from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChannelType(str, Enum):
    """Sales-channel hint that lets shipping-v4 route differently for WFS-fulfilled orders, marketplace-seller-fulfilled
    orders, and external (off-Walmart) orders."""

    WALMART_MARKETPLACE = "WALMART_MARKETPLACE"
    EXTERNAL = "EXTERNAL"
    WFS = "WFS"

    __str__ = str.__str__


ChannelTypeOrStr: TypeAlias = Annotated[ChannelType | str, open_enum_validator(ChannelType)]
