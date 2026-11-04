from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Carrier(str, Enum):
    """Carrier responsible for the shipment."""

    UPS = "UPS"
    USPS = "USPS"
    FED_EX = "FedEx"
    ON_TRAC = "OnTrac"
    LASER_SHIP = "LaserShip"
    WALMART_GROUND = "WALMART_GROUND"
    OTHER = "OTHER"

    __str__ = str.__str__


CarrierOrStr: TypeAlias = Annotated[Carrier | str, open_enum_validator(Carrier)]
