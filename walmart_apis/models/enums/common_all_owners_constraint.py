from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonAllOwnersConstraint(str, Enum):
    """A constraint that applies to all owners. If no constraint is specified, defer to any individual owner
    constraints."""

    MUST_MATCH = "MUST_MATCH"

    __str__ = str.__str__


CommonAllOwnersConstraintOrStr: TypeAlias = Annotated[
    CommonAllOwnersConstraint | str, open_enum_validator(CommonAllOwnersConstraint)
]
