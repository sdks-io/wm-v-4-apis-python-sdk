from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerType(str, Enum):
    """Indicates whether to request Consumer or Business offers. Default is Consumer."""

    CONSUMER = "Consumer"
    BUSINESS = "Business"

    __str__ = str.__str__


CustomerTypeOrStr: TypeAlias = Annotated[CustomerType | str, open_enum_validator(CustomerType)]
