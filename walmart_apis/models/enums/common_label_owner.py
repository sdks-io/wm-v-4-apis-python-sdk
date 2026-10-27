from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonLabelOwner(str, Enum):
    """Specifies who will label the items. Options include ``SELLER`` and ``NONE``., The owner of the preparations, if
    special preparations are required., Specifies who will label the items. Options include ``SELLER`` and ``NONE``.,
    The owner of the preparations, if special preparations are required., Specifies who will label the items. Options
    include ``SELLER`` and ``NONE``., The owner of the preparations, if special preparations are required."""

    SELLER = "SELLER"
    NONE = "NONE"

    __str__ = str.__str__


CommonLabelOwnerOrStr: TypeAlias = Annotated[CommonLabelOwner | str, open_enum_validator(CommonLabelOwner)]
