from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NdrAction(str, Enum):
    RETURN_TO_ORIGIN = "RETURN_TO_ORIGIN"
    REATTEMPT_DELIVERY = "REATTEMPT_DELIVERY"
    REDIRECT_TO_ACCESS_POINT = "REDIRECT_TO_ACCESS_POINT"
    CONTACT_BUYER = "CONTACT_BUYER"

    __str__ = str.__str__


NdrActionOrStr: TypeAlias = Annotated[NdrAction | str, open_enum_validator(NdrAction)]
