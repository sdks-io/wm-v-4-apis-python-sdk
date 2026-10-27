from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FirstDayOfWeek(str, Enum):
    MONDAY = "Monday"
    SUNDAY = "Sunday"

    __str__ = str.__str__


FirstDayOfWeekOrStr: TypeAlias = Annotated[FirstDayOfWeek | str, open_enum_validator(FirstDayOfWeek)]
