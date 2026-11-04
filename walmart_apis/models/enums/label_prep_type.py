from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LabelPrepType(str, Enum):
    """Labeling requirement for the shipment (upstream ``LabelPrepType``). NOTE : upstream renamed the first value from
    ``NO_LABEL`` to ``SELLER_LABEL`` -- same meaning (seller supplies their own label), clearer name."""

    SELLER_LABEL = "SELLER_LABEL"
    WALMART_LABEL = "WALMART_LABEL"

    __str__ = str.__str__


LabelPrepTypeOrStr: TypeAlias = Annotated[LabelPrepType | str, open_enum_validator(LabelPrepType)]
