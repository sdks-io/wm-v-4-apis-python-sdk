from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentChannelCode(str, Enum):
    DEFAULT = "DEFAULT"
    WFS = "WFS"

    __str__ = str.__str__


FulfillmentChannelCodeOrStr: TypeAlias = Annotated[
    FulfillmentChannelCode | str, open_enum_validator(FulfillmentChannelCode)
]
