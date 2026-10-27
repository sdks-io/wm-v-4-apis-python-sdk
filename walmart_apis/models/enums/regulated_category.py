from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RegulatedCategory(str, Enum):
    """Top-level category of regulation that applies. NOT_REGULATED means no verification is required and the rest of
    the fields are informational only."""

    NOT_REGULATED = "NOT_REGULATED"
    ALCOHOL = "ALCOHOL"
    TOBACCO = "TOBACCO"
    AGE_RESTRICTED = "AGE_RESTRICTED"
    PHARMACY = "PHARMACY"

    __str__ = str.__str__


RegulatedCategoryOrStr: TypeAlias = Annotated[RegulatedCategory | str, open_enum_validator(RegulatedCategory)]
