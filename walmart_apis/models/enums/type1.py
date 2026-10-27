from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type1(str, Enum):
    LABEL = "LABEL"
    RECEIPT = "RECEIPT"
    CUSTOMS_FORM = "CUSTOMS_FORM"
    COMMERCIAL_INVOICE = "COMMERCIAL_INVOICE"

    __str__ = str.__str__


Type1OrStr: TypeAlias = Annotated[Type1 | str, open_enum_validator(Type1)]
