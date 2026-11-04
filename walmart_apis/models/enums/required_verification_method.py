from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequiredVerificationMethod(str, Enum):
    """Identification method required at delivery. ``NONE`` indicates no verification method."""

    NONE = "NONE"
    DRIVERS_LICENSE = "DRIVERS_LICENSE"
    PASSPORT = "PASSPORT"
    GOVERNMENT_ID = "GOVERNMENT_ID"

    __str__ = str.__str__


RequiredVerificationMethodOrStr: TypeAlias = Annotated[
    RequiredVerificationMethod | str, open_enum_validator(RequiredVerificationMethod)
]
