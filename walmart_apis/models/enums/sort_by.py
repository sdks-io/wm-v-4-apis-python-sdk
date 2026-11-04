from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortBy(str, Enum):
    NUM_REVIEWS = "num_reviews"
    CUSTOMER_RATING = "customerRating"
    LIFECYCLE_STATUS = "lifecycleStatus"
    PUBLISHED_STATUS = "publishedStatus"
    UNPUBLISHED_REASONS = "unpublishedReasons"
    INVENTORY_STATUS = "inventoryStatus"

    __str__ = str.__str__


SortByOrStr: TypeAlias = Annotated[SortBy | str, open_enum_validator(SortBy)]
