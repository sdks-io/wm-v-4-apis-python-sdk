from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderItemDisposition(str, Enum):
    SELLABLE = "Sellable"
    UNSELLABLE = "Unsellable"

    __str__ = str.__str__


OrderItemDispositionOrStr: TypeAlias = Annotated[OrderItemDisposition | str, open_enum_validator(OrderItemDisposition)]
