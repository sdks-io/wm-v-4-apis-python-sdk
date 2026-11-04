from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepInstructionFulfillmentInboundShipments(str, Enum):
    """Type of preparation required. Possible values: BAG, TAPE, WRAP, LABEL."""

    BAG = "BAG"
    TAPE = "TAPE"
    WRAP = "WRAP"
    LABEL = "LABEL"

    __str__ = str.__str__


PrepInstructionFulfillmentInboundShipmentsOrStr: TypeAlias = Annotated[
    PrepInstructionFulfillmentInboundShipments | str, open_enum_validator(PrepInstructionFulfillmentInboundShipments)
]
