from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonReasonComment(str, Enum):
    """Reason for cancelling or rescheduling a self-ship appointment."""

    APPOINTMENT_REQUESTED_BY_MISTAKE = "APPOINTMENT_REQUESTED_BY_MISTAKE"
    VEHICLE_DELAY = "VEHICLE_DELAY"
    SLOT_NOT_SUITABLE = "SLOT_NOT_SUITABLE"
    OUTSIDE_CARRIER_BUSINESS_HOURS = "OUTSIDE_CARRIER_BUSINESS_HOURS"
    UNFAVOURABLE_EXTERNAL_CONDITIONS = "UNFAVOURABLE_EXTERNAL_CONDITIONS"
    PROCUREMENT_DELAY = "PROCUREMENT_DELAY"
    SHIPPING_PLAN_CHANGED = "SHIPPING_PLAN_CHANGED"
    INCREASED_QUANTITY = "INCREASED_QUANTITY"
    OTHER = "OTHER"

    __str__ = str.__str__


CommonReasonCommentOrStr: TypeAlias = Annotated[CommonReasonComment | str, open_enum_validator(CommonReasonComment)]
