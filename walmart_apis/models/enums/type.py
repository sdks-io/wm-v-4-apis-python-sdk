from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    """Type of relationship, such as ``VARIATION``, ``ACCESSORY``, or ``BUNDLE_COMPONENT``."""

    VARIATION = "VARIATION"
    ACCESSORY = "ACCESSORY"
    BUNDLE_COMPONENT = "BUNDLE_COMPONENT"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
