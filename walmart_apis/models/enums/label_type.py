from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LabelType(str, Enum):
    UNIQUE = "UNIQUE"
    BARCODE_2_D = "BARCODE_2D"
    PALLET = "PALLET"

    __str__ = str.__str__


LabelTypeOrStr: TypeAlias = Annotated[LabelType | str, open_enum_validator(LabelType)]
