from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonPrepOwner(str, Enum):
    """The owner of the preparations, if special preparations are required."""

    SELLER = "SELLER"
    NONE = "NONE"

    __str__ = str.__str__


CommonPrepOwnerOrStr: TypeAlias = Annotated[CommonPrepOwner | str, open_enum_validator(CommonPrepOwner)]
