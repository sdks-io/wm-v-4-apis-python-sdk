from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonOwnerConstraint(str, Enum):
    """A constraint that can apply to an individual owner."""

    SELLER_ONLY = "SELLER_ONLY"
    NONE_ONLY = "NONE_ONLY"

    __str__ = str.__str__


CommonOwnerConstraintOrStr: TypeAlias = Annotated[
    CommonOwnerConstraint | str, open_enum_validator(CommonOwnerConstraint)
]
