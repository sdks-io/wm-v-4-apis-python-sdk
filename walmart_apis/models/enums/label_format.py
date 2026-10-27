from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LabelFormat(str, Enum):
    PDF = "PDF"
    PNG = "PNG"
    ZPL = "ZPL"
    ZPL300 = "ZPL300"
    SHIPPING_SERVICE_DEFAULT = "ShippingServiceDefault"

    __str__ = str.__str__


LabelFormatOrStr: TypeAlias = Annotated[LabelFormat | str, open_enum_validator(LabelFormat)]
