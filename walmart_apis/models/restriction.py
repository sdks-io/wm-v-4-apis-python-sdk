from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reason import Reason, ReasonDict


class Restriction(SdkBaseModel):
    marketplace_id: str = Field(alias="marketplaceId")
    condition_type: str = Field(alias="conditionType")
    reasons: Optional[list[Reason]] = UNSET
    """Empty array means listing is not restricted"""


class RestrictionDict(TypedDict):
    marketplace_id: str
    condition_type: str
    reasons: NotRequired[list[ReasonDict]]
