from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Condition(str, Enum):
    """Item condition."""

    NEW_ITEM = "NewItem"
    USED_LIKE_NEW = "UsedLikeNew"
    USED_VERY_GOOD = "UsedVeryGood"
    USED_GOOD = "UsedGood"
    USED_ACCEPTABLE = "UsedAcceptable"
    COLLECTIBLE_LIKE_NEW = "CollectibleLikeNew"
    COLLECTIBLE_VERY_GOOD = "CollectibleVeryGood"
    COLLECTIBLE_GOOD = "CollectibleGood"
    COLLECTIBLE_ACCEPTABLE = "CollectibleAcceptable"
    REFURBISHED_WITH_WARRANTY = "RefurbishedWithWarranty"
    REFURBISHED = "Refurbished"
    CLUB_ITEM = "ClubItem"

    __str__ = str.__str__


ConditionOrStr: TypeAlias = Annotated[Condition | str, open_enum_validator(Condition)]
