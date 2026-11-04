from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DateRangeFilter(str, Enum):
    LAST_UPDATED_AFTER = "LastUpdatedAfter"
    LAST_UPDATED_BEFORE = "LastUpdatedBefore"

    __str__ = str.__str__


DateRangeFilterOrStr: TypeAlias = Annotated[DateRangeFilter | str, open_enum_validator(DateRangeFilter)]
