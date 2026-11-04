from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DaySchedule(SdkBaseModel):
    is_working_day: Optional[bool] = Field(default=UNSET, alias="isWorkingDay")
    """Whether the supply source processes orders on this day."""

    cut_off_time: Optional[str] = Field(default=UNSET, alias="cutOffTime")
    """Local order cut-off time, 24-hour HH:mm. Omitted on non-working days."""


class DayScheduleDict(TypedDict):
    is_working_day: NotRequired[bool]
    cut_off_time: NotRequired[str]
