from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundType(str, Enum):
    """Indicates whether the refund is issued for a return (``RETURN``), cancellation (``CANCELLATION``), or goodwill
    adjustment (``GOODWILL``)."""

    RETURN = "RETURN"
    CANCELLATION = "CANCELLATION"
    GOODWILL = "GOODWILL"

    __str__ = str.__str__


RefundTypeOrStr: TypeAlias = Annotated[RefundType | str, open_enum_validator(RefundType)]
