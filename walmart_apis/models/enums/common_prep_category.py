from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonPrepCategory(str, Enum):
    """The preparation category for shipping an item to Walmart's fulfillment network."""

    ADULT = "ADULT"
    BABY = "BABY"
    FC_PROVIDED = "FC_PROVIDED"
    FRAGILE = "FRAGILE"
    GRANULAR = "GRANULAR"
    HANGER = "HANGER"
    LIQUID = "LIQUID"
    PERFORATED = "PERFORATED"
    SET = "SET"
    SHARP = "SHARP"
    SMALL = "SMALL"
    TEXTILE = "TEXTILE"
    UNKNOWN = "UNKNOWN"
    NONE = "NONE"

    __str__ = str.__str__


CommonPrepCategoryOrStr: TypeAlias = Annotated[CommonPrepCategory | str, open_enum_validator(CommonPrepCategory)]
