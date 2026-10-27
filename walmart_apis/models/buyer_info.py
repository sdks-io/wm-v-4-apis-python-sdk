from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BuyerInfo(SdkBaseModel):
    """Buyer contact projection. ``buyerPhoneAnonymized`` is masked to the last 4 digits (e.g. ``***-***-0100``); the
    unmasked phone number is never returned by the v4 API."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    buyer_name: Optional[str] = Field(default=UNSET, alias="buyerName")
    buyer_email: Optional[EmailStr] = Field(default=UNSET, alias="buyerEmail")
    buyer_phone_anonymized: Optional[str] = Field(default=UNSET, alias="buyerPhoneAnonymized")
    """Phone with everything but the last four digits masked."""


class BuyerInfoDict(TypedDict):
    purchase_order_id: NotRequired[str]
    buyer_name: NotRequired[str]
    buyer_email: NotRequired[EmailStr]
    buyer_phone_anonymized: NotRequired[str]
