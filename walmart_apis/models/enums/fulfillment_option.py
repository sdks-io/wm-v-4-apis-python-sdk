from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentOption(str, Enum):
    S2_H = "S2H"
    S2_S = "S2S"
    PICKUP_TODAY = "PICKUP_TODAY"

    __str__ = str.__str__


FulfillmentOptionOrStr: TypeAlias = Annotated[FulfillmentOption | str, open_enum_validator(FulfillmentOption)]
