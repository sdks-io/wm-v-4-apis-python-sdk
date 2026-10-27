from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_channel_code import FulfillmentChannelCodeOrStr


class FulfillmentAvailability(SdkBaseModel):
    fulfillment_channel_code: Optional[FulfillmentChannelCodeOrStr] = Field(
        default=UNSET, alias="fulfillmentChannelCode"
    )
    quantity: Optional[int] = UNSET
    lead_time_to_deploy: Optional[str] = Field(default=UNSET, alias="leadTimeToDeploy")
    """ISO 8601 duration (e.g. PT2D for 2-day lead time)"""


class FulfillmentAvailabilityDict(TypedDict):
    fulfillment_channel_code: NotRequired[FulfillmentChannelCodeOrStr]
    quantity: NotRequired[int]
    lead_time_to_deploy: NotRequired[str]
