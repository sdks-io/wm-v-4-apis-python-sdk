from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludedDatumListingsItems(str, Enum):
    SUMMARIES = "summaries"
    ATTRIBUTES = "attributes"
    ISSUES = "issues"
    OFFERS = "offers"
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"
    PROCUREMENT = "procurement"

    __str__ = str.__str__


IncludedDatumListingsItemsOrStr: TypeAlias = Annotated[
    IncludedDatumListingsItems | str, open_enum_validator(IncludedDatumListingsItems)
]
