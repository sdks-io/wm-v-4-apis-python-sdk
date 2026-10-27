from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address1 import Address1, Address1Dict
from .enums.type11 import Type11OrStr


class AccessPoint(SdkBaseModel):
    access_point_id: str = Field(alias="accessPointId")
    name: str
    type_: Optional[Type11OrStr] = Field(default=UNSET, alias="type")
    address: Address1
    operating_hours: Optional[Any] = Field(default=UNSET, alias="operatingHours")
    """Per-day operating hours. Compressed shape; full DayOfWeekTimeMap fidelity tracked in a follow-up PR."""

    timezone: Optional[str] = UNSET
    """IANA timezone name (e.g. America/Los_Angeles)."""


class AccessPointDict(TypedDict):
    access_point_id: str
    name: str
    type_: NotRequired[Type11OrStr]
    address: Address1Dict
    operating_hours: NotRequired[Any]
    timezone: NotRequired[str]
