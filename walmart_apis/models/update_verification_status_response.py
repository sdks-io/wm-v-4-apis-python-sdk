from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.verification_status1 import VerificationStatus1OrStr


class UpdateVerificationStatusResponse(SdkBaseModel):
    """Recorded verification outcome for the order."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    verification_status: Optional[VerificationStatus1OrStr] = Field(default=UNSET, alias="verificationStatus")
    """Result of the buyer identity or age verification."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Date and time when the status was updated, in ISO 8601 format."""


class UpdateVerificationStatusResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    verification_status: NotRequired[VerificationStatus1OrStr]
    updated_at: NotRequired[RFC3339DateTime]
