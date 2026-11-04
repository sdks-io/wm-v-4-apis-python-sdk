from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConditionTypeProductPricing(str, Enum):
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    NEW = "New"
    RESTORED = "Restored"
    PRE_OWNED = "Pre-Owned"

    __str__ = str.__str__


ConditionTypeProductPricingOrStr: TypeAlias = Annotated[
    ConditionTypeProductPricing | str, open_enum_validator(ConditionTypeProductPricing)
]
