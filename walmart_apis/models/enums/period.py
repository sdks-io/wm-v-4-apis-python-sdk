from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period(str, Enum):
    """ISO 8601 duration for schedule recurrence"""

    PT5_M = "PT5M"
    PT15_M = "PT15M"
    PT30_M = "PT30M"
    P1_D = "P1D"
    P2_D = "P2D"
    P3_D = "P3D"
    PT1_H = "PT1H"
    P7_D = "P7D"
    P14_D = "P14D"
    P15_D = "P15D"
    P18_D = "P18D"
    P30_D = "P30D"

    __str__ = str.__str__


PeriodOrStr: TypeAlias = Annotated[Period | str, open_enum_validator(Period)]
