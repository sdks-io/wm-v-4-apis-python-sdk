from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StockStatus(str, Enum):
    """Stock health label based on current days of supply."""

    IN_STOCK = "InStock"
    AT_RISK = "AtRisk"
    OUT_OF_STOCK = "OutOfStock"
    LONG_TERM_OUT_OF_STOCK = "LongTermOutOfStock"
    NEW_TO_WFS = "NewToWfs"

    __str__ = str.__str__


StockStatusOrStr: TypeAlias = Annotated[StockStatus | str, open_enum_validator(StockStatus)]
