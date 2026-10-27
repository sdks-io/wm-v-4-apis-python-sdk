from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Points1(SdkBaseModel):
    """Walmart Rewards points."""

    points_number: Optional[int] = Field(default=UNSET, alias="PointsNumber")


class Points1Dict(TypedDict):
    points_number: NotRequired[int]
