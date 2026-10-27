from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeliveryExperience(str, Enum):
    DELIVERY_CONFIRMATION_WITH_ADULT_SIGNATURE = "DeliveryConfirmationWithAdultSignature"
    DELIVERY_CONFIRMATION_WITH_SIGNATURE = "DeliveryConfirmationWithSignature"
    DELIVERY_CONFIRMATION_WITHOUT_SIGNATURE = "DeliveryConfirmationWithoutSignature"
    NO_TRACKING = "NoTracking"

    __str__ = str.__str__


DeliveryExperienceOrStr: TypeAlias = Annotated[DeliveryExperience | str, open_enum_validator(DeliveryExperience)]
