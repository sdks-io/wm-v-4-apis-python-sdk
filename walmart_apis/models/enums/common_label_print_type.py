from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonLabelPrintType(str, Enum):
    """Indicates the type of print type for a given label."""

    STANDARD_FORMAT = "STANDARD_FORMAT"
    THERMAL_PRINTING = "THERMAL_PRINTING"

    __str__ = str.__str__


CommonLabelPrintTypeOrStr: TypeAlias = Annotated[CommonLabelPrintType | str, open_enum_validator(CommonLabelPrintType)]
