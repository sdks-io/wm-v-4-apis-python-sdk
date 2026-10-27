from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Name(str, Enum):
    """Duration category of the investigation."""

    RESEARCHING_QUANTITY_IN_SHORT_TERM = "researchingQuantityInShortTerm"
    RESEARCHING_QUANTITY_IN_MID_TERM = "researchingQuantityInMidTerm"
    RESEARCHING_QUANTITY_IN_LONG_TERM = "researchingQuantityInLongTerm"

    __str__ = str.__str__


NameOrStr: TypeAlias = Annotated[Name | str, open_enum_validator(Name)]
