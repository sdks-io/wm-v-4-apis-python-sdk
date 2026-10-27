from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundType(str, Enum):
    """Why the refund is being issued. Compressed from gmp-orders-mono's 22-entry ``RefundReason`` enum to the three
    classes that actually drive downstream behaviour today (return-flow vs cancel-flow vs goodwill-credit). Free-form
    sub-reason goes in ``reason``."""

    RETURN = "RETURN"
    CANCELLATION = "CANCELLATION"
    GOODWILL = "GOODWILL"

    __str__ = str.__str__


RefundTypeOrStr: TypeAlias = Annotated[RefundType | str, open_enum_validator(RefundType)]
