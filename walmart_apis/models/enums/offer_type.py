from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OfferType(str, Enum):
    B2_C = "B2C"
    B2_B = "B2B"

    __str__ = str.__str__


OfferTypeOrStr: TypeAlias = Annotated[OfferType | str, open_enum_validator(OfferType)]
