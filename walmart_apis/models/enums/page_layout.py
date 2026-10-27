from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PageLayout(str, Enum):
    DEFAULT = "DEFAULT"
    FOUR_IN_ONE = "FOUR_IN_ONE"

    __str__ = str.__str__


PageLayoutOrStr: TypeAlias = Annotated[PageLayout | str, open_enum_validator(PageLayout)]
