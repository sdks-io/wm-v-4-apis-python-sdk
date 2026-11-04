from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OptionalFulfillmentProgram(str, Enum):
    """Fulfillment program used for the fee estimate."""

    WFS_STANDARD = "WFS_STANDARD"
    WFS_EXPEDITED = "WFS_EXPEDITED"

    __str__ = str.__str__


OptionalFulfillmentProgramOrStr: TypeAlias = Annotated[
    OptionalFulfillmentProgram | str, open_enum_validator(OptionalFulfillmentProgram)
]
