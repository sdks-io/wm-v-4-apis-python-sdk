from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CarrierWillPickUpOption(str, Enum):
    CARRIER_CONTACT = "CarrierContact"
    SELLER_CONTACT = "SellerContact"
    NO_PREFERENCE = "NoPreference"

    __str__ = str.__str__


CarrierWillPickUpOptionOrStr: TypeAlias = Annotated[
    CarrierWillPickUpOption | str, open_enum_validator(CarrierWillPickUpOption)
]
