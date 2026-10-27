from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType(str, Enum):
    LISTINGS_FEED = "LISTINGS_FEED"
    INVENTORY_FEED = "INVENTORY_FEED"
    PRICING_FEED = "PRICING_FEED"
    ITEM_SETUP_FEED = "ITEM_SETUP_FEED"
    ORDER_ACKNOWLEDGEMENT_FEED = "ORDER_ACKNOWLEDGEMENT_FEED"
    ORDER_FULFILLMENT_FEED = "ORDER_FULFILLMENT_FEED"
    ORDER_CANCELLATION_FEED = "ORDER_CANCELLATION_FEED"
    RETIRE_ITEM_FEED = "RETIRE_ITEM_FEED"

    __str__ = str.__str__


FeedTypeOrStr: TypeAlias = Annotated[FeedType | str, open_enum_validator(FeedType)]
