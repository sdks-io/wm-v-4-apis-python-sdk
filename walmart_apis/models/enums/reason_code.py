from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReasonCode(str, Enum):
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
    ASIN_NOT_APPLICABLE = "ASIN_NOT_APPLICABLE"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"
    INELIGIBLE_ITEM_CONDITION = "INELIGIBLE_ITEM_CONDITION"
    COMPLIANCE_BLOCKED = "COMPLIANCE_BLOCKED"
    HAZMAT = "HAZMAT"
    RECALLED = "RECALLED"
    RESTRICTED_CATEGORY = "RESTRICTED_CATEGORY"

    __str__ = str.__str__


ReasonCodeOrStr: TypeAlias = Annotated[ReasonCode | str, open_enum_validator(ReasonCode)]
