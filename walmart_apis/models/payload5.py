from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cancellation_status import CancellationStatusOrStr


class Payload5(SdkBaseModel):
    cancelled: Optional[bool] = UNSET
    """Whether the cancellation was accepted by the carrier."""

    cancellation_status: Optional[CancellationStatusOrStr] = Field(default=UNSET, alias="cancellationStatus")
    message: Optional[str] = UNSET


class Payload5Dict(TypedDict):
    cancelled: NotRequired[bool]
    cancellation_status: NotRequired[CancellationStatusOrStr]
    message: NotRequired[str]
