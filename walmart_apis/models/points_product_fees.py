from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PointsProductFees(SdkBaseModel):
    """Walmart Rewards points information used in the fee estimate."""

    points_number: Optional[int] = Field(default=UNSET, alias="PointsNumber")
    """Number of Walmart Rewards points."""


class PointsProductFeesDict(TypedDict):
    points_number: NotRequired[int]
