from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .operational_configuration import OperationalConfiguration, OperationalConfigurationDict


class SupplySourceConfiguration(SdkBaseModel):
    """Operating settings for the supply source — time zone and the processing calendar."""

    time_zone: Optional[str] = Field(default=UNSET, alias="timeZone")
    """Time zone the supply source operates in (e.g. PST)."""

    operational_configuration: Optional[OperationalConfiguration] = Field(
        default=UNSET, alias="operationalConfiguration"
    )
    """Operating calendar for the supply source — which weekdays it processes orders, the daily order cut-off, and
    one-off non-working dates."""


class SupplySourceConfigurationDict(TypedDict):
    time_zone: NotRequired[str]
    operational_configuration: NotRequired[OperationalConfigurationDict]
