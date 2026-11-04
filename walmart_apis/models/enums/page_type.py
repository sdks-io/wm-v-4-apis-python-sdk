from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PageType(str, Enum):
    PACKAGE_LABEL_4X6 = "PackageLabel_4x6"
    PACKAGE_LABEL_4X3 = "PackageLabel_4x3"
    PACKAGE_LABEL_THERMAL = "PackageLabel_Thermal"

    __str__ = str.__str__


PageTypeOrStr: TypeAlias = Annotated[PageType | str, open_enum_validator(PageType)]
