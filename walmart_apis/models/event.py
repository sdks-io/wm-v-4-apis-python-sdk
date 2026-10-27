from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .location import Location, LocationDict


class Event(SdkBaseModel):
    event_code: str = Field(alias="eventCode")
    """Carrier-normalized event code (e.g. PICKED_UP, OUT_FOR_DELIVERY, DELIVERED, EXCEPTION)."""

    event_time: RFC3339DateTime = Field(alias="eventTime")
    location: Optional[Location] = UNSET
    description: Optional[str] = UNSET


class EventDict(TypedDict):
    event_code: str
    event_time: RFC3339DateTime
    location: NotRequired[LocationDict]
    description: NotRequired[str]
