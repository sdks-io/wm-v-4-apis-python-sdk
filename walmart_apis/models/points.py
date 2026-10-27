from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Points(SdkBaseModel):
    points_number: Optional[int] = Field(default=UNSET, alias="pointsNumber")


class PointsDict(TypedDict):
    points_number: NotRequired[int]
