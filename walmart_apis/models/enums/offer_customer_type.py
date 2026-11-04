from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OfferCustomerType(str, Enum):
    """Indicates whether the offer is business-to-consumer (``B2C``) or business-to-business (``B2B``)."""

    B2_C = "B2C"
    B2_B = "B2B"

    __str__ = str.__str__


OfferCustomerTypeOrStr: TypeAlias = Annotated[OfferCustomerType | str, open_enum_validator(OfferCustomerType)]
