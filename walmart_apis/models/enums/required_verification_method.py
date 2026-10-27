from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequiredVerificationMethod(str, Enum):
    """How the buyer must prove identity at delivery. NONE means no verification is required (NOT_REGULATED orders
    always return NONE)."""

    NONE = "NONE"
    DRIVERS_LICENSE = "DRIVERS_LICENSE"
    PASSPORT = "PASSPORT"
    GOVERNMENT_ID = "GOVERNMENT_ID"

    __str__ = str.__str__


RequiredVerificationMethodOrStr: TypeAlias = Annotated[
    RequiredVerificationMethod | str, open_enum_validator(RequiredVerificationMethod)
]
