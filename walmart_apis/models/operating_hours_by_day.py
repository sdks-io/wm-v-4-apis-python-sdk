from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .day_schedule import DaySchedule, DayScheduleDict


class OperatingHoursByDay(SdkBaseModel):
    """Per-weekday processing schedule."""

    sunday: Optional[DaySchedule] = UNSET
    monday: Optional[DaySchedule] = UNSET
    tuesday: Optional[DaySchedule] = UNSET
    wednesday: Optional[DaySchedule] = UNSET
    thursday: Optional[DaySchedule] = UNSET
    friday: Optional[DaySchedule] = UNSET
    saturday: Optional[DaySchedule] = UNSET


class OperatingHoursByDayDict(TypedDict):
    sunday: NotRequired[DayScheduleDict]
    monday: NotRequired[DayScheduleDict]
    tuesday: NotRequired[DayScheduleDict]
    wednesday: NotRequired[DayScheduleDict]
    thursday: NotRequired[DayScheduleDict]
    friday: NotRequired[DayScheduleDict]
    saturday: NotRequired[DayScheduleDict]
