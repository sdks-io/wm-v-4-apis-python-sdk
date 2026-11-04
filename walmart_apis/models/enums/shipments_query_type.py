from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentsQueryType(str, Enum):
    """Selects which filter combination ``getShipments`` applies (upstream ``QueryType``)."""

    SHIPMENT = "SHIPMENT"
    DATE_RANGE = "DATE_RANGE"
    NEXT_TOKEN = "NEXT_TOKEN"

    __str__ = str.__str__


ShipmentsQueryTypeOrStr: TypeAlias = Annotated[ShipmentsQueryType | str, open_enum_validator(ShipmentsQueryType)]
