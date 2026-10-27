from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConditionType1(str, Enum):
    NEW_NEW = "new_new"
    USED_LIKE_NEW = "used_like_new"
    USED_VERY_GOOD = "used_very_good"
    USED_GOOD = "used_good"
    USED_ACCEPTABLE = "used_acceptable"
    COLLECTIBLE_LIKE_NEW = "collectible_like_new"
    COLLECTIBLE_VERY_GOOD = "collectible_very_good"
    COLLECTIBLE_GOOD = "collectible_good"
    COLLECTIBLE_ACCEPTABLE = "collectible_acceptable"
    REFURBISHED_REFURBISHED = "refurbished_refurbished"

    __str__ = str.__str__


ConditionType1OrStr: TypeAlias = Annotated[ConditionType1 | str, open_enum_validator(ConditionType1)]
