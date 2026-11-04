from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .operating_hours_by_day import OperatingHoursByDay, OperatingHoursByDayDict


class OperationalConfiguration(SdkBaseModel):
    """Operating calendar for the supply source — which weekdays it processes orders, the daily order cut-off, and
    one-off non-working dates."""

    operating_hours_by_day: OperatingHoursByDay = Field(alias="operatingHoursByDay")
    """Per-weekday processing schedule."""

    additional_days_off: list[Date] = Field(alias="additionalDaysOff")
    """One-off non-working dates, outside the weekly schedule."""


class OperationalConfigurationDict(TypedDict):
    operating_hours_by_day: OperatingHoursByDayDict
    additional_days_off: list[Date]
