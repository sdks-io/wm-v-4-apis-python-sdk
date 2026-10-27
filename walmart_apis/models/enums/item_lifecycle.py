from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemLifecycle(str, Enum):
    """Lifecycle state of the item in the Walmart catalog."""

    ACTIVE = "Active"
    RETIRED = "Retired"
    ARCHIVED = "Archived"

    __str__ = str.__str__


ItemLifecycleOrStr: TypeAlias = Annotated[ItemLifecycle | str, open_enum_validator(ItemLifecycle)]
