from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RejectionReason(str, Enum):
    """Reason the verification was rejected. Required when ``verificationStatus=REJECTED``; ignored otherwise. Mirrors
    Amazon SP-API's enumerated rejection reasons."""

    BUYER_CANCELED = "BUYER_CANCELED"
    BUYER_REJECTED = "BUYER_REJECTED"
    ID_EXPIRED = "ID_EXPIRED"
    ID_INVALID = "ID_INVALID"
    ID_UNDERAGE = "ID_UNDERAGE"
    ID_MISMATCH = "ID_MISMATCH"
    OTHER = "OTHER"

    __str__ = str.__str__


RejectionReasonOrStr: TypeAlias = Annotated[RejectionReason | str, open_enum_validator(RejectionReason)]
