from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepInstructionsErrorReason(str, Enum):
    """The reason a requested seller SKU or ASIN could not be resolved."""

    DOES_NOT_EXIST = "DoesNotExist"
    INVALID_ASIN = "InvalidASIN"

    __str__ = str.__str__


PrepInstructionsErrorReasonOrStr: TypeAlias = Annotated[
    PrepInstructionsErrorReason | str, open_enum_validator(PrepInstructionsErrorReason)
]
