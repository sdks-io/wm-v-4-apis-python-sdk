from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StandardIdForLabel(str, Enum):
    WALMART_ORDER_ID = "WalmartOrderId"

    __str__ = str.__str__


StandardIdForLabelOrStr: TypeAlias = Annotated[StandardIdForLabel | str, open_enum_validator(StandardIdForLabel)]
