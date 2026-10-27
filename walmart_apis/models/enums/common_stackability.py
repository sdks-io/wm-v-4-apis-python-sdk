from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonStackability(str, Enum):
    """Indicates whether pallets will be stacked when carrier arrives for pick-up."""

    STACKABLE = "STACKABLE"
    NON_STACKABLE = "NON_STACKABLE"

    __str__ = str.__str__


CommonStackabilityOrStr: TypeAlias = Annotated[CommonStackability | str, open_enum_validator(CommonStackability)]
