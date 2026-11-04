from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TypeShipping(str, Enum):
    LABEL = "LABEL"
    RECEIPT = "RECEIPT"
    CUSTOMS_FORM = "CUSTOMS_FORM"
    COMMERCIAL_INVOICE = "COMMERCIAL_INVOICE"

    __str__ = str.__str__


TypeShippingOrStr: TypeAlias = Annotated[TypeShipping | str, open_enum_validator(TypeShipping)]
