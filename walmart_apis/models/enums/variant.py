from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Variant(str, Enum):
    MAIN = "MAIN"
    PT01 = "PT01"
    PT02 = "PT02"
    PT03 = "PT03"
    PT04 = "PT04"
    SWCH = "SWCH"

    __str__ = str.__str__


VariantOrStr: TypeAlias = Annotated[Variant | str, open_enum_validator(Variant)]
