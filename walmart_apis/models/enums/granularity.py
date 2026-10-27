from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Granularity(str, Enum):
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    TOTAL = "Total"

    __str__ = str.__str__


GranularityOrStr: TypeAlias = Annotated[Granularity | str, open_enum_validator(Granularity)]
