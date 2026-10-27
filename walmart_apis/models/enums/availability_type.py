from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AvailabilityType(str, Enum):
    """Indicates whether the item is available for shipping now, or on a known or an unknown date in the future."""

    NOW = "NOW"
    FUTURE_WITHOUT_DATE = "FUTURE_WITHOUT_DATE"
    FUTURE_WITH_DATE = "FUTURE_WITH_DATE"

    __str__ = str.__str__


AvailabilityTypeOrStr: TypeAlias = Annotated[AvailabilityType | str, open_enum_validator(AvailabilityType)]
