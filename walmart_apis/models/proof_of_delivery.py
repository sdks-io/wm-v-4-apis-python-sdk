from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ProofOfDelivery(SdkBaseModel):
    delivered_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveredTime")
    recipient_name: Optional[str] = Field(default=UNSET, alias="recipientName")
    signature_image: Optional[str] = Field(default=UNSET, alias="signatureImage")
    """Base64-encoded signature image bytes."""


class ProofOfDeliveryDict(TypedDict):
    delivered_time: NotRequired[RFC3339DateTime]
    recipient_name: NotRequired[str]
    signature_image: NotRequired[str]
