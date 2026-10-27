from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .access_point import AccessPoint, AccessPointDict


class Payload6(SdkBaseModel):
    access_points: Optional[list[AccessPoint]] = Field(default=UNSET, alias="accessPoints")


class Payload6Dict(TypedDict):
    access_points: NotRequired[list[AccessPointDict]]
