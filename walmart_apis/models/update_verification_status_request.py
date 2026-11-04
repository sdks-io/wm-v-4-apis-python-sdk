from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rejection_reason import RejectionReasonOrStr
from .enums.verification_status import VerificationStatusOrStr


class UpdateVerificationStatusRequest(SdkBaseModel):
    """Records the verification outcome for a regulated order. If ``verificationStatus`` is ``REJECTED``, you must
    provide the ``rejectionReason``."""

    verification_status: VerificationStatusOrStr = Field(alias="verificationStatus")
    """Outcome of buyer identity or age verification at pickup."""

    rejection_reason: Optional[RejectionReasonOrStr] = Field(default=UNSET, alias="rejectionReason")
    """Reason verification was rejected. Required when ``verificationStatus`` is ``REJECTED``. Ignored for
    ``APPROVED``."""


class UpdateVerificationStatusRequestDict(TypedDict):
    verification_status: VerificationStatusOrStr
    rejection_reason: NotRequired[RejectionReasonOrStr]
