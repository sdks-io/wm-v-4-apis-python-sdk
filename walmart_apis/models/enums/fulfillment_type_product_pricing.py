from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentTypeProductPricing(str, Enum):
    """Fulfillment type for the offer. Possible values are ``WFS`` and ``SELLER``."""

    WFS = "WFS"
    SELLER = "SELLER"

    __str__ = str.__str__


FulfillmentTypeProductPricingOrStr: TypeAlias = Annotated[
    FulfillmentTypeProductPricing | str, open_enum_validator(FulfillmentTypeProductPricing)
]
