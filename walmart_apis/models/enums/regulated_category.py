from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RegulatedCategory(str, Enum):
    """Category of regulation associated with the order. ``NOT_REGULATED`` indicates that no regulated category has been
    identified."""

    NOT_REGULATED = "NOT_REGULATED"
    ALCOHOL = "ALCOHOL"
    TOBACCO = "TOBACCO"
    AGE_RESTRICTED = "AGE_RESTRICTED"
    PHARMACY = "PHARMACY"

    __str__ = str.__str__


RegulatedCategoryOrStr: TypeAlias = Annotated[RegulatedCategory | str, open_enum_validator(RegulatedCategory)]
