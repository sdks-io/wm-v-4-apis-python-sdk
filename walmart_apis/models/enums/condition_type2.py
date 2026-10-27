from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConditionType2(str, Enum):
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""

    NEW = "New"
    USED = "Used"
    COLLECTIBLE = "Collectible"
    REFURBISHED = "Refurbished"
    CLUB = "Club"

    __str__ = str.__str__


ConditionType2OrStr: TypeAlias = Annotated[ConditionType2 | str, open_enum_validator(ConditionType2)]
