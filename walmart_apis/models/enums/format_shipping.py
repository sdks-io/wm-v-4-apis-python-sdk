from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FormatShipping(str, Enum):
    PDF = "PDF"
    PNG = "PNG"
    ZPL203 = "ZPL203"
    ZPL300 = "ZPL300"

    __str__ = str.__str__


FormatShippingOrStr: TypeAlias = Annotated[FormatShipping | str, open_enum_validator(FormatShipping)]
