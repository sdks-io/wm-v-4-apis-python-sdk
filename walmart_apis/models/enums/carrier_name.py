from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CarrierName(str, Enum):
    UPS = "UPS"
    USPS = "USPS"
    FED_EX = "FedEx"
    ON_TRAC = "OnTrac"
    LASER_SHIP = "LaserShip"
    WALMART_GROUND = "WALMART_GROUND"
    OTHER = "OTHER"

    __str__ = str.__str__


CarrierNameOrStr: TypeAlias = Annotated[CarrierName | str, open_enum_validator(CarrierName)]
