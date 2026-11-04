from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepOwner(str, Enum):
    """Party responsible for the prep. Possible values: SELLER, WALMART."""

    SELLER = "SELLER"
    WALMART = "WALMART"

    __str__ = str.__str__


PrepOwnerOrStr: TypeAlias = Annotated[PrepOwner | str, open_enum_validator(PrepOwner)]
