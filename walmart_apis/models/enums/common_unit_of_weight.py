from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonUnitOfWeight(str, Enum):
    """Unit of the weight being measured."""

    LB = "LB"
    KG = "KG"

    __str__ = str.__str__


CommonUnitOfWeightOrStr: TypeAlias = Annotated[CommonUnitOfWeight | str, open_enum_validator(CommonUnitOfWeight)]
