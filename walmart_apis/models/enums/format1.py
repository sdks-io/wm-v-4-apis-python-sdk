from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format1(str, Enum):
    PDF = "PDF"
    PNG = "PNG"
    ZPL203 = "ZPL203"
    ZPL300 = "ZPL300"

    __str__ = str.__str__


Format1OrStr: TypeAlias = Annotated[Format1 | str, open_enum_validator(Format1)]
