from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SellerStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"
    PENDING_APPROVAL = "PendingApproval"

    __str__ = str.__str__


SellerStatusOrStr: TypeAlias = Annotated[SellerStatus | str, open_enum_validator(SellerStatus)]
