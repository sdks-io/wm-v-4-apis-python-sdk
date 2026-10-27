from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rejection_reason import RejectionReasonOrStr
from .enums.verification_status import VerificationStatusOrStr


class UpdateVerificationStatusRequest(SdkBaseModel):
    """Records the seller's verification decision for a regulated order. REJECTED requires a ``rejectionReason``;
    APPROVED leaves ``rejectionReason`` unset."""

    verification_status: VerificationStatusOrStr = Field(alias="verificationStatus")
    """Outcome of the doorstep / pickup identity verification."""

    rejection_reason: Optional[RejectionReasonOrStr] = Field(default=UNSET, alias="rejectionReason")
    """Reason the verification was rejected. Required when ``verificationStatus=REJECTED``; ignored otherwise. Mirrors
    Amazon SP-API's enumerated rejection reasons."""


class UpdateVerificationStatusRequestDict(TypedDict):
    verification_status: VerificationStatusOrStr
    rejection_reason: NotRequired[RejectionReasonOrStr]
