from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.common_reason_comment import CommonReasonCommentOrStr


class ScheduleSelfShipAppointmentRequest(SdkBaseModel):
    """The ``scheduleSelfShipAppointment`` request."""

    reason_comment: Optional[CommonReasonCommentOrStr] = Field(default=UNSET, alias="reasonComment")
    """Reason for cancelling or rescheduling a self-ship appointment."""


class ScheduleSelfShipAppointmentRequestDict(TypedDict):
    reason_comment: NotRequired[CommonReasonCommentOrStr]
