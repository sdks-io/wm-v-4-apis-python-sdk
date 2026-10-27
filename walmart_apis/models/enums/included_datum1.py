from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludedDatum1(str, Enum):
    SUMMARIES = "summaries"
    ATTRIBUTES = "attributes"
    ISSUES = "issues"
    OFFERS = "offers"
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"
    PROCUREMENT = "procurement"

    __str__ = str.__str__


IncludedDatum1OrStr: TypeAlias = Annotated[IncludedDatum1 | str, open_enum_validator(IncludedDatum1)]
