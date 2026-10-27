from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludedDatum2(str, Enum):
    FEATURED_BUYING_OPTIONS = "featuredBuyingOptions"
    REFERENCE_PRICES = "referencePrices"
    LOWEST_PRICED_OFFERS = "lowestPricedOffers"
    SIMILAR_ITEMS = "similarItems"

    __str__ = str.__str__


IncludedDatum2OrStr: TypeAlias = Annotated[IncludedDatum2 | str, open_enum_validator(IncludedDatum2)]
