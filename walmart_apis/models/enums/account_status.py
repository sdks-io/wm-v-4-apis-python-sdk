from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"

    __str__ = str.__str__


AccountStatusOrStr: TypeAlias = Annotated[AccountStatus | str, open_enum_validator(AccountStatus)]
