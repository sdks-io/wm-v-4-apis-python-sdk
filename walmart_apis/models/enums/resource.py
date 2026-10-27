from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Resource(str, Enum):
    FEEDS = "feeds"
    REPORTS = "reports"

    __str__ = str.__str__


ResourceOrStr: TypeAlias = Annotated[Resource | str, open_enum_validator(Resource)]
