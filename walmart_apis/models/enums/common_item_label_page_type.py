from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonItemLabelPageType(str, Enum):
    """The page type to use to print the labels."""

    A4_21 = "A4_21"
    A4_24 = "A4_24"
    A4_24_64X33 = "A4_24_64x33"
    A4_24_66X35 = "A4_24_66x35"
    A4_24_70X36 = "A4_24_70x36"
    A4_24_70X37 = "A4_24_70x37"
    A4_24I = "A4_24i"
    A4_27 = "A4_27"
    A4_40_52X29 = "A4_40_52x29"
    A4_44_48X25 = "A4_44_48x25"
    LETTER_30 = "Letter_30"

    __str__ = str.__str__


CommonItemLabelPageTypeOrStr: TypeAlias = Annotated[
    CommonItemLabelPageType | str, open_enum_validator(CommonItemLabelPageType)
]
